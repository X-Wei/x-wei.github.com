# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import os

import six

from .conf_factory import ConfFactory


CUR_DIR = os.path.dirname(__file__)

logger = logging.getLogger(__name__)

from pelican import signals


def generate_default(generator):
    """
    The method that will be called by the Pelican plugin mechanism.
    It gets a configuration file to launch the generation with this file.

    :param generator: the Pelican generator
    """
    # Trying to get a panorama.yml file in the Pelican root dir (i.e. the parent of the content dir)
    conf_file = os.path.join(os.path.abspath(os.path.join(generator.settings['PATH'], os.pardir)), 'panorama.yml')
    if not os.path.isfile(conf_file):
        # The file is not file, using the default configuration file instead
        conf_file = os.path.join(CUR_DIR, 'default.yml')
    generate(generator, conf_file)


def generate(generator, conf_file):
    """
    The method that will be called by the Pelican plugin mechanism.

    :param generator: the Pelican generator
    """
    logger.info('Panorama generation started')
    # Initializing the conf factory
    conf_factory = ConfFactory()
    conf_factory.configure(conf_file)
    logger.info('Panorama configured with [%s]' % conf_file)
    # Initializing the data factory
    data_factory = conf_factory.data_factory
    data_factory.parse_data(generator.articles)
    # Initializing the chart factory
    chart_factory = conf_factory.chart_factory
    # Initializing the results
    charts = {}
    # Iterating over the confs to produce data and render the charts
    for conf_id, conf in six.iteritems(conf_factory.confs):
        # noinspection PyBroadException
        try:
            data = data_factory.produce(producer=conf['producer'])
            chart = chart_factory.render(data=data, renderer=conf['renderer'])
            charts[conf_id] = chart
        except Exception as err:
            logger.exception('Error while generating [%s] conf. -> chart not available.' % conf_id)
    # Setting results in the context
    # Charts will be accessible in the Pelican context under this name
    generator.context['panorama_charts'] = charts
    # Generation summary
    nb_chart_generated = len(charts)
    nb_conf = len(conf_factory.confs)
    if nb_chart_generated != nb_conf:
        logger.warn('All charts not generated [%s/%s]' % (nb_chart_generated, nb_conf))
    else:
        logger.info('All charts generated [%s/%s]' % (nb_chart_generated, nb_conf))

    logger.info('Panorama generation ended')


def register():
    """ Called by the Pelican engine to register the plugin.
    It uses a Blinker (https://pypi.python.org/pypi/blinker) and is registered on the event "article_generator_finalized".
    Raised when the generator has ended the generation of its context.
    """
    signals.article_generator_finalized.connect(generate_default)
