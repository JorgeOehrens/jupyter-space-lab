import pandas as ppd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

file= '' #Ingresar data de gaia
dt= pd.read_csv(file)

#Conversion

dt['ra_rad']= np.deg2rad(dt['ra'])
dt['dec_rad']= np.deg2rad(dt['dec'])



