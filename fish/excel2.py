# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']

# Data from the provided image for IoT market forecast
iot_forecast_data = {
    'Year': ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023f', '2024f', '2025f', '2026f', '2027f'],
    'Number of Connections (Billions)': [3.6, 4.6, 6.1, 8.0, 10.0, 11.3, 12.2, 14.4, 16.7, 19.2, 22.2, 25.5, 29.7]
}

# Creating a DataFrame
df_iot_forecast = pd.DataFrame(iot_forecast_data)

# Plotting the forecast data
plt.figure(figsize=(14, 7))
plt.plot(df_iot_forecast['Year'], df_iot_forecast['Number of Connections (Billions)'], marker='o', linestyle='-', color='blue')
plt.fill_between(df_iot_forecast['Year'], df_iot_forecast['Number of Connections (Billions)'], color="skyblue", alpha=0.4)

plt.title(u'2015年到2027年全球物聯網（IoT）連接量預估')
plt.xlabel(u'年')
plt.ylabel(u'全球活躍的IoT連接數量(十億)')
plt.grid(True)
plt.tight_layout()

# Show plot
plt.show()
