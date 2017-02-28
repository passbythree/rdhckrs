"""
This is an example for image reading
"""

import h5py
import matplotlib.pyplot as plt

read_path = '/media/blade/road_hackers/training_images/137.h5'

image_object = h5py.File(read_path, 'r')

for utc_time in image_object:  # utc_time is a string
    print(utc_time)

# get an image from 137.h5 dictionary
selected_image = image_object[utc_time]

# print information of selected_image dataset
print(selected_image)

# access to one pixel
print(selected_image[100][100])

print(len(image_object))

# display selected image
plt.imshow(selected_image)
plt.show()

image_object.close()
