
import keras
from keras.optimizers import SGD
from keras import models, layers
from keras.callbacks import TensorBoard
from time import time
from keras.datasets import boston_housing
from sklearn.preprocessing import StandardScaler

(X_train, y_train), (X_test, y_test) = boston_housing.load_data()

print(X_train[0], y_train[0])

scale = StandardScaler()


scale.fit(X_train)


X_train_scaled = scale.transform(X_train)
X_test_scaled = scale.transform(X_test)


print(X_train_scaled[0])

model = models.Sequential()

model.add(layers.Dense(8, activation='sigmoid', input_shape=[X_train.shape[1]]))
model.add(layers.Dense(16, activation='sigmoid'))
model.add(layers.Dense(1))
keras.optimizers.adam(lr=0.5)

model.compile(optimizer=SGD(), loss='mse', metrics=['mae'])


tensorboard = TensorBoard(log_dir="logs/{}".format(time()))

history = model.fit(X_train_scaled, y_train, batch_size=20, validation_split=0.2, epochs=50, callbacks=[tensorboard])

print(model.evaluate(X_test_scaled, y_test))