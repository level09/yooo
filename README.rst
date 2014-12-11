URL Shortener Service Based on Project Enferno
==============================================

This is a production ready URL shortener App based on Project Enferno http://enferno.io

(Flask, Mongodb)

it has a similar API to Google Shortener.

Examples
---------

Shorten a URL

::

    curl http://yooo.link/v1/url  -H 'Content-Type: application/json'  -d '{"longUrl": "http://www.google.com/"}'

::

Expand a URL:

::

    http://yooo.link/v1/url?shortUrl=http://domain.com/867nv
::


You can play with the API on the demo website: http://yooo.link


License
-------

MIT licensed.

