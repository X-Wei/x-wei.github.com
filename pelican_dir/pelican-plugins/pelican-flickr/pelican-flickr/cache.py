# codinf=utf-8
import flickrapi
import logging
import main
from .models import *

logger = logging.getLogger(__name__)

class FlickrCache:
  api = None

  # Flickr data
  sets = []
  photos = []

  # Exclusions
  sets_exclude = None

  # Cached sets (just ids)
  sets_cached = None

  def __init__(self):

    # Init flickr api
    self.api = flickrapi.FlickrAPI(main.FLICKR_API_KEY)

    # Setup includes / excludes
    self.sets_exclude = main.FLICKR_SETS_EXCLUDE

    # Setup cached sets ids
    self.sets_cached = FlickrCached('photosets')
    self.sets_cached.fetch()

  def load_photosets(self):
    '''
    Load photosets from cache or from flickr
    '''
    self.sets = []
    try:
      # Update authorized ?
      if not main.FLICKR_UPDATE:
        raise Exception('No flickr update authorized from settings.')

      # Try loading from Flickr
      logger.debug("Fetching Flickr photosets online...")
      sets = self.api.photosets_getList(user_id=main.FLICKR_USER)
      for photoset in sets.find('photosets').findall('photoset'):
        s = FlickrPhotoset(xml=photoset)
        if self.sets_exclude and (s.id in self.sets_exclude or s.title in self.sets_exclude):
          logger.info(u"Excludes %s" % (s,))
          continue
        logger.info(u"Use %s from %s" % (s, s.cached and 'cache' or 'flickr'))

        # Load photos from each new photoset
        s.load_photos(self.api)

        # Save photoset
        s.save()
        self.sets.append(s)

      # Save photosets id (with order)
      self.sets_cached.data = [s.id for s in self.sets]
      self.sets_cached.save()
    except Exception, e:
      logger.warning("Failed to load photosets from Flickr: %s" % (str(e),))

      # Just use sets from cache
      for s in self.sets_cached.data or []:
        ps = FlickrPhotoset(id=s)
        ps.load_photos(self.api)
        self.sets.append(ps)

    return len(self.sets) > 0

  def build(self):
    '''
    Build cache using data from flickr api
    '''
    if not self.load_photosets():
      logger.error("No photosets found for Flickr")
      return

  def export(self):
    '''
    Export cache in templates context
    '''
    return {
      'flickr_sets' : self.sets,
    }


