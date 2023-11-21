import tensorflow as tf
import pandas as pd
import numpy as np

data = pd.read_csv('BP_d.csv', delimiter=';')

data_use = data[["datum", "d_ta", "d_tx", "d_tn"]]

data_use_train = data_use.drop(columns='datum')

x_train = data_use_train.iloc[1:, :]

x = x_train.to_numpy()

model = tf.keras.models.load_model("second_test_modell.h5")


HIST = 10
x_predict = (np.array([x[i:i+HIST] for i in range(len(x)-HIST)])-8)/40

predictions = model.predict(x_predict)
predictions_print = (predictions*40)+8

predictions_df = pd.DataFrame(predictions_print, columns=["da_t", "d_tx", "d_tn"])
predictions_df.to_csv("predictions.csv", sep=";", index=False)



