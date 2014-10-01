#!/usr/bin/env python
# Raspberry Pi Photobooth
#
# Controls the Raspberry Pi Camera
# Takes a sequence of pictures and lays them out
# into a 4x6 frame for immediate printing

# To use Raspberry Pi Camera
#  sudo apt-get update
#  sudo apt-get upgrade
#  sudo raspi-config  ==> Select 'camera' and choose enable. Reboot is needed


# 
# To use Python Image Library:
# sudo apt-get install python-dev libjpeg-dev
# sudo pip install -I pillow
#
import PIL.Image as Image
import picamera
import time
import os


num_photos = 2
composite_size = (800, 600)
target_size = (400, 300)
dest_dir = ['/home', 'pi']
start_delay = 5
camera = picamera.PiCamera()
camera.vflip=True

def get_filename(session_name, composite=False):
    '''Returns filename to use for the next image, 
       based on session_name and timestamp'''
    if composite:
        filename =  "%s-Composite-%d.jpg" % (session_name, time.time())
    else:
        filename =  "%s-%d.jpg" % (session_name, time.time())
        
    path = list(dest_dir)
    path.append(filename)
    abs_path = os.path.join(*path)
    return abs_path
    
def start_photoshoot(session_name):
    'Take photos and composite them into a single image'
    images = []
    
    for i in range(0, num_photos):
        abs_file = get_filename(session_name)
        camera.capture(abs_file)
        images.append(abs_file)
        
        if (i == num_photos - 1):
            break
        
        print "WAIT"
        time.sleep(1)
        
    
    # Positioning only works for 2 photos right now    
    comp_img = Image.new(mode='RGBA', size=composite_size)
    if len(images) > 0:
        pos = (0, 0)
        for img in images:
            src_img = Image.open(img)
            src_img.resize(target_size)
            comp_img.paste(src_img, pos)
            pos = (pos[0]+400, pos[1])
        comp_filename = get_filename(session_name, True)
        print "Saving to: %s" % (comp_filename)
        comp_img.save(comp_filename)
    
if __name__ == '__main__':
    session_name = 'TestSession1'
    
    for x in range(0,start_delay):
        print "Starting in", int(start_delay-x)
        time.sleep(1)
        
    start_photoshoot(session_name)
