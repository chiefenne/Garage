#!/usr/bin/python

import platform
from bottle import route, run, static_file, template, request


try:
    import relay
except ImportError:
    # raise ImportError('<any message you want here>')
    print '\n\nNot on RPi'
    print 'You are on %s' % (platform.uname()[0])
    print 'Working with dummy relay\n\n'
    import dummy_relay as relay


pedestrian = 23
gate = 24

# initialize relay and pins
pins = [pedestrian, gate]
relay = relay.Relay(pins)


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
@route('/click')
def handle_click():

    # get id of the clicked <div> element from index.html
    id_clicked = request.query['id']

    if id_clicked == 'pedestrian':
        print 'pedestrian clicked'
        relay.pulse(pedestrian, duration=2.0)
    elif id_clicked == 'gate':
        print 'gate clicked'
        relay.pulse(gate, duration=0.15)


# debug version including automatic reload for faster development
# no server restart necessary after file change
# run(host='0.0.0.0', port=9000, debug=True, reloader=True)

# production setup
run(host='0.0.0.0', port=9000)
