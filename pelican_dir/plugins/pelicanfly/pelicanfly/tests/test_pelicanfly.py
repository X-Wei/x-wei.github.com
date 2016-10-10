# -*- coding: utf-8 -*-
import os
from shutil import rmtree
from tempfile import mkdtemp
import unittest

from pelican import Pelican
from pelican.settings import read_settings
from pelican.tests.support import mute

from fontawesome_markdown import FontAwesomeExtension
import pelicanfly

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.abspath(os.path.join(CURRENT_DIR, 'output'))

INPUT_PATH = os.path.join(CURRENT_DIR, "content")

class TestPelicanfly(unittest.TestCase):

    def setUp(self):
        self.temp_path = mkdtemp(prefix='pelicanfly.')
        pelicanfly_path, _ = os.path.join(os.path.split(pelicanfly.__file__))
        self.pelicanfly_static = os.path.join(pelicanfly_path, 'static')
        self.settings = read_settings(path=None,
                                      override={
                                          'PATH': INPUT_PATH,
                                          'OUTPUT_PATH': self.temp_path,
                                          'PLUGINS': [pelicanfly]})
        self.pelican = Pelican(self.settings)
        mute(True)(self.pelican.run)()
        pass

    def tearDown(self):
        rmtree(self.temp_path)
        pass

    def test_add_markdown_plugin(self):
        added = any([isinstance(x,FontAwesomeExtension)
            for x in self.pelican.settings['MD_EXTENSIONS']])
        self.assertTrue(added)

    def test_add_static_paths(self):
        theme = self.pelican.settings['THEME_STATIC_PATHS']
        self.assertTrue(self.pelicanfly_static in theme)

    def test_markdown_plugin(self):
        sample_output = open(os.path.join(self.temp_path, 'pages', 'a-sample-page.html'), 'r')
        self.assertTrue('<i class="fa fa-bug"></i>' in sample_output.read())

    def test_assets_exist(self):
        for static_dir in ['css', 'fonts']:
            static_path = os.path.join(self.pelicanfly_static, static_dir)
            for static_file in os.listdir(static_path):
                in_theme = os.path.join(self.temp_path, 'theme',
                                        static_dir, static_file)
                self.assertTrue(os.path.exists(in_theme))
