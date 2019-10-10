#!/usr/bin/env python
# encoding: utf-8
"""
webcam_pano_template.py

Created by Gene McGill based on code by Chris Waigl.
Modified by Telayna Gordon for use with the ACRC camera on the roof of the GI.

This is a working script as is but is intended to be copied to a new file
and modified as needed for other pan-tilt-zoom (PTZ) webcam operations.

This script captures a set of images from the GI roof camera. These
could be input for a panorama.  The method used is pan-tilt-zoom to move
the camera around.

See the AXIS camera manual at:

Q6035-E: http://classic.www.axis.com/files/manuals/um_q6035e_46632_en_1206.pdf

"""

# DEGREES are the degree values to pan too.  Some trial and error will help you narrow
# down the degree or degrees you need.
DEGREES = [ -140.0, -85.0, -30.0, 25.0 ]

# URLCAP is the command sent to capture the image.  This may be camera type-specific
URLCAP = 'http://137.229.30.45/axis-cgi/jpg/image.cgi?resolution=1920x1080' # AXIS Q6035-E Mk II Network Camera

# In the case of panorama it is quite likely the focus should be on infinity.  This
# command adjusts the focus to infinity.
URLFOCUS = 'http://137.229.30.45/axis-cgi/com/ptz.cgi?focus=9999'

# Always move to HOME when finished!
URLHOME = 'http://137.229.30.45/axis-cgi/com/ptz.cgi?move=home'

# URLTILT defines the tilt up or down in degrees.  Trial and error will
# help you decide what is right for your need.
URLTILT = 'http://137.229.30.45/axis-cgi/com/ptz.cgi?tilt=-5'

# URLZOOMOUT defines the zoom in / out value.
URLZOOMOUT = 'http://137.229.30.45/axis-cgi/com/ptz.cgi?zoom=1'

# ARCHIVEDIR is where the captured images will be stored.
# Be sure to create that directory and make sure the permissions
# are appropriate.
ARCHIVEDIR = '/products/htdocs/media/cam/acrc_pano/misc'
#ARCHIVEDIR = '/data/acrcweb/public/image/panoramas' ACRC directory to use

import os.path
import urllib
from datetime import datetime
import time

def main():
	start=0
	for i in DEGREES:
			# print "Loop %d" % (i) # uncomment for debug
			# print URLTILT # uncomment for debug
			urllib.urlretrieve(URLTILT)
			URLPAN = 'http://137.229.30.45/axis-cgi/com/ptz.cgi?pan=' + str(i)
			# print URLPAN # uncomment for debug
			urllib.urlretrieve(URLPAN)
			time.sleep(15)
			#put in a time delay to prevent blurry pictures from camera moving too fast.
			urllib.urlretrieve(URLZOOMOUT)
			# print URLZOOMOUT # uncomment for debug
			urllib.urlretrieve(URLFOCUS)
			timestamp = datetime.utcnow()
			FILEPATTERN = 'roof_pan' + str(i) + '.jpg'
			filename = os.path.join(ARCHIVEDIR, FILEPATTERN)
			# print filename # uncomment for debug
			fullpath, message = urllib.urlretrieve(URLCAP, filename)
			#print URLHOME #uncomment for debug
			#urllib.request.urlretrieve(URLHOME)

if __name__ == '__main__':
	main()
