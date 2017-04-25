from skimage import io, color
from skimage.filters.rank import median
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.morphology import disk
from matplotlib import pyplot as plt

#Reads in image and runs it through a gray layer to help filter
img = io.imread('test.jpg')
img_gray = color.rgb2gray(img)
img_filtered = median(img_gray)
coords = []

#intializing and creating the plot that will print at the end to show blob detection results
plt.figure()
plt.imshow(img_filtered, cmap='gray')
plt.title('Filtered Image')

blobs = blob_doh(img_filtered)

#creates circles around all the blobs found
for blob in blobs:
    y, x, r = blob
    c = plt.Circle((x, y), r, color='red', linewidth=2, fill=False)
    plt.gca().add_patch(c)
    coords += [[x,y]]

#return coordinates and shows the final blob detection run
print coords
plt.show()


