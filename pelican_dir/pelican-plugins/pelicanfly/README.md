Introduction
============
[![Build Status](https://travis-ci.org/bmcorser/pelicanfly.png?branch=master)](https://travis-ci.org/bmcorser/pelicanfly)

This is **pelicanfly**, a plugin for [Pelican](http://docs.getpelican.com/)
that lets you type things like `i ♥ :fa-coffee:` in your
[Markdown](http://daringfireball.net/projects/markdown/) documents and have it
come out as little [Font Awesome](http://fontawesome.io/) icons in the browser.
It provides a minimal extension to Markdown and a plugin for Pelican.

The Pelican plugin hacks in some static assets to make this work with
Pelican "out of the box". If you just want the Markdown extension, it is
available
[separately](http://bmcorser.github.com/fontawesome-markdown/).

Installation
============

It's not hard, just install via pip:

```bash
(env)$ pip install pelicanfly
```

Then add to your Pelican settings, under `PLUGINS` as follows:

```python
PLUGINS = [
    # ...
    'pelicanfly',
    # ...
]
```

If you have followed these steps correctly, next time you build your Pelican
blog, the plugin will do its magic and convert all the `:fa-heart:` style tags
into proper nice little Font Awesome icons. Job done!

FontAwesome updates
===================
I try to keep this repo up to date with FontAwesome, but if it's not, feel free
to submit a PR (the handy `update_fontawesome.sh` script to download will do some
of the lifting to download their assets).
