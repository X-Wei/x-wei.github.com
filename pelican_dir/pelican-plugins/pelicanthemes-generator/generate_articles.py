#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: 2013 @ bruno@adele.im / bruno.adele.im
#
# use:
# generate_articles.py ../pelican-themes

import sys
import os

from jinja2 import Environment, FileSystemLoader, meta


# Search all template files
def list_themes(themesroot):
    ignore = [
        'dev-random', 'dev-random2', 'html5-dopetrope', 'irfan',
        'nmnlist', 'pelican-bootstrap3', 'storm', 'syte',
        'bold', 'bootlex', 'bootstrap', 'built-texts', 'elegant',
        'gum', 'lannisport', 'pure', 'tuxlite_tbs',
    ]
    dirlist = []

    allfiles = os.listdir(themesroot)
    for dirname in allfiles:
        dirname = dirname.lower()
        if dirname not in ignore:
            if os.path.isdir('%s/%s/templates' % (themesroot, dirname)):
                dirlist.append(dirname)

    return sorted(dirlist)


# get all variable in template file
def get_variables(filename):
    env = Environment(loader=FileSystemLoader('templates'))
    template_source = env.loader.get_source(env, filename)[0]
    parsed_content = env.parse(template_source)

    return meta.find_undeclared_variables(parsed_content)


# Generate all themes article
def generate_themes_article(themesroot):

    themes = list_themes(themesroot)
    os.system("rm content/*")
    for theme in themes:
        print ("generate article for %s" % theme)
        article = ""

        # extract gitlog
        gitlog = os.popen("cd %s ; " % themesroot
                          + "git log --date=short --format='%ad~%s' " +
                          theme +
                          " | tail -n10"
        )
        logs = []
        for line in gitlog.readlines():
            logline = line.split("~")
            logs.append(logline)

        # Title and tags
        title = "Details information for %s theme" % theme
        article += "%s\n" % title
        article += "%s\n" % ("#" * len(title))
        article += ":date: %s\n" % logs[0][0]
        article += ":tags: pelican-themes, %s\n" % theme
        article += ":summary: The last update for this theme is **%s** and they have **%s** modifications\n" % (logs[0][0], len(logs))
        article += "\n"

        # Preview
        article += "**Theme preview**\n\n"
        article += ".. image:: /static/small_%s_index.png\n" % theme
        # article += "   :width: 40%\n"
        article += "   :target: /static/%s_index.png\n\n" % theme

        article += ".. image:: /static/small_%s_article.png\n" % theme
        # article += "   :width: 40%\n"
        article += "   :target: /static/%s_article.png\n\n" % theme

        # Summary logs
        article += "**Last logs**\n\n"
        article += "this themes they have %s modifications\n\n" % len(logs)
        article += ".. sourcecode:: plaintext\n\n"
        for log in logs:
            article += "   %s - %s" % (log[0], log[1])

        article += "\n"
        # Text
        article += "**lipsum**\n\n"
        article += "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras aliquam lacus arcu, eu facilisis sem blandit ac. Suspendisse nec lacinia nunc, eu vestibulum nulla. Curabitur quis sollicitudin neque. Cras iaculis venenatis nibh sit amet tincidunt. Etiam non purus eu dolor posuere vestibulum vel ac eros. Nulla luctus ligula id massa mattis, quis vestibulum libero pellentesque. Quisque viverra lobortis elit at aliquet. Morbi vestibulum ac justo dignissim ornare. Ut vulputate orci in sodales sagittis. Aenean iaculis ut est at feugiat.\n\n"

        article += " Proin sit amet mi quam. Aliquam nec ipsum ac arcu sagittis pellentesque. Integer ac eleifend lectus. Nunc ullamcorper orci eu libero cursus, vitae vestibulum justo elementum. Aenean at commodo turpis, sit amet aliquet ipsum. Aenean risus lorem, ultrices id ipsum eget, molestie fermentum est. Nam imperdiet lectus eleifend urna eleifend, et vestibulum velit vulputate. In hac habitasse platea dictumst.\n\n"

        article += "Vivamus iaculis sagittis posuere. Nulla massa arcu, commodo et vestibulum sit amet, aliquet ac felis. Nunc tempus elementum purus vitae vulputate. Praesent convallis ante erat, ac auctor erat euismod ut. Donec non mauris vitae est aliquam fermentum. Nulla interdum, turpis vel accumsan ultricies, augue tellus scelerisque mi, vel interdum felis erat vel diam. Quisque venenatis erat quis justo fermentum, sed venenatis turpis bibendum. Quisque malesuada nisl eu est vulputate ultrices. Praesent porttitor enim lacinia tempus rutrum.\n\n"

        try:
            # This will create a new file or **overwrite an existing file**.
            f = open("content/%s.rst" % theme, "w")
            try:
                f.writelines(article)
            finally:
                f.close()
        except IOError:
            pass


# Generate index themes summary
def generate_summary_preview(themesroot):
    themes = list_themes(themesroot)

    title = "All preview themes"
    article = ""
    article += "%s\n" % title
    article += "%s\n" % ("#" * len(title))
    article += ":date: 2099-01-01\n"
    article += ":tags: pelican-themes\n"
    article += ":summary: Preview of %s themes\n\n" % (len(themes))

    for theme in themes:
        title = "preview theme for  %s" % theme
        article += "%s\n" % title
        article += "%s\n\n" % ("=" * len(title))
        article += ".. image:: /static/small_%s_index.png\n" % theme
        # article += "   :width: 40%\n"
        article += "   :target: /details-information-for-%s-theme.html\n\n" % theme

        article += ".. image:: /static/small_%s_article.png\n" % theme
        # article += "   :width: 40%\n"
        article += "   :target: /details-information-for-%s-theme.html\n\n" % theme
        article += "\n\n\n\n"
    try:
        # This will create a new file or **overwrite an existing file**.
        f = open("content/pelicanthemes-index-preview.rst", "w")
        try:
            f.writelines(article)
        finally:
            f.close()
    except IOError:
        pass


if len(sys.argv) == 2:
    generate_themes_article(sys.argv[1])
    generate_summary_preview(sys.argv[1])
