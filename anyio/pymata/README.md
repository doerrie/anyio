This is an Arduino Firmata + PyMata replacement for anyio.
Firmata is a firmware and serial protocol much like anyio with a lot of extra features.
It has support for reading and writing analog pins, I2C commands, real-time information, and provides callback routines.
I wanted a library that would work with "Adventures in Minecraft" while allowing children to graduate to using advanced GPIO features.
The pymata/GPIO.py file is extremely simple and I believe that kids will be able to use other PyMata commands as well.

The Firmata firmware comes with the Arduino IDE.

To build the firmware:
* Download the Arduino IDE.
* Update your libraries
* open File -> Examples -> Firmata ->  FirmataStandardPlus
* Compile and Upload to your ProMicro, or other Arduino.

To setup the software:
* Install the latest python 2.7, be sure to choose to python on the system path.
* Install and Update pip
* run the command 'pip install PyMata'
* change the base GPIO.py file to redirect to 'pymata', if it is not already.
* anyio will now use your PyMata to communicate to your Firmata firmware.
