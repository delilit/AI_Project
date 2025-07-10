from sklearn.ensemble import GradientBoostingClassifier
import joblib
import numpy as np

model = joblib.load('model.pkl')

input_data = [180000, 60, 0.2, 0.0]

input_array = np.array(input_data).reshape(1, -1)

prediction = model.predict(input_array)

print("it's done")