import pandas as pd

# Sample DataFrame with a Date column
data = {
    'Date': ['2021-01-15', '2021-02-05', '2021-05-20', '2021-12-25', '2022-02-01', '2022-03-10'],
    'Value': [10, 20, 30, 40, 50, 60]
}

df = pd.DataFrame(data)

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Define the date range
start_date = '2021-02-02'
end_date = '2022-02-02'

# Filter the DataFrame for the specified date range
filtered_df = df.loc[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

print(filtered_df)

