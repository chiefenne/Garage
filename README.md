# Garage
Remote garage control using a RaspberryPi written mainly in Python.

A web server (server.py) based on Bottle (www.bottlepy.org) runs on the RPi.

A web site (index.html) can be launched to offer two buttons ("Side Gate", "Car Gate") which interact with the server.
From within the network where the RPi is running, the server can be contacted via "localhost:9000".

A handler (handler.js) handles click events on the buttons and sends requests to the server.
The server handles the respective button click to operate a relay (methods in module relay.py are switching GPIO pins).


#### Installation

Copy complete code and folders to any location on your RPi (e.g. "/opt/garage").
The most simple way is to clone via git.

```
git clone http://github.com/chiefenne/Garage
```

Starting the server:

```
sudo python server.py
```

To automatically start the server at every RPi boot, create a shell script start_server.sh containing:

```
cd /opt/garage
sudo python server.py
```

To launch it automatically put the following lines into the file "/etc/rc.local":

```
# start garage webserver
if [ -e /opt/garage/start_server.sh ]; then
sudo /opt/garage/start_server.sh
fi
```


Via services like Weaved (www.weaved.com) online access from everywhere can be achieved to operate your garage doors.


#### Code modification

In order to be able to develop and run the code on a platform other than the RPi (because of the missing RPi.GPIO module) dummy modules for the relay (dummy_relay.py) and the camera (dummy_camera.py) have been introduced.
This function needs to have exactly the same methods as relay.py (at least those which are used in server.py).
The code in server.py automatically checks for the platform and imports the respective module.

