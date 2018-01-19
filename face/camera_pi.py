#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2014, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# Author : sosorry
# Date   : 05/31/2015
# Origin : http://blog.miguelgrinberg.com/post/video-streaming-with-flask

import cv2

class Camera(object):
    def __init__(self):
#	self.cascPath ="haarcascade_frontalface_default.xml"
#	self.faceCascade = cv2.CascadeClassifier(cascPath)

        self.video = cv2.VideoCapture(0)
        #self.video = cv2.VideoCapture(1)
        #self.video.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,  640)
        #self.video.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)
        self.video.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,  320)
        self.video.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 240)
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        #cascPath ="haarcascade_frontalface_default.xml"
        #faceCascade = cv2.CascadeClassifier(cascPath)
	#ret, frame = self.video.read()
    	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    	#faces = faceCascade.detectMultiScale(
       # 	gray,
        #	scaleFactor=1.1,        
        #	minNeighbors=5,
        #	minSize=(30, 30),
        #	flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    	#)

     #   if len(faces)>=1:
    #		print "Found {0} faces!".format(len(faces))

    	# Draw a rectangle around the faces
    #	for (x, y, w, h) in faces:
     #   	cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


        ret, jpeg = cv2.imencode('.jpg', image)
        #return frame
	return jpeg.tostring()
