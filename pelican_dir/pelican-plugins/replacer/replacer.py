# -*- coding: utf-8 -*-
import pelican


def init(pelican_object):
    # I have no good idea. Pass settings to replace function.
    global replaces
    replaces = pelican_object.settings.get('REPLACES', ())


def replace(path, context):
    with open(path, 'r') as f:
        s = f.read()
        for src, tgt in replaces:
            s = s.decode('utf-8').replace(src.decode('utf-8'), tgt.decode('utf-8'))

    with open(path, 'w') as f:
        f.write(s.encode('utf-8'))


def register():
    pelican.signals.initialized.connect(init)
    pelican.signals.content_written.connect(replace)
