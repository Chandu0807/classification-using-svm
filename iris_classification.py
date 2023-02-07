import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
columns = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Class_labels'] 
# Load the data
df = pd.read_csv('Iris.csv')
df.head()