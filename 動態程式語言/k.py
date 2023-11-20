# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

# 定義函數計算發電功率
def calculate_power(v, blade_width, blade_thickness, rho=1.225, cp=0.35):
    A = blade_width * blade_thickness
    return 0.5 * rho * A * cp * v**3

# 定義函數計算效率
def calculate_efficiency(cp):
    return cp * 16 / 27

# 定義風速範圍
wind_speeds = np.linspace(1, 15, 100)

# 假設葉片寬度為 12 公分，厚度為 21.19 毫米（轉換為米）
blade_width = 0.12
blade_thickness = 0.02119

# 計算不同風速下的發電功率和效率
power_output = [calculate_power(v, blade_width, blade_thickness) for v in wind_speeds]
efficiency = [calculate_efficiency(0.35) for _ in wind_speeds]  # 假設 C_p 為 0.35

# 繪製風速 vs 發電功率 曲線
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(wind_speeds, power_output, label='import matplotlib.pyplot as plt')
import numpy as np

# 定義函數計算發電功率
def calculate_power(v, blade_width, blade_thickness, rho=1.225, cp=0.35):
    A = blade_width * blade_thickness
    return 0.5 * rho * A * cp * v**3

# 定義函數計算效率
def calculate_efficiency(cp):
    return cp * 16 / 27

# 定義風速範圍
wind_speeds = np.linspace(1, 15, 100)

# 假設葉片寬度為 12 公分，厚度為 21.19 毫米（轉換為米）
blade_width = 0.12
blade_thickness = 0.02119

# 計算不同風速下的發電功率和效率
power_output = [calculate_power(v, blade_width, blade_thickness) for v in wind_speeds]
efficiency = [calculate_efficiency(0.35) for _ in wind_speeds]  # 假設 C_p 為 0.35

# 繪製風速 vs 發電功率 曲線
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(wind_speeds, power_output, label='Generating power')
plt.xlabel('wind speed (m/s)')
plt.ylabel('Generating power (W)')
plt.title('wind speed vs Generating power')
plt.legend()
plt.grid(True)

# 繪製風速 vs 效率 曲線
plt.subplot(1, 2, 2)
plt.plot(wind_speeds, efficiency, label='efficiency')
plt.xlabel('wind speed (m/s)')
plt.ylabel('efficiency')
plt.title('wind speed vs efficiency')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
plt.xlabel('wind speed (m/s)')
plt.ylabel('Generating power (W)')
plt.title('wind speed vs Generating power')
plt.legend()
plt.grid(True)

# 繪製風速 vs 效率 曲線
plt.subplot(1, 2, 2)
plt.plot(wind_speeds, efficiency, label='efficiency')
plt.xlabel('wind speed (m/s)')
plt.ylabel('efficiency')
plt.title('wind speed vs efficiency')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()