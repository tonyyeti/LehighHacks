from __future__ import division
from cvxopt import solvers, matrix
import matplotlib.pyplot as plt
from TickerDataMiner1 import DataSource
from radar import *
import numpy as np

#from __future__ import division
import json
import time
import requests
import pandas as pd
import numpy as np

'''
import os
try:
    from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

except ImportError:
  from http.server import SimpleHTTPRequestHandler as Handler
  from http.server import HTTPServer as Server


class MyTCPHandler(Server.BaseRequestHandler):
    def handle (self):
        #self.data=self.request.body.input1
        data = self.request.recv(1024).strip()
        #print self.client_address, "sent", data
        
#self.request.sendall(self.data.upper())

# Read port selected by the cloud for our application
PORT = int(os.getenv('PORT', 9000))
# Change current directory to avoid exposure of control files
os.chdir('static')

httpd = Server(("", PORT), Handler)
try:
  print("Start serving at port %i" % PORT)
  httpd.serve_forever()
except KeyboardInterrupt:
  pass
httpd.server_close()
'''

from MVO import calculation
import os
try:
    from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
    from SocketServer import TCPServer as Server
except ImportError:
    from http.server import SimpleHTTPRequestHandler as Handler
    from http.server import HTTPServer as Server

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
import cgi


PORT_NUMBER = 9000

#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		if self.path=="/":
			self.path="./static/index.html"
        
		try:
			#Check the file extension required and
			#set the right mime type
            
                
			sendReply = False
			if self.path.endswith(".html"):
				mimetype='text/html'
				sendReply = True
			if self.path.endswith(".jpg"):
				mimetype='image/jpg'
				sendReply = True
			if self.path.endswith(".gif"):
				mimetype='image/gif'
				sendReply = True
			if self.path.endswith(".js"):
				mimetype='application/javascripts'
				sendReply = True
			if self.path.endswith(".css"):
				mimetype='text/css'
				sendReply = True
                        if self.path.endswith(".jpeg"):
                                mimetype='image/jpeg'
                                sendReply=True
                        if self.path.endswith(".png"):
                                mimetype='image/png'
                                sendReply=True
			if sendReply == True:
				#Open the static file requested and send it
				f = open(curdir + sep + self.path)
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
			return
        
		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)
    
	#Handler for the POST requests
	def do_POST(self):
		if self.path=="/send":
                        self.path1="./static/part1.txt"
                        self.path2="./static/part2.txt"
			form = cgi.FieldStorage(
                                    fp=self.rfile,
                                    headers=self.headers,
                                    environ={'REQUEST_METHOD':'POST',
                                    'CONTENT_TYPE':self.headers['Content-Type'],
                                    })
                                    
                                    
                        print ("Your name is:  "+  form["Gender"].value +" " + " "+ form["Age"].value + "  "+form["InvestMentHorizon"].value+"  ")#+form["Industry"].value)
                        Parameter=[form["Gender"].value,form["Age"].value,form["Education"].value,form["InvestMentHorizon"].value,form["Industry"].value]
                        print "Parameter is "+ Parameter[0]+"  "+Parameter[1]+"  "+Parameter[2]+"  "+Parameter[3]+"  "+Parameter[4]
                        list_indus=[int(Parameter[4])]
                        
                        '''
                        credentials={ "url": "https://gateway.watsonplatform.net/personality-insights/api","password": "m1BKzhXCHa8A", "username": "c4673874-470b-4c4d-ba77-999f62ae6f88"}
                                    
                        content={"content":"GOP frontrunner wants to discuss his bid for the GOP nomination NOW PLAYING Donald Trump weighs in on meeting with the RNC Republican presidential front-runner Donald Trump claimed Thursday night that his controversial remarks about punishing women who have abortions were taken out of context."  
                        +"The latest furor to surround Trump's campaign began when he told Matthews there should be some form of punishment for women who get abortions if the procedure is outlawed, later adding that what the punishment would be would have to be determined."
                        +"Provide contextual feedback messages for typical user actions with the handful of available and flexible alert messages."}
                        r = requests.post("https://gateway.watsonplatform.net/personality-insights/api/v2/profile", auth=json.dumps(credentials),data=json.dumps(content))
                        print r.text
                        '''
                        back_list,position=calculation(1,1,"KingJames")
                        
                        string2=""
                        for i in range(1,len(back_list)):
                            string2+=back_list[i]+"<br>"
                            string2+=back_list[i]+"<br><br>"
                        f1 = open(curdir + sep + self.path1)
                        f2 = open(curdir + sep + self.path2)
                        self.send_response(200)
                        self.end_headers()
                        self.wfile.write(f1.read())
                        #<iframe src="//giphy.com/embed/BorouzRzoYQWA" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="http://giphy.com/gifs/bulldog-rocking-BorouzRzoYQWA">via GIPHY</a></p>
                        picname1="/radar.svg"
                        picname2="/picname.png"
                        
                        self.wfile.write("<iframe src=\""+picname1+"\" width=\"240\" height=\"170\" frameBorder=\"0\" id=\"svg1\"class=\"giphy-embed\" allowFullScreen></iframe><br>")
                        
                        self.wfile.write("<iframe src=\""+picname2+"\" width=\"240\" height=\"170\" frameBorder=\"0\" id=\"png1\"class=\"giphy-embed\" allowFullScreen></iframe><br>")
                            #self.wfile.write("<span id=\"span1\">"+string1+"</span><br>")
                        self.wfile.write("<span id=\"span2\">"+string2+"</span><br>")
                        
                        self.wfile.write(f2.read())
                        f1.close()
                        f2.close()
                        #self.wfile.write("Parameter is "+ Parameter[0]+"  "+Parameter[1]+"  "+Parameter[2]+"  "+Parameter[3]+"  "+Parameter[4])
			return


try:
    #os.chdir('static')
    PORT = int(os.getenv('PORT', 8000))
	#Create a web server and define the handler to manage the
	#incoming request
    server = HTTPServer(('0.0.0.0', PORT), myHandler)
    print 'Started httpserver on port ' , PORT
	
	#Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()


