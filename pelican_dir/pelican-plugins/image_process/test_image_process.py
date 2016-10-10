# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from PIL import Image, ImageChops
from pelican.tests.support import unittest, get_settings, temporary_folder

from image_process import images, harvest_images, process_images


CUR_DIR = os.path.dirname(__file__)
TEST_IMAGES = [os.path.join(CUR_DIR, 'test_data/pelican-bird.jpg'), os.path.join(CUR_DIR, 'test_data/pelican-bird.png')]

class Pelican(object):
    def __init__(self, settings):
        self.settings = settings

class Instance(object):
    def __init__(self, content, settings):
        self._content = content
        self.settings = settings

class ImageDerivativeTest(unittest.TestCase):
    transforms = {
        'crop': ['crop 10 20 100 200'],
        'flip_horizontal': ['flip_horizontal'],
        'flip_vertical': ['flip_vertical'],
        'grayscale': ['grayscale'],
        'resize': ['resize 200 250'],
        'rotate': ['rotate 20'],
        'scale_in': ['scale_in 200 250 False'],
        'scale_out': ['scale_out 200 250 False'],
        'blur': ['blur'],
        'contour': ['contour'],
        'detail':['detail'],
        'edge_enhance': ['edge_enhance'],
        'edge_enhance_more': ['edge_enhance_more'],
        'emboss': ['emboss'],
        'find_edges': ['find_edges'],
        'smooth': ['smooth'],
        'smooth_more': ['smooth_more'],
        'sharpen': ['sharpen'],
        }

    def test_extraction(self):
        settings = get_settings(IMAGE_PROCESS = self.transforms)
        html = '<img class="test image-process image-process-crop test2" src="/tmp/test.jpg" />'
        c = Instance(html, settings)

        del images[:]
        harvest_images(c)

        expected_content = '<img class="test image-process image-process-crop test2" src="/tmp/derivatives/crop/test.jpg"/>'

        expected_source = os.path.join(settings['PATH'], 'tmp/test.jpg')
        output_path, _ = os.path.split(expected_source)
        base_path = os.path.join(output_path, settings['IMAGE_PROCESS_DIR'], 'crop')
        expected_destination = os.path.join(base_path, 'test.jpg')
        expected_images = [(expected_source, expected_destination, [u'crop 10 20 100 200'])]

        self.assertEqual(c._content, expected_content)
        self.assertEqual(images, expected_images)


    def test_transforms(self):
        settings = get_settings(IMAGE_PROCESS = self.transforms)
        p = Pelican(settings)
        del images[:]
        with temporary_folder() as tmpdir:
            for d in self.transforms:
                for i in TEST_IMAGES:
                    _, name = os.path.split(i)
                    destination = os.path.join(tmpdir, d, name)
                    images.append((i, destination, settings['IMAGE_PROCESS'][d]))
            process_images(p)

            for i in images:
                transformed = Image.open(i[1])

                path, name = os.path.split(i[0])
                expected_path = os.path.join(path, 'results', i[2], name)
                expected = Image.open(expected_path)

                self.assertEqual(ImageChops.difference(transformed, expected).getbbox(), None)

class HTMLGenerationTest(unittest.TestCase):
    """
    Check that all syntaxes generate proper HTML.
    """
    valid_transforms = {
        'thumb': ["crop 0 0 50% 50%", "scale_out 150 150", "crop 0 0 150 150"],
        'article-image': {'type': 'image',
                          'ops': ["scale_in 300 300"],
                          },
        'crisp': {'type': 'responsive-image',
                  'srcset': [('1x', ["scale_in 800 600 True"]),
                             ('2x', ["scale_in 1600 1200 True"]),
                             ('4x', ["scale_in 3200 2400 True"]),
                             ],
                  'default': '1x',
                  },
        'crisp2': {'type': 'responsive-image',
                   'srcset': [('1x', ["scale_in 800 600 True"]),
                              ('2x', ["scale_in 1600 1200 True"]),
                              ('4x', ["scale_in 3200 2400 True"]),
                              ],
                   'default': ["scale_in 400 300 True"],
                   },
        'large-photo': {'type': 'responsive-image',
                        'sizes': '(min-width: 1200px) 800px, (min-width: 992px) 650px, (min-width: 768px) 718px, 100vw',
                        'srcset': [('600w', ["scale_in 600 450 True"]),
                                   ('800w', ["scale_in 800 600 True"]),
                                   ('1600w', ["scale_in 1600 1200 True"]),
                                   ],
                        'default': '800w',
                        },
        'pict': {'type': 'picture',
                 'sources': [{'name': 'default',
                              'media': '(min-width: 640px)',
                              'srcset': [('640w', ["scale_in 640 480 True"]),
                                         ('1024w', ["scale_in 1024 683 True"]),
                                         ('1600w', ["scale_in 1600 1200 True"]),
                                         ],
                              'sizes': '100vw',
                              },
                             {'name': 'source-1',
                              'srcset': [('1x', ["crop 100 100 200 200"]),
                                         ('2x', ["crop 100 100 300 300"]),
                                         ]
                              }
                             ],
                 'default': ('default', '640w'),
                 },
        'pict2': {'type': 'picture',
                  'sources': [{'name': 'default',
                               'media': '(min-width: 640px)',
                               'srcset': [('640w', ["scale_in 640 480 True"]),
                                          ('1024w', ["scale_in 1024 683 True"]),
                                          ('1600w', ["scale_in 1600 1200 True"]),
                                          ],
                               'sizes': '100vw',
                               },
                              {'name': 'source-2',
                               'srcset': [('1x', ["crop 100 100 200 200"]),
                                          ('2x', ["crop 100 100 300 300"]),
                                          ]
                               }
                              ],
                  'default': ('source-2', ["scale_in 800 600 True"]),
                  },
        }

    def test_undefined(self):
        settings = get_settings(IMAGE_PROCESS = self.valid_transforms)
        html = '<img class="image-process-undefined" src="/tmp/test.jpg" />'
        c = Instance(html, settings)
        del images[:]
        with self.assertRaises(RuntimeError):
            harvest_images(c)


    def test_image_generation(self):
        settings = get_settings(IMAGE_PROCESS=self.valid_transforms, IMAGE_PROCESS_DIR='derivs')
        test_data = [
            ('<img class="image-process-thumb" src="/tmp/test.jpg" />',
             '<img class="image-process-thumb" src="/tmp/derivs/thumb/test.jpg"/>',
             ('tmp/test.jpg', 'thumb/test.jpg', ["crop 0 0 50% 50%", "scale_out 150 150", "crop 0 0 150 150"])
             ),
            ('<img class="image-process-article-image" src="/tmp/test.jpg" />',
             '<img class="image-process-article-image" src="/tmp/derivs/article-image/test.jpg"/>',
             ('tmp/test.jpg', 'article-image/test.jpg', ["scale_in 300 300"])
             )
           ]

        for data in test_data:
            expected_source = os.path.join(settings['PATH'], data[2][0])
            output_path, _ = os.path.split(expected_source)
            base_path = os.path.join(output_path, settings['IMAGE_PROCESS_DIR'])
            expected_destination = os.path.join(base_path, data[2][1])

            c = Instance(data[0], settings)

            del images[:]
            harvest_images(c)

            expected_images = [(expected_source, expected_destination, data[2][2])]

            self.assertEqual(c._content, data[1])
            self.assertEqual(images, expected_images)


    def test_responsive_image_generation(self):
        settings = get_settings(IMAGE_PROCESS=self.valid_transforms, IMAGE_PROCESS_DIR='derivs')
        test_data = [
            ('<img class="image-process-crisp" src="/tmp/test.jpg" />',
             '<img class="image-process-crisp" src="/tmp/derivs/crisp/1x/test.jpg" srcset="/tmp/derivs/crisp/1x/test.jpg 1x, /tmp/derivs/crisp/2x/test.jpg 2x, /tmp/derivs/crisp/4x/test.jpg 4x"/>',
             [('tmp/test.jpg', 'crisp/1x/test.jpg', ["scale_in 800 600 True"]),
              ('tmp/test.jpg', 'crisp/2x/test.jpg', ["scale_in 1600 1200 True"]),
              ('tmp/test.jpg', 'crisp/4x/test.jpg', ["scale_in 3200 2400 True"]),
              ]),

            ('<img class="image-process-crisp2" src="/tmp/test.jpg" />',
             '<img class="image-process-crisp2" src="/tmp/derivs/crisp2/default/test.jpg" srcset="/tmp/derivs/crisp2/1x/test.jpg 1x, /tmp/derivs/crisp2/2x/test.jpg 2x, /tmp/derivs/crisp2/4x/test.jpg 4x"/>',
             [('tmp/test.jpg', 'crisp2/1x/test.jpg', ["scale_in 800 600 True"]),
              ('tmp/test.jpg', 'crisp2/2x/test.jpg', ["scale_in 1600 1200 True"]),
              ('tmp/test.jpg', 'crisp2/4x/test.jpg', ["scale_in 3200 2400 True"]),
              ('tmp/test.jpg', 'crisp2/default/test.jpg', ["scale_in 400 300 True"])
              ]),

            ('<img class="image-process-large-photo" src="/tmp/test.jpg" />',
             '<img class="image-process-large-photo" sizes="(min-width: 1200px) 800px, (min-width: 992px) 650px, (min-width: 768px) 718px, 100vw" src="/tmp/derivs/large-photo/800w/test.jpg" srcset="/tmp/derivs/large-photo/600w/test.jpg 600w, /tmp/derivs/large-photo/800w/test.jpg 800w, /tmp/derivs/large-photo/1600w/test.jpg 1600w"/>',
             [('tmp/test.jpg', 'large-photo/600w/test.jpg', ["scale_in 600 450 True"]),
              ('tmp/test.jpg', 'large-photo/800w/test.jpg', ["scale_in 800 600 True"]),
              ('tmp/test.jpg', 'large-photo/1600w/test.jpg', ["scale_in 1600 1200 True"]),
              ]),
           ]

        for data in test_data:
            c = Instance(data[0], settings)

            del images[:]
            harvest_images(c)

            expected_images = list()
            for t in data[2]:
                expected_source = os.path.join(settings['PATH'], t[0])
                output_path, _ = os.path.split(expected_source)
                base_path = os.path.join(output_path, settings['IMAGE_PROCESS_DIR'])
                expected_destination = os.path.join(base_path, t[1])
                expected_images.append((expected_source, expected_destination, t[2]))

            self.maxDiff = None
            self.assertEqual(c._content, data[1])
            for i in images:
                self.assertIn(i, expected_images)
            for i in expected_images:
                self.assertIn(i, images)


    def test_picture_generation(self):
        settings = get_settings(IMAGE_PROCESS=self.valid_transforms, IMAGE_PROCESS_DIR='derivs')
        test_data = [
            ('<picture><source class="source-1" src="/images/pelican-closeup.jpg"></source><img class="image-process-pict" src="/images/pelican.jpg"/></picture>',
             '<picture><source media="(min-width: 640px)" sizes="100vw" srcset="/images/derivs/pict/default/640w/pelican.jpg 640w, /images/derivs/pict/default/1024w/pelican.jpg 1024w, /images/derivs/pict/default/1600w/pelican.jpg 1600w"></source><source srcset="/images/derivs/pict/source-1/1x/pelican-closeup.jpg 1x, /images/derivs/pict/source-1/2x/pelican-closeup.jpg 2x"></source><img class="image-process-pict" src="/images/derivs/pict/default/640w/pelican.jpg"/></picture>',
             [('images/pelican.jpg', 'pict/default/640w/pelican.jpg', ["scale_in 640 480 True"]),
              ('images/pelican.jpg', 'pict/default/1024w/pelican.jpg', ["scale_in 1024 683 True"]),
              ('images/pelican.jpg', 'pict/default/1600w/pelican.jpg', ["scale_in 1600 1200 True"]),
              ('images/pelican-closeup.jpg', 'pict/source-1/1x/pelican-closeup.jpg', ["crop 100 100 200 200"]),
              ('images/pelican-closeup.jpg', 'pict/source-1/2x/pelican-closeup.jpg', ["crop 100 100 300 300"])
              ]),

            ('<div class="figure"><img alt="Pelican" class="image-process-pict2" src="/images/pelican.jpg" /> <p class="caption">A nice pelican</p> <div class="legend"> <img alt="Other view of pelican" class="image-process source-2" src="/images/pelican-closeup.jpg" /> </div> </div>',
             '<div class="figure"><picture><source media="(min-width: 640px)" sizes="100vw" srcset="/images/derivs/pict2/default/640w/pelican.jpg 640w, /images/derivs/pict2/default/1024w/pelican.jpg 1024w, /images/derivs/pict2/default/1600w/pelican.jpg 1600w"></source><source srcset="/images/derivs/pict2/source-2/1x/pelican-closeup.jpg 1x, /images/derivs/pict2/source-2/2x/pelican-closeup.jpg 2x"></source><img alt="Pelican" class="image-process-pict2" src="/images/derivs/pict2/source-2/default/pelican-closeup.jpg"/></picture> <p class="caption">A nice pelican</p> <div class="legend">  </div> </div>',
             [('images/pelican.jpg', 'pict2/default/640w/pelican.jpg', ["scale_in 640 480 True"]),
              ('images/pelican.jpg', 'pict2/default/1024w/pelican.jpg', ["scale_in 1024 683 True"]),
              ('images/pelican.jpg', 'pict2/default/1600w/pelican.jpg', ["scale_in 1600 1200 True"]),
              ('images/pelican-closeup.jpg', 'pict2/source-2/1x/pelican-closeup.jpg', ["crop 100 100 200 200"]),
              ('images/pelican-closeup.jpg', 'pict2/source-2/2x/pelican-closeup.jpg', ["crop 100 100 300 300"]),
              ('images/pelican-closeup.jpg', 'pict2/source-2/default/pelican-closeup.jpg', ["scale_in 800 600 True"])
              ]),
           ]

        for data in test_data:
            c = Instance(data[0], settings)

            del images[:]
            harvest_images(c)

            expected_images = list()
            for t in data[2]:
                expected_source = os.path.join(settings['PATH'], t[0])
                output_path, _ = os.path.split(expected_source)
                base_path = os.path.join(output_path, settings['IMAGE_PROCESS_DIR'])
                expected_destination = os.path.join(base_path, t[1])
                expected_images.append((expected_source, expected_destination, t[2]))

            self.maxDiff = None
            self.assertEqual(c._content, data[1])
            for i in images:
                self.assertIn(i, expected_images)
            for i in expected_images:
                self.assertIn(i, images)


if __name__ == '__main__':
    unittest.main()
