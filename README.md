# drone_project
Pooper Trooper target tracking module 

Project Goal:
Design a drone with the capability to simulate 
a bird by detecting human heads and dropping raisins on them.
 
My Goal:
 · Set up Infrared camera that can capture images on drone.

 · Create a script that can analyze the image and detect a person.

 · If there’s a person communicate that a raisin must be dropped

 
Camera:
Camera specs and further documentation:
https://www.sparkfun.com/products/13233
 
Set up Guide:
https://learn.sparkfun.com/tutorials/flir-lepton-hookup-guide
 
raspberrypi_capture:
The program provided with the Flir Lepton (Longwave infrared camera) 
and captures an image in pgm format.
 
blob_detect.py:
Scikit-Image, provides free image processing algorithms. Blob detection 
checks an image for blobs (bright on dark). The program can’t read pgm 
files so we had to use ImageMagick to convert the images to tiff files 
that can be read in by blob detection.
 
To Download ImageMagick: 
https://www.theurbanpenguin.com/image-manipulation-on-the-raspberry-pi-using-imagemagick/
 
To Download SciKit-Image follow “Step 3: Installing Python Packages”: 
http://www.instructables.com/id/Raspberry-Pi-Based-Document-Scanner-With-Automatic/
 
testprint.py:
The script I wrote to capture an image, run blob detection, and return 
blob coordinates. This script needs to be integrated with navigation part 
of the project, as coordinates provided will help guide drone to target until 
it’s within reach to release raisin and hit target. 