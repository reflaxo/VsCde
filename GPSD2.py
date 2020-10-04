import os
from gps import *
import time
import threading

session = gps(mode=WATCH_ENABLE)
try:
    print("tried")
    while True:
        # Do stuff
        report = session.next()
        print("message:" report)
        # Check report class for 'DEVICE' messages from gpsd.  If
        # we're expecting messages from multiple devices we should
        # inspect the message to determine which device
        # has just become available.  But if we're just listening
	# to a single device, this may do.
        if report['class'] == 'DEVICE':
            # Clean up our current connection.
            session.close()
            # Tell gpsd we're ready to receive messages.
            session = gps(mode=WATCH_ENABLE)
	# Do more stuff
except StopIteration:
    print "GPSD has terminated"