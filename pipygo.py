import os, os.path
import random
import string

from classes.car import Car

import cherrypy

class PiPyGo(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')

class PiPyGoWebService(object):
    exposed = True
    my_car = Car()

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        #return cherrypy.session['mystring']
        return my_car.get_steering_direction()

    def POST(self, steering_directon):
        cherrypy.session['steering_directon'] = steering_direction
        return ""

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/command': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    webapp = PiPyGo()
    webapp.generator = PiPyGoWebService()
    cherrypy.quickstart(webapp, '/', conf)
