import json
import os
import tempfile
import main

class FlickrCached(object):
  '''
  Helper methods to cache objects
  '''
  id = None
  cache_path = ''
  data = {}
  cached = True

  # Template generation
  slug = ''
  url = ''
  generated_path = ''

  def __init__(self, cache_id):
    self.id = cache_id

    # Setup cache dir
    cache_dir = os.path.join(tempfile.gettempdir(), 'pelican_flickr')
    if main.FLICKR_CACHE and not os.path.isdir(cache_dir):
      os.mkdir(cache_dir)

    # Setup final cache path for object
    self.cache_path = os.path.join(cache_dir, '%s.json' % self.id)

  def fetch(self):
    '''
    Get a data set from cache
    '''
    if not main.FLICKR_CACHE:
      return False

    if not os.path.exists(self.cache_path):
      return False
    with open(self.cache_path, 'r') as f:
      self.data = json.loads(f.read())

    # Check data
    if not self.data:
      raise Exception('No data from %s' % self.cache_path)
    return True

  def save(self):
    '''
    Save a serializable data set in local cache
    '''
    if not main.FLICKR_CACHE:
      return False

    with open(self.cache_path, 'w') as f:
      f.write(json.dumps(self.data))
    return True

  def build_paths(self, parts):
    # Build path, url, and slug for a cache object
    self.slug = '/'.join(parts)
    self.generated_path = '%s/%s.html' % (main.FLICKR_OUTPUT_DIRNAME, self.slug)
    self.url = '/' + self.generated_path

