# -*- coding: utf-8 -*-
# Copyright (c) 2014 Kura
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import unicode_literals
import json
import logging
from operator import itemgetter

try:
    # 2
    from urllib2 import urlopen
    from urllib2 import HTTPError
except ImportError:
    # 3
    from urllib.request import urlopen
    from urllib.request import HTTPError


from pelican import signals


logger = logging.getLogger(__name__)
GITHUB_API = "https://api.github.com/users/{0}/repos"


class GithubProjects(object):

    def __init__(self, gen):
        self.content = None
        self.gen = gen
        github_url = GITHUB_API.format(self.gen.settings['GITHUB_USER'])
        try:
            f = urlopen(github_url)
            # 3 vs 2 makes us have to do nasty stuff to get encoding without
            # being 3 or 2 specific. So... Yeah.
            encoding = f.headers['content-type'].split('charset=')[-1]
            c = f.read().decode(encoding)
        except HTTPError:
            logger.warning("unable to open {0}".format(github_url))
            return
        self.content =  json.loads(c)

    def process(self):
        if self.content is None:
            return []
        projects = []
        for repo in self.content:
            if repo['private']:
                continue
            r = {
                'name': repo['name'], 'language': repo['language'],
                'description': repo['description'], 'github_url': repo['html_url'],
                'homepage': repo['homepage']
            }
            projects.append(r)
        return sorted(projects, key=itemgetter('name'))


def initialize(gen):
    if not 'GITHUB_USER' in gen.settings.keys():
        logger.warning('GITHUB_USER not set')
    else:
        gen.plugin_instance = GithubProjects(gen)

def fetch(gen, metadata):
    gen.context['github_projects'] = gen.plugin_instance.process()


def register():
    signals.article_generator_init.connect(initialize)
    signals.article_generator_context.connect(fetch)
