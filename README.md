MiniLED
=======

A python API to display text/images to small LED badges and signs.  Was created with the [LED Mini Desk Sign](http://www.brightledsigns.com/products/4_x16_LED_Mini_Desk_Sign-12972-0.html) in mind.

Installation
------------

#### From PyPi:

``` bash
pip install MiniLED
```

#### From Source:

``` bash
git clone git://github.com/robertf224/MiniLED.git && cd MiniLED
python setup.py install
```

Usage
-----

To use the sign, simply create a Sign object, passing it the path to the device.

``` python
from MiniLED import Sign
# This will be something like /dev/ttyUSB1 on Linux
sign = Sign('/dev/tty.usbserial')
```

Now we can start sending messages.

``` python
sign.setmessage('Hello World')
```

We can add optional arguments as well.

``` python
# Message slot number (1-8, default is 1)
sign.setmessage('Slots!', slot=8)

# Message effect ('hold', 'scroll', 'snow', 'flash', 'hold+flash', default is 'hold')
sign.setmessage('Effects!', effect='hold+flash')

# Message speed (1-5, default is 1)
sign.setmessage('Speed!', speed=5)
```

Coming Soon
-----------

Automatic device discovery, images, two-line text.

