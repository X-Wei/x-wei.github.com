#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: 2013 @ bruno@adele.im / bruno.adele.im
#
# use:
# generate_pelicanconf.py ../pelican-themes

import sys
import os

from jinja2 import Environment, FileSystemLoader, meta


def list_themes(themesroot):
    ignore = [
        'dev-random', 'dev-random2', 'html5-dopetrope', 'irfan',
        'nmnlist', 'pelican-bootstrap3', 'storm', 'syte',
    ]
    dirlist = []

    allfiles = os.listdir(themesroot)
    for dirname in allfiles:
        if dirname not in ignore:
            if os.path.isdir('%s/%s/templates' % (themesroot, dirname)):
                dirlist.append(dirname)

    return sorted(dirlist)


# get all variable in template file
def get_variables(themesroot, themename, tplname):
    ignore = [
        'AUTHOR', 'SITENAME', 'DISQUS_SITENAME', 'DEFAULT_LANG',
        'DEFAULT_PAGINATION', 'FEED_ALL_ATOM', 'FEED_ALL_RSS',
        'FEED_DOMAIN', 
    ]

    tpldir = "%s/%s/templates" % (themesroot, themename)
    env = Environment(loader=FileSystemLoader(tpldir))
    template_source = env.loader.get_source(env, tplname)[0]
    parsed_content = env.parse(template_source)

    variables = []
    undeclared = meta.find_undeclared_variables(parsed_content)
    for item in undeclared:
        if item not in ignore:
            variables.append(item)

    return sorted(variables)


def get_all_tpl_vars(themesroot, themename):
    # Get all vars from templates files
    all_vars = set()

    tpldir = "%s/%s/templates" % (themesroot, themename)
    files = os.listdir(tpldir)
    for fname in files:
        variables = get_variables(themesroot, themename, fname)
        for var in variables:
            if var.isupper():
                all_vars.add(var)

    return sorted(all_vars)


def writetext(filename, text):
    f = open(filename, "w")
    f.writelines(text)
    f.close()


def themeconf(themesroot, themename):
    """
    themeconf <themename> <libconf>
    ex:
      themeconf jesuislibre /dir/officialblogsrc/pelicanconf.py
    """
    all_vars = get_all_tpl_vars(themesroot, themename)

    pconf = '%s/%s/pelicanconf_sample.py' % (themesroot, themename)
    if os.path.exists(pconf):
        sys.path.append(os.path.abspath(os.path.dirname(pconf)))
        m = __import__(os.path.basename(pconf.replace('.py', '')))
    else:
        m = str  # tips, empty __dict__, todo, change this tips

    # TODO found a solution for out the UTF8
    # text = "#!/usr/bin/env python\n# -*- coding: utf-8 -*- #\nfrom __future__ import unicode_literals\n\n"

    # Show pelicanconf.py vars content
    text = ""
    for var in all_vars:
        if var in m.__dict__:
            text += "%s = %s\n" % (var, repr(m.__dict__[var]))
        else:
            text += "# %s =\n" % var

    writetext('./confs/%s_pelicanconf.py' % themename, text)


def generateconfs(themesroot):
    themes = list_themes(themesroot)

    for theme in themes:
        print ("generate conf for %s theme" % theme)
        themeconf(themesroot, theme)


if len(sys.argv) == 2:
    generateconfs(sys.argv[1])
