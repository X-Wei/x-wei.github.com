sort_tags
===================================
This plugin adds `tags_sorted_article_length` to the context,
which is a list of tupels (Tag, [Articles]) that is sorted 
by number of Articles first and Tag second.

##Usage:
```
{% for tag, articles in tags_sorted_by_article_length %}
```
##Example tags.html
```
    <section id="tags">
      <div class="panel panel-default">
        <div class="panel-body">
            <h1>Tags for {{ SITENAME }}</h1>
            <div class="panel-group" id="accordion">
                {%- for tag, articles in tags_sorted_by_article_length %}
                <div class="panel panel-default">
                    <div class="panel-heading">
                        <h4 class="panel-title">
                            <a data-toggle="collapse" data-parent="#accordion" href="#collapse-{{tag.slug}}">{{ tag }} <span class="badge pull-right">{{ articles|count }}</span></a>
                        </h4>
                    </div>
                    <div id="collapse-{{tag.slug}}" class="panel-collapse collapse">
                        <div class="panel-body">
                            {% for article in articles %}
                            <p><span class="categories-timestamp"><time datetime="{{ article.date.isoformat() }}">{{ article.locale_date }}</time></span> <a href="{{ SITEURL }}/{{ article.url }}">{{ article.title }}</a></p>
                            {% endfor %}
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
      </div>
    </section>
```

