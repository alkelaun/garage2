
# **Garage Door opener With Raspberry Pi, Django, and a Relay**

## Purpose:
Open or close my garage door by clicking on a website.

![full archictecture](https://github.com/alkelaun/garage2/blob/master/raspberrypi/garagedoor.jpg)

## Architecture:
Three smaller projects are intertwined in this project.
1. Open the garage door by clicking on a website.
2. Proxy the video stream through the same website. (And same credentials)
3. Sense the state of the garage door through a sensor and Zigbee.

### Garage Door Opener
#### Requirements
1. Open garage door via a website button.
2. User must be authenticated.

#### Design
1. Use Django for website display and authentication.
2. Use a Raspberry Pi to control a relay wired to the button near the house.
3. Use a python script/CherryPy server to control the raspberry pi. `garage.py`
(This is how the django site interacts with the raspberry pi. It's definitely insecure.)


