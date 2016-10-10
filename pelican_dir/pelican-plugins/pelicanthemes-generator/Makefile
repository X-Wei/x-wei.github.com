PY=python
PELICAN=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py
PORT=8000

# Pelican
html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

confs:
	./generate_pelicanconfs.py ../pelican-themes

articles:
	./generate_articles.py ../pelican-themes

screenshots:
	./generate_screenshots.py ../pelican-themes

themes: 
	./generate_pelicanconfs.py ../pelican-themes
	./generate_articles.py ../pelican-themes
	./generate_screenshots.py ../pelican-themes

serve:
	cd $(OUTPUTDIR) && $(PY) -m SimpleHTTPServer $(PORT)

push:
	git push github master

upload:
	rsync -ar --delete output/ pelicanthemes.jesuislibre@10.0.0.6:/home/pelicanthemes.jesuislibre/public_html/
	@echo "Done..."
