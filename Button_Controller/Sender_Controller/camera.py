#import picamera
import os
import time

def makePhotos(count = 1):
    """camera = picamera.PiCamera()

    camera.resolution=(2592,1944)
    camera.led = False
    camera.exposure_mode = 'auto'
    camera.color_effects = (128,128)"""
    dirName = str(time.ctime())
    """os.mkdir("Photos/" + dirName)
    i = 0
    while i < count:
        fileName = "Photos/" + dirName + "/" + str(i+1) + ".jpg"
        camera.capture(fileName)
        time.sleep(2)
        i += 1
        
    camera.close()"""
    return dirName