#!/usr/bin/python

import subprocess
import platform

from bottle import route, run, static_file, template, request

system = {0: 'PC', 1: 'RASPBERRY'}

# check for platform
is_raspberry = 'arm' in platform.machine().lower()

if is_raspberry:
    import relay

    # detect camera
    cam = subprocess.check_output('vcgencmd get_camera', shell=True)
    has_camera = int(cam.split()[1][-1])

    if has_camera:
        import picamera
    else:
        import dummy_camera as picamera
else:
    has_camera = 0
    import dummy_relay as relay
    import dummy_camera as picamera

print '\n'
print ' **************************'
print ' Platform: %s' % (system[is_raspberry])
print ' Operating system: %s' % (platform.system())
if not is_raspberry:
    print ' Working with dummy modules for relay and camera'
else:
    if has_camera:
        print ' Camera module attached'
    else:
        print ' No camera module attached'
print ' **************************'
print '\n'

# define gpio ids
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
        relay.pulse(pedestrian, duration=2.5)
    elif id == 'gate':
        relay.pulse(gate, duration=0.1)


# handle mouse click event and get parameter(s)
@route('/cam')
def handle_camera_click():

    if has_camera:
        filename = 'camera.png'
        folder = 'static/'
        camera.capture(folder+filename)
        message = ''
    else:
        message = 'Default image'

    return message


# debug version including automatic reload of server.py
# no server restart necessary after file change
# NOTE: problems when on Pi and camera module loaded
# NOTE: use production setup instead
# run(host='0.0.0.0', port=9000, debug=True, reloader=True)

# production setup
run(host='0.0.0.0', port=9000)
