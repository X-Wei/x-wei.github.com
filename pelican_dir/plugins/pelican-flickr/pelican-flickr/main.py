from pelican import signals
import tempfile
import os
import flickrapi
import logging
from .generator import FlickrGenerator
from .cache import FlickrCache

logger = logging.getLogger(__name__)

def register():
  signals.initialized.connect(init_flickr)
  signals.get_generators.connect(add_generator)
  signals.page_generator_context.connect(add_context)

def add_generator(generators):
  return FlickrGenerator

def add_context(generator, metadata):
  generator.context.update(FLICKR_CACHE.export())

def init_flickr(sender):

  # Load mandatory settings
  settings = {
    'FLICKR_API_KEY' : {
      'mandatory' : True,
    },
    'FLICKR_USER' : {
      'mandatory' : True,
    },
    'FLICKR_OUTPUT_DIRNAME' : {
      'mandatory' : False,
      'default' : 'flickr',
    },
    'FLICKR_UPDATE' : {
      'mandatory' : False,
      'default' : True,
    },
    'FLICKR_CACHE' : {
      'mandatory' : False,
      'default' : True,
    },
    'FLICKR_SETS_EXCLUDE' : {
      'mandatory' : False,
      'default' : None,
    },
  }
  for setting, conf in settings.items():
    try:
      val = sender.settings[setting]
    except KeyError:
      if conf['mandatory']:
        raise Exception('Missing %s settings' % setting)
      val = conf['default']
    globals()[setting] = val
    logger.debug('Read setting %s = %s' % (setting, val))

  # Init cache
  cache = FlickrCache()
  cache.build()
  globals()['FLICKR_CACHE'] = cache
