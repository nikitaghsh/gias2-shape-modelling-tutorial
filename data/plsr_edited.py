import numpy as np
import pandas as pd
# import matplotlib.pyplot  as _plt

import os
from sklearn.cross_decomposition import PLSRegression
from sklearn.metrics import mean_squared_error
from sklearn import model_selection
from subprocess import call



X = pd.read_csv('train_ant.csv',header=None)
Y = pd.read_csv('train_wts.csv',header=None)
test_set = pd.read_csv('anthro_test.csv',header=None)
pls2 = PLSRegression(scale=True)
model = pls2.fit(X,Y)
pred_training = pls2.predict (X)
pred_testing = pls2.predict(test_set)

print(pred_testing)

np.savetxt("PCA_wts.csv",pred_testing, delimiter=",")
