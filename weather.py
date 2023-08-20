# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import json

# df = pd.read_csv('./allweather-2018.csv')

# df['Date'] = pd.to_datetime(df['Date'])
# df['Date'] = df['Date'].dt.strftime('%m-%d-%Y')

# df['Hi Temp'] = pd.to_numeric(df['Hi Temp'], errors='coerce')
# df['Low Temp'] = pd.to_numeric(df['Low Temp'], errors='coerce')

# df['Avg Temp'] = (df['Hi Temp'] + df['Low Temp']) / 2

# columns_to_keep = ['Date', 'Time', 'Avg Temp']  # List the columns you want to keep
# df = df[columns_to_keep]

# daily_avg_temp = df.groupby("Date")["Avg Temp"].mean().reset_index()

# # Create a list of dates in the format 'mm-dd-yyyy' for January 2018
# january_dates = [f'01-{str(day).zfill(2)}-2018' for day in range(1, 32)]

# # Create a DataFrame for January 2018 with 'Avg Temp' set to NaN for all days
# january_df = pd.DataFrame({'Date': january_dates, 'Avg Temp': np.nan})

# # Concatenate the January DataFrame with the existing daily_avg_temp DataFrame
# complete_daily_avg_temp = pd.concat([january_df, daily_avg_temp])

# # Sort the DataFrame by 'Date'
# complete_daily_avg_temp = complete_daily_avg_temp.sort_values(by='Date')

# print(daily_avg_temp)

# date_list = daily_avg_temp['Date'].tolist()
# temp_list = daily_avg_temp['Avg Temp'].tolist()

# # print(date_list)
# # print(temp_list)

# #Create a dictionary in the desired format
# json_data = {
#     'date': date_list,
#     'temp': temp_list
# }

# # Write the JSON data to a file
# with open('rhodesWeatherStation_2018.json', 'w') as json_file:
#     json.dump(json_data, json_file, indent=4)

# print("Data exported to rhodesWeatherStation_" + ".json")



import numpy as np
import pandas as pd
import json

# Load your existing data from the CSV file
df = pd.read_csv('./allweather-2018.csv')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].dt.strftime('%m-%d-%Y')

# Convert 'Hi Temp' and 'Low Temp' columns to numeric, setting errors to coerce
df['Hi Temp'] = pd.to_numeric(df['Hi Temp'], errors='coerce')
df['Low Temp'] = pd.to_numeric(df['Low Temp'], errors='coerce')

# Calculate the 'Avg Temp' column as the average of 'Hi Temp' and 'Low Temp'
df['Avg Temp'] = (df['Hi Temp'] + df['Low Temp']) / 2

# List of columns to keep
columns_to_keep = ['Date', 'Time', 'Avg Temp']

# Filter the DataFrame to only keep the desired columns
df = df[columns_to_keep]

# Group by 'Date' and calculate the daily average temperature
daily_avg_temp = df.groupby("Date")["Avg Temp"].mean().reset_index()

# Create a list of dates in the format 'mm-dd-yyyy' for January 2018
january_dates = [f'01-{str(day).zfill(2)}-2018' for day in range(1, 32)]

# Create a DataFrame for January 2018 with 'Avg Temp' set to NaN for all days
january_df = pd.DataFrame({'Date': january_dates, 'Avg Temp': 22.5})

# Concatenate the January DataFrame with the existing daily_avg_temp DataFrame
complete_daily_avg_temp = pd.concat([january_df, daily_avg_temp])

# Sort the DataFrame by 'Date'
complete_daily_avg_temp = complete_daily_avg_temp.sort_values(by='Date')

# Convert 'Date' column back to datetime format if needed
complete_daily_avg_temp['Date'] = pd.to_datetime(complete_daily_avg_temp['Date'])

# Reset index
complete_daily_avg_temp = complete_daily_avg_temp.reset_index(drop=True)

# Create a dictionary in the desired format
json_data = {
    'date': complete_daily_avg_temp['Date'].dt.strftime('%m-%d-%Y').tolist(),
    'temp': complete_daily_avg_temp['Avg Temp'].tolist()
}

# Write the JSON data to a file
with open('rhodesWeatherStation_2018.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=4)

print("Data exported to rhodesWeatherStation_2018.json")
