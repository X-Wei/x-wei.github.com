# -*- coding: utf-8 -*-
'''
Genealogy Generator
-------

The genealogy plugin generates surname and people lists from the metadata
in each article
'''


from pelican import signals
from pelican.generators import ArticlesGenerator
from pelican.urlwrappers import (URLWrapper)

from collections import defaultdict
from functools import partial
from operator import attrgetter

class Surname(URLWrapper):
    def __init__(self, name, *args, **kwargs):
        super(Surname, self).__init__(name.strip(), *args, **kwargs)

class Person(URLWrapper):
    def __init__(self, name, *args, **kwargs):
        super(Person, self).__init__(name.strip(), *args, **kwargs)


def generate_context(generator):
    generator.surnames = defaultdict(list)
    generator.people = defaultdict(list)

    for article in generator.articles:
        # compile list of articles for each surname
        if hasattr(article,'surnames'):
            surnames = article.surnames.split(',')
            for surname in surnames:
                surname = Surname(surname,generator.settings)
                generator.surnames[surname].append(article)
            article.surnames = surnames
        # compile list of articles for each person
        if hasattr(article, 'people'):
            people = article.people.split(',')
            for person in people:
                person = Person(person,generator.settings)
                generator.people[person].append(article)
            article.people = people

    generator.surnames = list(generator.surnames.items())
    generator.surnames.sort()

    generator.people = list(generator.people.items())
    generator.people.sort()

    generator._update_context(('surnames','people'))
    generator.save_cache()

def generate_surnames(generator,write):
    try:
        surname_template = generator.get_template('surname')
    except:
        return

    for surname, articles in generator.surnames:
        articles.sort(key=attrgetter('date'), reverse=True)
        dates = [article for article in generator.dates if article in articles]
        write(surname.save_as, surname_template, generator.context, surname=surname,
              articles=articles, dates=dates,
              paginated={'articles': articles, 'dates': dates},
              page_name=surname.page_name, all_articles=generator.articles)

def generate_people(generator,write):

    try:
        person_template = generator.get_template('person')
    except:
        return

    for person, articles in generator.people:
        articles.sort(key=attrgetter('date'), reverse=True)
        dates = [article for article in generator.dates if article in articles]
        write(person.save_as, person_template, generator.context, person=person,
              articles=articles, dates=dates,
              paginated={'articles': articles, 'dates': dates},
              page_name=person.page_name, all_articles=generator.articles)
        
def generate_output(generator, writer):
    write = partial(writer.write_file,
                    relative_urls=generator.settings['RELATIVE_URLS'])

    # Generate surname pages
    generate_surnames(generator,write)
    # Generate person pages
    generate_people(generator,write)
    


def register():
    signals.article_generator_finalized.connect(generate_context)
    signals.article_writer_finalized.connect(generate_output)
