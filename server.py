#!/usr/bin/python

from bottle import route, run, static_file, template
import relay


pedestrian = 23
gate = 24

# initialize relay and pins
pins = [pedestrian, gate]
relay = relay.Relay(pins)


# declare that all static files are in the "current_path/static" folder
# in this case we have styles.css, handler.js, icons, etc. there
@route('/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static/')


# load index.html which is the start page
@route('/')
def index():
    return template("index.html")


# handle mouse down request of pedestrian entrance
@route('/mouse_down_pe')
def handle_mouse_down_pe():
    relay.pulse(pedestrian, duration=2.0)


# handle mouse down request of entrance gate
@route('/mouse_down_eg')
def handle_mouse_down_eg():
    relay.pulse(gate, duration=0.15)


# debug version including automatic reload for faster development
# no server restart necessary after file change
# run(host='0.0.0.0', port=9000, debug=True, reloader=True)

# production setup
run(host='0.0.0.0', port=9000)
