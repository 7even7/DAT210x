import pandas as pd
from scipy import misc
import os

path = "C:/Data/Projektit/DAT210x/Module4/Datasets/ALOI/32"
samples = []
samplesReshaped = []

for filename in os.listdir(path):
    img = misc.imread(path+"//"+filename)
    print img.shape
    imgReshaped = img.reshape(-1)
    print imgReshaped.shape
    samples.append(img)
    samplesReshaped.append(imgReshaped)
    