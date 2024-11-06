import pandas as pd

# Sample DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Age': [25, 30, 35]})
df3 = pd.DataFrame({'ID': [1, 2], 'City': ['New York', 'Los Angeles']})

# Method 1: Merge (similar to SQL JOIN)
merged_df = pd.merge(df1, df2, on='ID', how='inner')

# Method 2: Join (combine based on index)
joined_df = df1.set_index('ID').join(df2.set_index('ID'))

# Method 3: Concatenate (adding rows)
concatenated_df = pd.concat([df1, df3], ignore_index=True)
print("Merged DataFrame:\n", merged_df)
print("\nJoined DataFrame:\n", joined_df)
print("\nConcatenated DataFrame:\n", concatenated_df)
