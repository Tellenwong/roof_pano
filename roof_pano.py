#!/usr/bin/env python
# encoding: utf-8
"""
roof_pano.py

Created by Gene McGill based on code by Chris Waigl.
Modified by Telayna Wong for use with the ACRC camera on the roof of the GI.

This is a working script as is but is intended to be copied to a new file
and modified as needed for other pan-tilt-zoom (PTZ) webcam operations.

This script captures a set of images from the GI roof camera. These
could be input for a panorama.  The method used is pan-tilt-zoom to move
the camera around.

See the AXIS camera manual at:

AXIS Q3708-PVE Network Camera

"""

# URLCAP is the command sent to capture the image.  This may be camera type-specific
URLCAP = 'http://137.229.30.45/axis-cgi/jpg/image.cgi?resolution=1920x1080' # AXIS Q6035-E Mk II Network Camera

# ARCHIVEDIR is where the captured images will be stored.
# Be sure to create that directory and make sure the permissions
# are appropriate.
ARCHIVEDIR = '/products/htdocs/media/cam/acrc_pano/misc'
#ARCHIVEDIR = '/data/acrcweb/public/image/panoramas' ACRC directory to use

import os.path
import urllib
from datetime import datetime
import time

timestamp = datetime.utcnow()
FILEPATTERN = 'roof_pan' + str(timestamp) + '.jpg'
filename = os.path.join(ARCHIVEDIR, FILEPATTERN)
# print filename # uncomment for debug
fullpath, message = urllib.urlretrieve(URLCAP, filename)
#print URLHOME #uncomment for debug