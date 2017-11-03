#-*- coding: utf-8 -*-

import os, os.path
import cherrypy

class NextPage:
       
    def index(self):
        return "otrā lapa!!"
    index.exposed = True

class FrontPage:
    _cp_config = {
        'tools.encode.on':True,
        'tools.encode.encoding':'utf8',
        } 
   
    next=NextPage()
    
    def index(self):
        return '''
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <link href="/static/css/style.css" rel="stylesheet">
            <title>Box configurator</title>
        </head>
        
        <form action="configurator" method="get">
            Box dimensions<br />
            <br />
            Width (mm):  
            <input type="text" name="width" value="" 
                size="15" maxlength="40"/> <br />
            <br />
            
            Length (mm):  
            <input type="text" name="length" value="" 
                size="15" maxlength="40"/> <br />
            <br />
            
            Height (mm):  
            <input type="text" name="height" value="" 
                size="15" maxlength="40"/> <br />
            <br />
            
            <br />
            <button type="submit">SUBMIT</button>
        </form> '''
        
    index.exposed = True
    
    def configurator(self, width, length, height):
        print '\n\n',width,'\n',length,'\n', height,'\n\n'
      
        return '''
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <link href="/static/css/style.css" rel="stylesheet">
            <title>Box configurator</title>
        </head>
        <img src="http://img38.imageshack.us/img38/2576/mv5bmtk5mtuzmdk5m15bml5.jpg" alt="Paldies!" />
        <br />
        Episks paldies.<br />
        <br />
        <a href="./">Atpakaļ uz sākumu</a>
        '''
                
    configurator.exposed = True

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }    

cherrypy.server.socket_host = '0.0.0.0'#'78.84.26.115'    
cherrypy.quickstart(FrontPage(),'/', conf)