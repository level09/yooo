URL Shortener Service Based on Project Enferno
==============================================

This is a production ready URL shortener App based on Project Enferno http://enferno.io

(Flask, Mongodb)

it has a similar API to Google Shortener.

This API can be deployed within 3 minutes using this ansible script: 

https://github.com/level09/yooo-ansible

You can also check out this tutorial: 

https://medium.com/@level09/introducing-yooo-a-url-shortener-api-based-on-enferno-framework-823bdc2afa05



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

