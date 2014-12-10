# coding: utf-8

from flask import Flask, request, abort, Response, redirect, url_for, flash, Blueprint
from flask.templating import render_template
from flask_security.decorators import roles_required, login_required
import  json, short_url
from models import Link
bp_public = Blueprint('public',__name__, static_folder='../static')

@bp_public.route('/')
def index():
    return Response('{"API": {"status":"ok","version":"1.0"}}', content_type ='application/json')

@bp_public.route('/v1/url',methods=['GET','POST'])
def process():
    shortUrl = request.args.get('shortUrl','')
    if shortUrl:
        return expand(shortUrl)
    longUrl = request.get_json()['longUrl']
    if longUrl:
        return shorten(longUrl)
    else:
        return Response('{"error": {"code":400,"message":"API Error"}}',content_type='application/json')


def shorten(longUrl):
    try:
        link = Link.objects.get(longUrl=longUrl)
        return Response('{"id":"%s","longUrl":"%s"}' % (request.host_url + link.shortUrl,link.longUrl),content_type='application/json')
    except Exception, e:
        #first save it to get the id
        link = Link(longUrl=longUrl)
        link.save()
        link.shortUrl = short_url.encode_url(link.lid)
        link.save()
        shortUrl =  request.host + link.shortUrl
        return Response('{"id":"%s","longUrl":"%s"}' % (shortUrl,longUrl),content_type='application/json',status=200)

def expand(shortUrl):
    key = short_url.decode_url(shortUrl.split('/')[-1])
    try:
        link = Link.objects.get(lid=key)
        return Response('{"id":"%s","longUrl":"%s","status":"ok"}' % (shortUrl,link.longUrl),content_type='application/json')
    except Exception:
        return Response('{"error": {"code":400,"message":"API Error"}}',content_type='application/json')

@bp_public.route('/<shortUrl>')
def redir(shortUrl=None):
    try:
        key = short_url.decode_url(shortUrl)
        link = Link.objects.get(lid = key)
        link.usage += 1
        link.save()
        print link.longUrl
        return redirect(link.longUrl,301)
    except Exception:
        return Response('{"error": {"code":400,"message":"Key Error"}}',content_type='application/json')
