blog
====

My static HTML blog - using [Pelican](http://blog.getpelican.com/)

* Create a virtualenv and activate it
* `pip install -r requirements`
* `cd src/`
* Generate the site: `pelican content` (or `pelican /path/to/your/content/ [-s path/to/your/settings.py]`)
* Start a server: `cd output && python -m pelican.server`, the go to `http://localhost:8000/` to see the result



* To generate a single file: `pelican --write-selected output/posts/my-post-title.html`
* To watch modifications, run pelican with the `-r` (`--autoreload`) option

## Deploy

* `pelican content -s publishconf.py`
* `rsync -avc --delete output/ host.example.com:/var/www/your-site/`
