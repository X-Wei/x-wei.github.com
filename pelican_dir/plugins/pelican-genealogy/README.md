# Pelican genealogy plugin

This plugin is useful for a genealogy blog that wants to track
surnames and people mentioned in each article. The plugin parses
metadata for articles in the form:

```
Surnames: Zappala, Sposato
People: Mariano Zappala, Anna Sposato
```

This metadata is added to a list of people and surnames associated
with the artice. In addition, context is added for a dictionary that
maps each surname and person name to a list of articles where they are
mentioned. Both the metadata and the context can be accessed from
within a theme to provide surname and person pages. Finally, pages are
generated for each surname and each person, following a template from
the theme.

## Configuration

To configure the plugin, use the following:

```
SURNAME_URL = '{slug}'
SURNAME_SAVE_AS = '/surnames/{slug}.html'
PERSON_URL = '{slug}'
PERSON_SAVE_AS = '/people/{slug}.html'
```

## Theme Support

A theme that uses this plugin is available at
[pelican-etna](https://github.com/zappala/pelican-etna).

To see an example of this plugin and a supporting theme, see
[genealogy.zappala.org](http://genealogy.zappala.org).

(The site above is not yet converted to Pelican but is coming soon.)



