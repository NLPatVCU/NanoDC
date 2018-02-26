import pandas as pd
import numpy as np
import re
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix


regexp = re.compile('nano')
abstracts = pd.read_json("../Data/Datasets/abstracts.json")
X = abstracts['abstract'].values
y = abstracts['is_nano'].values

predictions = []
for abstract in X:
    if regexp.search(abstract, re.IGNORECASE):
        predictions.append(1)
    else:
        predictions.append(0)

true = []
for value in y:
    if value == "Yes":
        true.append(1)
    else:
        true.append(0)

predictions = np.array(predictions)
true = np.array(true)

print("Predictions", predictions)
print("True", true)

print("Accuracy", accuracy_score(y_true=true, y_pred=predictions))
print("Precision: ", precision_score(y_true=true, y_pred=predictions))
print("Recall: ", recall_score(y_true=true, y_pred=predictions))
print("F1 Score: ", f1_score(y_true=true, y_pred=predictions))
