import pandas as pd
import numpy as np

df = pd.DataFrame({
    "A": np.random.randint(1, 100, size=100000),
    "B": np.random.randint(1, 100, size=100000),
    "C": np.random.randint(1, 100, size=100000),
    "D": np.random.choice(["x", "y", "z"], size=100000)
})

df.to_csv(r"C:\Users\seakl\Documents\I5-AMS\Advand Programming\TP\TP-04\Ex2\data\sample.csv", index=False)

