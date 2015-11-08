#!/usr/bin/python

import platform
from bottle import route, run, static_file, template, request

try:
    import relay
    import picamera
except ImportError:
    print '\n'
    print ' **************************'
    print ' Not on RPi'
    print ' You are on %s' % (platform.uname()[0])
    print ' Working with dummy modules'
    print ' **************************'
    print '\n'
    import dummy_relay as relay
    import dummy_camera as picamera


pedestrian = 23
gate = 24

# initialize relay and pins
pins = [pedestrian, gate]
relay = relay.Relay(pins)

# initialize camera
camera = picamera.PiCamera()
camera.resolution = (499, 443)


# load index.html which is the start page
@route('/')
def index():
    return template('index.html')


# declare that all static files are in the 'current_path/static' folder
# in this case we have styles.css, handler.js, icons, etc. there
@route('/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static/')


# handle mouse click event and get parameter(s)
@route('/door')
def handle_door_click():

    # get id of the clicked <div> element from index.html
    id = request.query['id']

    if id == 'pedestrian':
        message = 'Side gate operating'
        relay.pulse(pedestrian, duration=2.0)
    elif id == 'gate':
        message = 'Car gate operating'
        relay.pulse(gate, duration=0.15)

    # create responseText for XMLHttpRequest
    return message


# handle mouse click event and get parameter(s)
@route('/cam')
def handle_camera_click():

    # get id of the clicked <div> element from index.html
    id = request.query['id']

    if id == 'l-cam':
        message = 'Photo has been taken'
    elif id == 'm-cam':
        message = id + ' was clicked'
    elif id == 'r-cam':
        message = id + ' was clicked'

    filename = 'my_image.png'
    folder = 'static/'
    camera.capture(folder+filename)

    return message


# debug version including automatic reload of server.py
# no server restart necessary after file change
# NOTE: problems when on Pi and camera module loaded
# NOTE: use production setup instead
# run(host='0.0.0.0', port=9000, debug=True, reloader=True)

# production setup
run(host='0.0.0.0', port=9000)
