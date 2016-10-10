#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: 2013 @ bruno@adele.im / bruno.adele.im
#
# use:
# generate_screenshot.py ../pelican-themes

import time
import sys
import os


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


def generate_screenshot(themesroot, theme):
            print ("")

            os.system("cat pelicanconf_default.py > pelicanconf.py")
            os.system("cat confs/%s_pelicanconf.py >> pelicanconf.py" % theme)
            os.system("echo \"THEME = '%s/%s'\" >> pelicanconf.py" % (themesroot, theme))

            print ("generate screenshot for %s" % theme)
            os.system("rm -rf output/*")
            os.system("make html")

            # print("Sleep")
            # time.sleep(20)
            # print("Ready for snap")  
            
            params = '--min-width=1024 --delay=2000 --max-wait=2000 --max-width=1024 --max-height=2048'
            
            os.system("CutyCapt %s --url=http://localhost:8000 --out=content/static/%s_index_tmp.png" % (params, theme))
            os.system("CutyCapt %s --url=http://localhost:8000/details-information-for-%s-theme.html --out=content/static/%s_article_tmp.png" % (params, theme, theme))
            os.system("convert content/static/%s_index_tmp.png -trim content/static/%s_index.png" % (theme, theme)) 
            os.system("convert content/static/%s_article_tmp.png -trim content/static/%s_article.png" % (theme, theme)) 
            os.system("convert content/static/%s_index.png -resize %s -gravity north -crop 410x307 content/static/small_%s_index.png" % (theme, '410x307', theme)) 
            os.system("convert content/static/%s_article.png -resize %s  -gravity north -crop 410x307 content/static/small_%s_article.png" % (theme, '410x307', theme)) 
            os.system("rm content/static/%s_*_tmp.png" % theme)

                     
            #os.popen("CutyCapt --url=file:///LIVE/projects/pelicanthemes-generator/output/index.html --out=content/static/%s_index.png" % theme)

def generate_screenshots(themesroot):
    themes = list_themes(themesroot)
    for theme in themes:
        generate_screenshot(themesroot, theme)

    generate_screenshot(themesroot, 'jesuislibre')


if len(sys.argv) == 2:
    generate_screenshots(sys.argv[1])
