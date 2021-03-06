#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

DEBUG = True

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.out.write('appengine webapp - hello world!')

def main():
    application = webapp.WSGIApplication([
        ('/', MainPage),
    ], debug=DEBUG)

    run_wsgi_app(application)


if __name__ == '__main__':
    main()
