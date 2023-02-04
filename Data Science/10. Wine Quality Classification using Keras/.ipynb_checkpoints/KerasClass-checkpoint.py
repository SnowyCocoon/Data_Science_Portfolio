'''
Autor: Dominik Strzałko
Numer Indeksu: 434788
Data: 06/05/2021
Tytuł Zadania: 11. Sieci neuronowe (Keras)
Treść Zadania: Zaimplementuj rozwiązanie wybranego problemu klasyfikacyjnego za pomocą prostej sieci neuronowej stworzonej przy użyciu biblioteki Keras.
Oprócz kodu (.py/.ipynb) proszę również dołączyć plik z danymi uczącymi/testowymi.
'''

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam


from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

import numpy as np
import pandas as pd

wine=pd.read_csv('winequality-red.csv')

y = wine['quality']
x = wine.drop('quality', axis=1)

citricacid = x['fixed acidity'] * x['citric acid']
citric_acidity = pd.DataFrame(citricacid, columns=['citric_accidity'])
density_acidity = x['fixed acidity'] * x['density']
density_acidity = pd.DataFrame(density_acidity, columns=['density_acidity'])

x = wine.join(citric_acidity).join(density_acidity)

bins = (2, 5, 8)
labels = ['bad', 'nice']
y = pd.cut(y, bins = bins, labels = labels)

enc = LabelEncoder()
yenc = enc.fit_transform(y)

scale = StandardScaler()
scaled_x = scale.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(scaled_x,yenc , test_size=0.2,train_size=0.8, random_state=21)

NeuralModel = Sequential([
                        Dense(128, activation='relu', input_shape=(14,)),
                        Dense(32, activation='relu'),
                        Dense(64, activation='relu'),
                        Dense(64, activation='relu'),
                        Dense(64, activation='relu'),
                        Dense(1, activation='sigmoid')
])


#https://keras.io/api/losses/
#https://keras.io/api/optimizers/
#https://keras.io/api/metrics/

opt = Adam(lr=0.0003)
NeuralModel.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy','AUC'])
NeuralModel.fit(x_train, y_train, batch_size= 16, epochs = 16) #verbose = 1

y_pred = NeuralModel.predict(x_test)
y_pred = np.around(y_pred, decimals=0)
results = accuracy_score(y_test,y_pred)

print(f"accuracy: {results}")

# Accuracy wynosi 1 z powodu banalnego podziału na 2 klasy jakosci Wina: "bad" i "nice".