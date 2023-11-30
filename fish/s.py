# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']

# 年龄分类及其对应的经营者人数
age_groups = ['15-24', '25-44', '45-64', '65-69', '70+']
num_operators = [38, 2218, 11662, 3233, 4802]  # 根据描述提供的示例数据

# 创建条形图
plt.figure(figsize=(10, 6))
bars = plt.bar(age_groups, num_operators, color='skyblue')

# 标题和标签
plt.title(u'臺灣南部地區魚塭產業之業者分佈年齡')
plt.xlabel(u'年齡層(歲)')
plt.ylabel(u'業者數量(人)')

# 在每个条形上显示数量
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom')  # va='bottom' 确保数字在条形的顶部

# 显示网格
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 保存图表

plt.show()
