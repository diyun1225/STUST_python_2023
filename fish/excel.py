# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

	
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
# Age categories and corresponding number of operators
age_groups = ['15-24', '25-44', '45-64', '65-69', '70+']
num_operators = [53, 3480, 18793, 5185, 7580]  # Sample data based on the description

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(age_groups, num_operators, color='skyblue')

# Title and labels
plt.title(u'臺灣從事漁業之經營管理者分佈年齡')
plt.xlabel(u'年齡層（歲）')
plt.ylabel(u'人數（人）')

# Show grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the figure
plt.show()
