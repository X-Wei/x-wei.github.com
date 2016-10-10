#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Template CSV loader
-------------------
Authored by Lucy Park <me@lucypark.kr>, 2015
Released under the BSD 2-Clause License (http://opensource.org/licenses/BSD-2-Clause)
"""

import os
import re

from pelican import signals

def read_txt(filepath, encoding='utf-8'):
    with open(filepath, 'r') as f:
        doc = f.read().decode(encoding)
    return doc

def csv_loader(csv_elem, curpath,\
        linefeed='\n', delim=',', classes=['table'], limit=5):

    if "'''" in csv_elem:
        filename = None
        doc = csv_elem.split("'''")[1]
    else:
        filename = csv_elem.split("'")[1]
        filepath = os.path.join('content', curpath, filename)
        doc = read_txt(filepath)

    if classes:
        csv_string = '<table class="%s">' % ' '.join(classes)
    else:
        csv_string = '<table>'

    if filename:
        csv_list = filter(None, doc.split(linefeed))[:limit]
    else:
        csv_list = filter(None, doc.split(linefeed))

    for i, row in enumerate(csv_list):
        if i==0:
            csv_string += '<tr><th>%s</th></tr>' % '</th><th>'.join(row.split(delim))
        else:
            csv_string += '<tr><td>%s</td></tr>' % '</td><td>'.join(row.split(delim))

    if filename:
        csv_string += '<tr><td colspan="%s" class="data-link"><a href="%s">data link</a></td></tr>' % (len(csv_list[0].split(delim)), filename)
    csv_string += '</table>'

    return csv_string

def loadcsv(data_passed_from_pelican):
    """A function to read through each page and post as it comes through from Pelican, find all instances of triple-backtick (```...```) code blocks, and add an HTML wrapper to each line of each of those code blocks"""

    if data_passed_from_pelican._content: # If the item passed from Pelican has a "content" attribute (i.e., if it's not an image file or something else like that)
    # NOTE: `data_passed_from_pelican.content` seems to be read-only, whereas `data_passed_from_pelican._content` is able to be overwritten. (Mentioned by Jacob Levernier in his Better Code-Block Line Numbering Plugin)
        page_content = data_passed_from_pelican._content
        curpath = os.path.dirname(data_passed_from_pelican.get_relative_source_path())
    else:
        return # Exit the function, essentially passing over the (non-text) file.

    all_csv_elements = re.findall('{% csv .*? %}', page_content, re.DOTALL) # re.DOTALL puts python's regular expression engine ('re') into a mode where a dot ('.') matches absolutely anything, including newline characters.

    if(len(all_csv_elements) > 0):
        updated_page_content = page_content

    for csv_elem in all_csv_elements:
        replacement = csv_loader(csv_elem, curpath)
        updated_page_content = updated_page_content.replace(csv_elem, replacement)

        data_passed_from_pelican._content = updated_page_content

def register():
    signals.content_object_init.connect(loadcsv)
