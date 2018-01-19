#!/usr/bin/env/ python

# Import Tornado modules
import os
from tornado import web, ioloop, websocket
from tornado.options import define, options

# Import RPi.GPIO module
import RPi.GPIO as gpio

# Gpio pin initialize
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(12, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)
gpio.setup(16, gpio.OUT)

# Set OUTPUT False as default
gpio.output(12, False)
gpio.output(11, False)
gpio.output(13, False)
gpio.output(15, False)
gpio.output(16, False)

# Vacuum cleaner power state (default: off)
onoff = False

# Websocket server ip & port settings
define("ip", default="192.168.43.37")
define("port", default=8888)

# Web page rendering
class Cmd(web.RequestHandler):
    def get(self):
        self.render("index.html")

# Websocket server event handler
class Socket(websocket.WebSocketHandler):
    def open(self):
        print ' [x] connected.'

    def on_close(self):
        print ' [x] disconnected.'

    def on_message(self, cmd):
        global onoff
        print ' [x] send message. ---->  ' + cmd
    
        # Set gpio OUTPUT to control vacuum cleaner with cmd message from client
        if cmd == 'go' or cmd =='g':
            gpio.output(12, False)
            gpio.output(11, True)
            gpio.output(13, False)
            gpio.output(15, True)
        elif cmd == 'stop' or cmd =='s':
            gpio.output(12, False)
            gpio.output(11, False)
            gpio.output(13, False)
            gpio.output(15, False)
        elif cmd == 'back' or cmd =='b':
            gpio.output(12, True)
            gpio.output(11, False)
            gpio.output(13, True)
            gpio.output(15, False)
        elif cmd == 'right' or cmd =='r':
            gpio.output(12, False)
            gpio.output(11, True)
            gpio.output(13, True)                                                                                                                                                  
            gpio.output(15, False)                                                                                                                                               
        elif cmd == 'left' or cmd =='l':                                                                                                                                            
            gpio.output(12, True)
            gpio.output(11, False)
            gpio.output(13, False)
            gpio.output(15, True)
        elif cmd == 'ftog':
            if onoff == False:
                gpio.output(16, True)
                onoff = True
            else:
                gpio.output(16, False)
                onoff = False                
        else:
            gpio.output(12, False)
            gpio.output(11, False)
            gpio.output(13, False)
            gpio.output(15, False)

settings = dict(
    debug=True,
    autoreload=True,
    compiled_template_cache=False,
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    template_path=os.path.join(os.path.dirname(__file__), "templates")
)

class Application(web.Application):
    def __init__(self):
        handlers = [
            (r"/", Cmd),
            (r"/socket", Socket)
        ]
        web.Application.__init__(self, handlers, **settings)

def main():
    options.parse_command_line()
    app = Application()
    app.listen(options.port, options.ip)
    ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
