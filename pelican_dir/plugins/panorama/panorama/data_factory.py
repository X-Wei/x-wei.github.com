# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from pandas import DataFrame, Series


FUNCTIONS_ALLOWED = ['count_article_by_column_by_year', 'top_article', 'count_article', 'count_article_by_year',
                     'count_article_by_column']


class DataFactory(object):
    """ Responsible to produce data ready to be rendered.
    """

    def __init__(self, metadata_columns, tag_columns):
        """ Store the definition of data (the columns).

        :param metadata_columns: the metadata to extract, only the metadata defined in self.metadata_column are extracted
        :param tag_columns: all tags are extracted, it is used to rename columns instead of automatically generated names
        """
        self.data = None
        self.metadata_columns = metadata_columns
        self.tag_columns = tag_columns

    def parse_data(self, articles):
        """ Responsible to parse articles in order to extract data.
        Data is extracted as a DataFrame containing the following columns:
        - Article metadata: only the metadata defined in self.metadata_column are extracted
        - Article tags: all tags are extracted, the name defined in self.tags_column are used to rename columns
        Data is indexed by a generated ID (integer).

        :param articles: The articles to parse.
        """
        tags = []
        metadata = []
        # TODO not the more efficient way to do that I think.
        for article in articles:
            if hasattr(article, 'tags'):
                # Extracting all tags name from an article and putting them in a Series
                tags.append(
                    Series([tag.name for tag in article.tags], ['tag_' + str(x) for x in range(len(article.tags))]))
            # Selecting metadata, only the ones specified in the columns
            metadata.append(Series(
                dict([(i, article.metadata[i]) for i in self.metadata_columns if i in article.metadata]),
                self.metadata_columns))
        # Creating the tags DataFrame
        tags_data_frame = DataFrame(tags)
        # Renaming columns, leaving the remaining ones with the generated name "tag_"
        # Mapping current column names to the new ones in order to make a replacement
        if self.tag_columns is not None:
            replacement = dict(zip(tags_data_frame.columns.get_values()[:len(self.tag_columns)], self.tag_columns))
            # Inplace means no copy
            tags_data_frame.rename(columns=replacement, inplace=True)
        # Creating the metadata DataFrame
        metadata_data_frame = DataFrame(metadata)
        # Replacing data in column category by its string value
        # TODO maybe a better way to do that, it seems a bit ugly
        metadata_data_frame['category'] = metadata_data_frame['category'].apply(lambda x: str(x))
        # Merging the two DataFrame together
        self.data = metadata_data_frame.join(tags_data_frame)

    def produce(self, producer):
        """ Call the producer method by passing it the data and simply returns the result.
        Producer methods are intended to return:
        - a Series
        - a dict of Series

        :param producer: the producer method to call.
        :return: the
        """
        return producer(data=self.data)

    def get_producer(self, function_name):
        """ Instantiate the function from its name.
        Raises an exception if the function is not allowed.

        :param function_name: the name of the function
        :return: the function
        """
        if function_name not in FUNCTIONS_ALLOWED:
            raise ValueError('Function [%s] not allowed for a renderer' % function_name)
        return eval(function_name)


def count_article_by_column(data, column):
    """ Count the number of articles in data grouped by the specified column.

    :param data: the DataFrame containing articles
    :param column: the column used to group data
    :return: a Series containing the number of articles indexed by column
    """
    return count_article(data.groupby(column))


def count_article_by_year(data):
    """ Count the number of articles in data grouped by year.

    :param data: the DataFrame containing articles
    :return: a Series containing the number of articles indexed by year
    """
    return count_article(data.groupby(lambda x: data['date'][x].year))


def count_article(data):
    """ Count the number of articles in data.

    :param data: the DataFrame containing articles
    :return: a Series containing the number of articles
    """
    return data['title'].count()


def top_article(data, column, top):
    """ Give the top x number of item in column
    :param data: the DataFrame containing articles
    :param column: the column to use to count
    :param top: the number of result to keep
    :return: a Series containing the result
    """
    data = count_article_by_column(data=data, column=column)
    data.sort(ascending=False)
    return data[:top]


def count_article_by_column_by_year(data, column):
    """ Count the number of articles grouped by the specified column over the years.

    :param data: the DataFrame containing articles
    :param column: the column used to group data
    :return: a dict of Series
    """
    # TODO maybe there is a better way to do that, but it works ;-)
    # Computing a range of year to reindex series and filling the gaps
    y_range = range(min(data['date']).year, max(data['date']).year + 1)
    result = []
    # Grouping data by column
    groups = data.groupby([column])
    for group_name, group in groups:
        # Counting by year for each group
        series = count_article_by_year(group)
        series.name = group_name
        # Indexing data to obtain the full year range
        series = series.reindex(y_range)
        # Filling missing values
        series = series.fillna(0)
        result.append(series)
    return result