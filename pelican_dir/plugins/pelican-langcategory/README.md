pelican-langcategory
====================

Plugin for Pelican to make languages behave the same as categories (visitor can browse articles in certain language)


## Usage

Check out the plugin to your pelican's plugins directory 

Edit your *pelicanconf.py*: 

    PLUGINS = ['pelican-langcategory']
    LANGUAGE_URL = 'lang/{lang}/'
    LANGUAGE_SAVE_AS = 'lang/{lang}/index.html'
    
Later you can visit url like '/lang/en/', '/lang/cn/' to browse your articles just like categories.
