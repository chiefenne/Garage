# Garage
Remote garage control using a RaspberryPi. Relay control, etc. in Python.

A web server based on Bottle (bottlepy.org) runs on the RPi.
Copy complete code and folders for instance to "/opt/garage" and create a shell script that changes to this folder and runs server.py.
Launch this script from /etc/rc.local to automatically start the server at every RPi boot.

A web site (index.html) can be launched to offer two buttons ("Garden Gate", "Car Gate").
From within the network where the RPi is running, the server can be contacted via "localhost:9000".

A handler (handler.js) handles click events on the buttons and sends an information (parameter "id" in GET request) to the server.
The server handles the respective button click to operate a relay (methods in module relay.py which operate on GPIO pins).

Via services like Weaved (www.weaved.com) online access from everywhere can be achieved.
