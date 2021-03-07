#################
### Project 1 ###
#################

### basic scale ###

import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# homes = pd.read_csv('out.csv')
homes = pd.read_csv('homes.csv')
print(homes)
type(homes[['prices']])

homes[['prices_scale']] = homes[['prices']]/100000 # prices
homes[['sqft_scale']] = homes[['sqft']]/1000 # prices

x = homes.drop(["prices_scale","prices","sqft"],axis = 1)
y = homes.prices_scale
x.shape

x_1 = np.array(homes['prices_scale'], dtype=float)
x_2 = np.array(homes['sqft_scale'], dtype=float)
x_3 = np.array(homes['sqft_scale'], dtype=float)


print(y)
#print(combined_x)
# exercise 1 bedrooms, baths, SF & price -- pick your own location

model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')
history = model.fit(x_1, y, epochs=500)

p1 = model.predict(x_1)
print(p1)

model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')
history = model.fit(x_1, y, epochs=500)

p2 = model.predict(x_2)
print(p2)

p = pd.DataFrame(p)
homes[['predict']] = p*100000
#homes[['diff']] = homes['predict']*100000 - homes['prices']

print(homes[['predict']])
print(p)

plt.plot(history.history['loss'], label='loss')
plt.ylim([0, 500])
plt.xlabel('Epoch')
plt.ylabel('loss')
plt. xlim(-5, 100)
plt. ylim(-1, 50)
plt.legend()
plt.grid(True)
plt.show()

plt.scatter(homes['prices'], homes['predict'])
plt.xlim([0, 1700000])
plt.ylim([0, 2000000])
plt.axline([0, 0], [1, 1])
plt.xlabel('asking price')
plt.ylabel('predictions')
plt.legend()
plt.show()

# MSE
# 1/1000 scale
x_alt = homes['prices']
y_alt = homes['predict']

summation = 0
n = len(y_alt)
for i in range (0,n):
  difference = x_alt[i] - y_alt[i]
  squared_difference = difference**2
  summation = summation + squared_difference

MSE = summation/n
print ("The Mean Squared Error is: " , MSE)

# The Mean Squared Error is:  1517978370517.7815 w/o zip
# The Mean Squared Error is:   798382812584.5723 w/ zip

### standardize & normalize data ###

from sklearn.preprocessing import StandardScaler # mean of 0 and SD of 1
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
# from sklearn.preprocessing import Normalizer

ss = StandardScaler()
mms = MinMaxScaler()
rob = RobustScaler()
# nor = Normalizer()

#homes = pd.read_csv('austin.csv')

homes_tform = ss.fit_transform(homes)
homes_tform.shape

x = homes_tform[:, 1:46]
y = homes_tform[:,0]
x.shape

model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[45])])
model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit(x, y, epochs=500)

p = model.predict(x)
p_tform = np.concatenate([p, x], axis=1)
p_back = ss.inverse_transform(p_tform)

# p_back = pd.DataFrame(p_back)

homes[['predict_back']] = p_back[:,0]
# homes[['diff_back']] = homes['predict_back'] - homes['prices']

# MSE
# 1/1000 scale
prices = homes['prices']
predicted = homes['predict_back']

summation = 0
n = len(predicted)
for i in range (0,n):
  difference = prices[i] - predicted[i]
  squared_difference = difference**2
  summation = summation + squared_difference

MSE = summation/n
print ("The Mean Squared Error is: " , MSE)

# The Mean Squared Error is:  1512080777545.8586 -- standard scaler w/o zip
# The Mean Squared Error is:   788122563382.5979 -- standard scaler w/ zip
# The Mean Squared Error is:  1642034535361.3896 -- min max scaler
# The Mean Squared Error is:  1511846877953.2502 -- robust scaler