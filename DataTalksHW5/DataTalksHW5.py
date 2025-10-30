import numpy as np
import pandas as pd
import pickle
import sklearn

with open("pipeline_v1.bin", "rb") as f:
    model = pickle.load(f)


record = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0,
}

X = [record]

probs = model.predict_proba(X)[0, 1]
print(f"Probability of conversion: {probs:.3f}")
