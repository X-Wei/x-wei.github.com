pelican-jinja2content
=====================

This [Pelican](https://github.com/getpelican/pelican) plugin uses the [Jinja2](https://github.com/mitsuhiko/jinja2) template engine used by Pelican to render the content of articles.
This allows the use of Jinja2 template code in articles, and thus provides access to for example the extremely useful `include` or `import` statements of Jinja2 from within articles.

Installation
------------

Copy the `jinja2content` directory to the `plugins` directory of your Pelican project (or whatever directory you specified for plugins in Pelican's `PLUGIN_PATHS` setting) and add
`'jinja2content'` to the list of plugins (Pelican setting `PLUGINS`) of your project.

Usage
-----

Simply use Jinja2 template code in your articles. If you want to use custom template files for Jinja2's `include` or `import`, place them into the `templates` folder of your theme.

Known Issues
------------

* As [Markdown](https://github.com/waylan/Python-Markdown)'s [`attr_list` extension](https://pythonhosted.org/Markdown/extensions/attr_list.html) in 
[`extra`](https://pythonhosted.org/Markdown/extensions/extra.html) uses `{: ...}` to specify additional HTML attributes for the content to be rendered by Markdown, but also allows for plain `{ ... }` 
notation, this might conflict with eventual Jinja2 template code you supply in your articles. An easy fix is to remove the `attr_list` extension for Pelican's `MD_EXTENSIONS` settings variable (remove 
`'extra'` and add all extensions in `extra` manually except from `attr_list`).

Warranty
--------

No warranty whatsoever is provided for this code. Use only at your own risk!
