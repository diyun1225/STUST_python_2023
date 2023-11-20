# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

# 定義函數計算發電功率
def calculate_power(v, blade_width, blade_thickness, rho=1.225, cp=0.35):
    A = blade_width * blade_thickness
    return 0.5 * rho * A * cp * v**3

# 定義風速範圍
wind_speeds = np.linspace(1, 15, 100)

# 假設葉片寬度為 12 公分，厚度為 21.19 毫米（轉換為米）
blade_width = 0.12
blade_thickness = 0.02119

# 計算不同風速下的發電功率
power_output = [calculate_power(v, blade_width, blade_thickness) for v in wind_speeds]

# 繪製風機性能曲線
plt.plot(wind_speeds, power_output, label=u'Fan performance curve')
plt.xlabel(u'Wind speed  (m/s)')
plt.ylabel(u'Generating powe (W)')
plt.title(u'Vertical axis wind turbine fan performance curve')
plt.legend()
plt.grid(True)
plt.show()