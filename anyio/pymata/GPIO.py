# anyio/pymata/GPIO.py  02/02/2017 M. Scott Doerrie
# Any bugs in this implementation are his responsibility.
#
# Based on:
# anyio/arduino/GPIO.py  21/04/2014  D.J.Whale
#
# A trivial Firmata/pymata based digital GPIO link

# CONFIGURATION ========================================================

from PyMata.pymata import PyMata

DEBUG = False

# TODO: Are these to be referenced by users or can they be deleted?
MIN_PIN = 0
MAX_PIN = 16

IN      = PyMata.INPUT
OUT     = PyMata.OUTPUT
BCM     = 0
BOARD   = 1
HIGH    = PyMata.HIGH
LOW     = PyMata.LOW


# OS INTERFACE =========================================================

from ..arduino import portscan

# STATIC REDIRECTORS ===================================================

# Find out if there is a pre-cached port name.
# If not, try and find a port by using the portscanner

name = portscan.getName()
if name != None:
  if DEBUG:
    print("Using port:" + name)
  PORT = name
else:
  name = portscan.find()
  if name == None:
    raise ValueError("No port selected, giving in")
  PORT = name
  print("Your anyio board has been detected")
  print("Now running your program...")

# Initialize PyMata on the serial port we found
board = PyMata(port_id=PORT,bluetooth=False)

# Each GPIO function has at most one PyMata function.
def setmode(mode):
  # For compatability only.  Do nothing.
  pass

def setup(channel, mode):
  board.set_pin_mode(pin=channel, mode=mode, pin_type=PyMata.DIGITAL)
  pass

def input(channel):
  return board.digital_read(channel)

def output(channel, value):
  board.digital_write(channel, value)
  pass

def cleanup():
  # For compatability only.  Do nothing.
  pass

# END
