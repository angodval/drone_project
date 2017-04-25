import subprocess
import os

#Runs raspberrypi capture (takes the picture)
subprocess.call(['./raspberrypi_capture/raspberrypi_capture', ''])
#Converts outputed pgm file into jpg file
subprocess.call(['convert', 'test.pgm', 'test.jpg'])
#Takes converted jpg image and runs the blob detection alogrithm 
subprocess.call(['python', 'blob_detect.py'])
