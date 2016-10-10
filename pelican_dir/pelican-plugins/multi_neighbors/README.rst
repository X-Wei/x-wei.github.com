Multi Neighbors Plugin for Pelican
==================================

This plugin adds ``next_articles`` (a sequence of newer articles) and
``prev_articles`` (a sequence of older articles) variables to the article's
context.


Usage
-----

To install this plugin, see `How to use plugins
<http://docs.getpelican.com/en/latest/plugins.html>`__ from the Pelican
documentation.

In ``pelicanconf.py``, configure the maximum number of articles to list. For
example:

.. code-block::

    MULTI_NEIGHBORS = 5

Output the variables in your article template:

.. code-block:: html+jinja

    {% if article.prev_articles %}
        <nav class="older">
            <h1>Previous articles</h1>
            <ul>
                {% for article in article.prev_articles %}
                    <li>
                        <a href="{{ SITEURL }}/{{ article.url }}">
                            {{ article.title }}
                        </a>
                    </li>
                {% endfor %}
            </ul>
        </nav>
    {% endif %}
    {% if article.next_articles %}
        <nav class="newer">
            <h1>Next articles</h1>
            <ul>
                {% for article in article.next_articles %}
                    <li>
                        <a href="{{ SITEURL }}/{{ article.url }}">
                            {{ article.title }}
                        </a>
                    </li>
                {% endfor %}
            </ul>
        </nav>
    {% endif %}
