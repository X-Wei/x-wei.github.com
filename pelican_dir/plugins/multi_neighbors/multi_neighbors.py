""" Multi-neighbor articles plugin for Pelican.

This plugin adds ``next_articles`` (newer) and ``prev_articles`` (older)
variables to the article's context.
"""

from collections import deque
from pelican import signals


def neighbors(generator):
    # Populate prev_articles.
    prevs = deque([], generator.settings['MULTI_NEIGHBORS'])
    for article in reversed(generator.articles):
        if not hasattr(article, 'prev_articles'):
            article.prev_articles = list()
        if prevs:
            article.prev_articles.extend(prevs)
            if len(prevs) == prevs.maxlen:
                prevs.pop()
        prevs.appendleft(article)

    # Populate next_articles.
    nexts = deque([], generator.settings['MULTI_NEIGHBORS'])
    for article in generator.articles:
        if not hasattr(article, 'next_articles'):
            article.next_articles = list()
        if nexts:
            article.next_articles.extend(nexts)
            if len(nexts) == nexts.maxlen:
                nexts.pop()
        nexts.appendleft(article)


def register():
    signals.article_generator_finalized.connect(neighbors)
