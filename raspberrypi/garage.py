import cherrypy
import RPi.GPIO as GPIO
from time import gmtime, strftime, localtime, sleep
import os

# Simple Logger
def log(type="none"):
	c = type
	d = strftime("%Y-%m-%d %H:%M:%S", localtime())
	f = open("logfile", "a+")
	f.write("%s - %s\r\n" % (c,d))
	f.close()

def pushdoor():
        #setup  
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	GPIO.setup(7,GPIO.OUT, initial=GPIO.LOW)
	#Door Timing (Not sure why it starts at 0 to set relay on)
	GPIO.output(7 , 0)
	sleep(1)
	GPIO.output(7 , 1)
	# Cleanup
	GPIO.cleanup()

# @cherrypy creates a url
# Should be refactored as a RESTful service
class GarageDoor(object):

	@cherrypy.expose
	def index(self):
		log("test")	
		return "Controller is Up\n"

	@cherrypy.expose
	def trigger(self):
		pushdoor()
		log("door triggered")
		return "Garage Door Triggered \n"


if __name__ == '__main__':
	cherrypy.config.update({'server.socket_host': '0.0.0.0'} )      
	cherrypy.quickstart(GarageDoor())
