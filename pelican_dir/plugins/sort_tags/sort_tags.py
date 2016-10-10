'''
sort_tags
===================================

This plugin adds tags_sorted_article_length to the context,
which is a list of tupels (Tag, [Articles]) that is sorted 
by number of Articles first and Tag second.
'''

from operator import itemgetter
from pelican import signals

def sort_tags_by_articles_size(generator):
    most_articles = 0

    for values in generator.tags.values():
        if(len(values) > most_articles):
            most_articles=len(values)
            

    def extract_and_size(item):
        articles = itemgetter(1)(item)
        length = len(articles)
        tag_lower = (itemgetter(0)(item)).slug.lower()
        return (most_articles - len(articles), tag_lower)

    generator.context['tags_sorted_by_article_length'] = sorted(
        generator.tags.items(),
        key=extract_and_size,
        reverse=False)

def register():
    signals.article_generator_finalized.connect(sort_tags_by_articles_size)