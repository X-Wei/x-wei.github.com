# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from functools import partial
import os
import io
import logging

from pandas.util.testing import assert_series_equal
from pelican.generators import (ArticlesGenerator)
from pelican.tests.support import unittest, get_settings
from jinja2 import Environment, PackageLoader
from pandas import Series

from panorama import panorama
from panorama.chart_factory import ChartFactory
from panorama.conf_factory import ConfFactory
from panorama.data_factory import count_article_by_column_by_year, count_article_by_column, count_article_by_year, \
    top_article

logger = logging.getLogger(__name__)

CUR_DIR = os.path.dirname(__file__)

TEST_DATA = os.path.join(CUR_DIR, 'test_data')
CONTENT_DIR = os.path.join(TEST_DATA, 'content')
TEST_DIR = os.path.join(CUR_DIR, 'test_output')
TEST_PAGE_TEMPLATE = 'test_page.html'
CONF_DIR = os.path.join(TEST_DATA, 'conf')

TEST_DATA_FILE = os.path.join(TEST_DATA, 'p/article_data.p')

CONF_FILE = os.path.join(CONF_DIR, 'panorama.yml')
CONF_ERR_FILE = os.path.join(CONF_DIR, 'panorama_error.yml')


def create_generator():
    settings = get_settings(filenames={})
    settings['CACHE_CONTENT'] = False  # cache not needed for this logic tests
    return ArticlesGenerator(context=settings.copy(), settings=settings,
                             path=CONTENT_DIR, theme=settings['THEME'], output_path=None)

class TestGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = create_generator()

    def test_generate_default(self):
        # Registering plugin
        panorama.register()
        # Generating data from file
        self.generator.generate_context()

    def test_generate(self):
        # Generating data from file
        self.generator.generate_context()
        panorama.generate(generator=self.generator, conf_file=CONF_FILE)

    def tearDown(self):
        # preparing template rendering for test page generation
        pl = PackageLoader('tests', 'template')
        jinja2_env = Environment(lstrip_blocks=True, trim_blocks=True, loader=pl)
        self.template_test_page = jinja2_env.get_template(TEST_PAGE_TEMPLATE)
        with io.open(os.path.join(TEST_DIR, 'all_charts.html'), 'w', encoding='utf8') as output_file:
            output_file.write(self.template_test_page.render(panorama_charts=self.generator.context['panorama_charts']))


class TestData(unittest.TestCase):
    def setUp(self):
        generator = create_generator()
        generator.generate_context()
        conf_factory = ConfFactory()
        conf_factory.configure(CONF_FILE)
        self.data_factory = conf_factory.data_factory
        self.data_factory.parse_data(generator.articles)

    def test_count_article_by_column_by_year(self):
        self.assertEqual(len(count_article_by_column_by_year(self.data_factory.data, 'genre')), 5)

    def test_count_article_by_column(self):
        expected_result = Series({'BD': 4, 'Divers': 1, 'Jeunesse': 1, 'Roman': 3, 'Roman Noir': 1})
        assert_series_equal(count_article_by_column(self.data_factory.data, 'genre'), expected_result)

    def test_count_article_by_year(self):
        expected_result = Series({2007: 1, 2008: 2, 2010: 1, 2014: 7})
        assert_series_equal(count_article_by_year(self.data_factory.data), expected_result)

    def test_top_article(self):
        expected_result = Series({'Gallimard': 3})
        assert_series_equal(top_article(self.data_factory.data, 'publisher', 1), expected_result)


class TestChart(unittest.TestCase):
    def setUp(self):
        self.chart_factory = ChartFactory()

    def test_render(self):
        expected_chart_name = 'test_chart'
        renderer = partial(self.chart_factory.get_renderer(class_name='discreteBarChart'), name=expected_chart_name)
        data = Series({'BD': 4, 'Divers': 1, 'Jeunesse': 1, 'Roman': 3, 'Roman Noir': 1})
        chart = self.chart_factory.render(data=data, renderer=renderer)
        self.assertEqual(chart.name, expected_chart_name)
        self.assertIsNotNone(chart.htmlcontent)
        self.assertIsNotNone(chart.container)


class TestConf(unittest.TestCase):
    def setUp(self):
        self.conf_factory = ConfFactory()

    def test_load_conf(self):
        # top_article_error shall be in the configuration since the error is only detected at runtime
        expected_result = ['nb_article_by_genre_year', 'top_article_by_writer', 'nb_article_by_ranking',
                           'nb_article_by_ranking_year', 'nb_article_by_genre', 'nb_article_by_year',
                           'top_article_error']
        self.conf_factory.configure(CONF_FILE)
        self.assertEqual(set(self.conf_factory.confs.keys()), set(expected_result))

    def test_chart_configuration(self):
        self.conf_factory.configure(CONF_FILE)
        self.chart_factory = self.conf_factory.chart_factory
        data = Series({'BD': 4, 'Divers': 1, 'Jeunesse': 1, 'Roman': 3, 'Roman Noir': 1})
        # Testing a default value
        renderer = partial(self.chart_factory.get_renderer(class_name='pieChart'), name='pie_chart')
        chart = self.chart_factory.render(data=data, renderer=renderer)
        self.assertEquals(chart.width, '700')
        # Testing a value overriden
        renderer = partial(self.chart_factory.get_renderer(class_name='discreteBarChart'), name='bar_chart')
        chart = self.chart_factory.render(data=data, renderer=renderer)
        self.assertEquals(chart.width, '500')

    def test_load_bad_conf(self):
        expected_result = ['nb_article_by_error']
        self.conf_factory.configure(CONF_ERR_FILE)
        self.assertEqual(set(self.conf_factory.confs.keys()), set(expected_result))