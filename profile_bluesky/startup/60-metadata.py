print(__file__)

import datetime
import socket 
import getpass 

# Set up default metadata

HOSTNAME = socket.gethostname() or 'localhost' 
USERNAME = getpass.getuser() or 'synApps_xxx_user' 
RE.md['login_id'] = USERNAME + '@' + HOSTNAME
RE.md['beamline_id'] = 'developer'	# TODO: YOUR_BEAMLINE_HERE
RE.md['proposal_id'] = None
RE.md['pid'] = os.getpid()

#import os
#for key, value in os.environ.items():
#    if key.startswith("EPICS"):
#        RE.md[key] = value
