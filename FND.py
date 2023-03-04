import pandas as pd # data manipulation and analysis
import numpy as np # python lib for working with arrays, linear algebra
import seaborn as sns # data exploration and visualisation
import matplotlib.pyplot as plt # data visulisation and graphical charting
from sklearn.model_selection import train_test_split # create 2 subsets of the data (training and testing)
from sklearn.metrics import accuracy_score # accuracy of correctly classified among all samples.
from sklearn.metrics import classification_report # generating a human-readable text report
import re # determine if a given text fits the given regular expression 
import string 

data_fake = pd.read_csv('Datasets/Fake.csv')
data_true = pd.read_csv('Datasets/True.csv')

