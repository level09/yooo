URL Shortener Service Based on Project Enferno
==============================================

This is a production ready URL shortener App based on Project Enferno http://enferno.io

(Flask, Mongodb)

it has a similar API to Google Shortener.

Examples
---------

Shorten a URL

::

curl http://domain.com/v1/url  -H 'Content-Type: application/json'  -d '{"longUrl": "http://www.google.com/"}'

::

Expand a URL:

::

    http://domain.com/v1/url?shortUrl=http://domain.com/<code>
::


License
-------

MIT licensed.

