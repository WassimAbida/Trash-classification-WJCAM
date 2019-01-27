from skimage.io import imsave
from download import download
import numpy as np
import os


url = "https://www.dropbox.com/s/uzwczfzg80tfy8u/images.npy?dl=0"
path = download(url, './images.npy', replace=True)

data = np.load(path)
if not os.path.exists(os.path.join("data", "images")):
    os.makedirs(os.path.join("data", "images"))

for i in range(len(data)):
    imsave(os.path.join("data", "images", str(i) + ".png"), data[i])
    os.rename(os.path.join("data", "images", str(i) + ".png"), os.path.join("data", "images", str(i)))

os.remove('./images.npy')
