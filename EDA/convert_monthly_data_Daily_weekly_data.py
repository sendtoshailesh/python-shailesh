import pandas as pd

# Sample DataFrame with monthly data
dates = pd.date_range('2021-01-01', periods=4, freq='M')
data = pd.DataFrame({'Value': [100, 200, 300, 400]}, index=dates)

# Method 1: Convert Monthly to Daily
daily_data = data.resample('D').ffill()

# Method 2: Convert Monthly to Weekly
weekly_data = data.resample('W').ffill()

print("Daily Data:\n", daily_data)
print("\nWeekly Data:\n", weekly_data)

