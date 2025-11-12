import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Alice', 'Charlie'],
        'Age': [25, 30, 25, 35]}
df = pd.DataFrame(data)

# Remove duplicate rows based on all columns (default behavior)
unique_df = df.drop_duplicates()
print("DataFrame after drop_duplicates (default):")
print(unique_df)

# Remove duplicates based on 'Name' column, keeping the last occurrence
unique_names_last = df.drop_duplicates(subset='Name', keep='last')
print("\nDataFrame after drop_duplicates (subset='Name', keep='last'):")
print(unique_names_last)