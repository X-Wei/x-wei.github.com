# codinf=utf-8
from pelican.utils import slugify
from .cached import FlickrCached
import main
import logging

logger = logging.getLogger(__name__)

class FlickrPhotoset(FlickrCached):
  '''
  Represents & Cache a Flickr Photoset
  '''
  primary = None
  photos = []

  def __init__(self, xml=None, id=None):
    if xml is not None:
      # Load from Flickr xml
      flickr_data = xml.attrib
      super(FlickrPhotoset, self).__init__(flickr_data['id'])

      if not self.check_cache(flickr_data):
        # Update from online data
        self.cached = False
        self.data = flickr_data
        self.data['title'] = xml.find('title').text
        self.data['description'] = xml.find('description').text

    elif id is not None:
      # Load from cache
      super(FlickrPhotoset, self).__init__(id)
      self.fetch()
    else:
      raise Exception('Specify xml source or photoset id.')

    # Always update paths
    self.build_paths((slugify(self.title), ))

  def __unicode__(self):
    return u"Flickr Photoset %s '%s'" % (self.id, self.title)

  def __getattr__(self, name):
    return self.data.get(name, None)

  def __getitem__(self, name):
    return self.data.get(name, None)

  def load_photos(self, api):
    '''
    Load all photos from this photoset
    '''
    self.photos = []
    try:
      # Update authorized ?
      if not main.FLICKR_UPDATE:
        raise Exception('No flickr update authorized from settings.')

      photos = api.photosets_getPhotos(photoset_id=self.id, media='photos')
      xml_photos = photos.find('photoset').findall('photo')
    except:
      xml_photos = self.data['photos']

    for i, xml in enumerate(xml_photos):
      photo_id = type(xml) == unicode and xml or xml.attrib['id']
      try:
        photo = FlickrPhoto(photo_id, api, self)
      except Exception, e:
        logger.error('%d/%d Failed loading of %s : %s', i+1, len(xml_photos), photo_id, str(e))
        continue
      logger.debug(u'%d/%d %s from %s' % (i+1, len(xml_photos), photo, photo.cached and 'cache' or 'flickr'))

      # Save photo
      self.photos.append(photo)
      if not photo.cached:
        photo.save()

      # Check primary
      if self.data['primary'] == photo.id:
        self.primary = photo

    self.data['photos'] = [p.id for p in self.photos]

  def check_cache(self, data):
    # Check the cached data are up to date
    if not self.fetch():
      return False
    return data['date_update'] == self.data['date_update']

class FlickrPhoto(FlickrCached):
  api = None
  photoset = None

  def __init__(self, id, api, photoset):
    self.api = api
    self.photoset = photoset
    super(FlickrPhoto, self).__init__(id)
    self.fetch()

    # Update authorized ?
    if main.FLICKR_UPDATE:
      self.load_from_flickr()

    # Check data
    if not self.data:
      raise Exception('No data available')

    # Always update paths
    self.build_paths((self.photoset.slug, self.id, ))

  def load_from_flickr(self):
    # Load data from flickr
    try:
      infos = self.load_infos()
      if not self.data or infos['dates']['lastupdate'] != self.data['infos']['dates']['lastupdate']:
        self.cached = False
        self.data = {
          'infos' : infos,
          'sizes' : self.load_sizes(),
        }
    except Exception, e:
      logger.error(str(e))

  def __unicode__(self):
    return u"Flickr Photo %s '%s'" % (self.id, 'infos' in self.data and self.data['infos']['title'] or '-')

  def __getattr__(self, name):
    return self.__getitem__(name)

  def __getitem__(self, name):
    if name in self.data.get('infos', {}):
      return self.data['infos'][name]
    return self.data.get(name, None)

  def load_infos(self):
    '''
    Load base infos for a photo
    '''
    xml = self.api.photos_getInfo(photo_id=self.id)
    xml = xml.find('photo')
    out = xml.attrib
    out['title'] = xml.find('title').text
    out['description'] = xml.find('description').text
    out['dates'] = xml.find('dates').attrib

    # Load urls
    out['urls'] = {}
    for url_xml in xml.find('urls').findall('url'):
      out['urls'][url_xml.attrib['type']] = url_xml.text

    # Load tags
    out['tags'] = []
    for tag_xml in xml.find('tags').findall('tag'):
      tag = tag_xml.attrib
      tag['tag'] = tag_xml.text
      out['tags'].append(tag)

    return out

  def load_sizes(self):
    '''
    Fetch sizes, indexed per name
    '''
    out = {}
    sizes = self.api.photos_getSizes(photo_id=self.id)
    for xml in sizes.find('sizes').findall('size'):
      size = xml.attrib
      slug = slugify(size['label'], ((' ', ''),))
      out[slug] = size
    return out

