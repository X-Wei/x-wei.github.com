from __future__ import unicode_literals

from pelican import signals, contents

cjk_range = [
    (u'\u3400', u'\u4DB5'),  # CJK Unified Ideographs Extension A
    (u'\u4E00', u'\u9FA5'),  # CJK Unified Ideographs
    (u'\u9FA6', u'\u9FBB'),  # CJK Unified Ideographs
    (u'\uF900', u'\uFA2D'),  # CJK Compatibility Ideographs
    (u'\uFA30', u'\uFA6A'),  # CJK Compatibility Ideographs
    (u'\uFA70', u'\uFAD9'),  # CJK Compatibility Ideographs
    (u'\U00020000', u'\U0002A6D6'),  # CJK Unified Ideographs Extension B
    (u'\U0002F800', u'\U0002FA1D'),  # CJK Compatibility Supplement
]

punc_range = [
    (u'\u3000', u'\u309f'),
    (u'\u30a0', u'\u30ff'),
    (u'\u31f0', u'\u31ff'),
    (u'\uff00', u'\uffef'),  # Halfwidth and Fullwidth Forms
]


def _with_range(char, check_range):
    for start, end in check_range:
        if char >= start and char <= end:
            return True
    return False


def is_cjk(char):
    return _with_range(char, cjk_range) or _with_range(char, punc_range)


def is_space(char):
    return char in "\r\t\n "


def chinese_auto_spacing(content):
    if content._content is None:
        return

    ret = []
    src = content._content
    cjk_mode = False
    for char in src:
        if cjk_mode:
            if is_space(char):
                continue
            if not is_cjk(char):
                ret.append(" ")
        else:
            if is_cjk(char):
                ret.append(" ")

        cjk_mode = is_cjk(char)
        ret.append(char)
    if len(ret) > 0:
        content._content = "".join(ret)


def register():
    signals.content_object_init.connect(chinese_auto_spacing)
