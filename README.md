# Garage
Remote garage control using a RaspberryPi written mainly in Python.

A web server (server.py) based on Bottle (www.bottlepy.org) runs on the RPi.

A web site (index.html) can be launched to offer two buttons ("Garden Gate", "Car Gate") which interact with the server.
From within the network where the RPi is running, the server can be contacted via "localhost:9000".

A handler (handler.js) handles click events on the buttons and sends requests to the server.
The server handles the respective button click to operate a relay (methods in module relay.py switch GPIO pins).


## INSTALLATION

Copy complete code and folders to any location on your RPi (e.g. "/opt/garage").
The most simple way is to clone via git.

Start the server using:
sudo server.py

To automatically start the server at every RPi boot, create a shell script like:

Script: start_server.sh
cd /opt/garage
sudo server.py

To launch it automatically put the command "start_server.sh" into the file "/etc/rc.local".


Via services like Weaved (www.weaved.com) online access from everywhere can be achieved to operate your gargage doors.

