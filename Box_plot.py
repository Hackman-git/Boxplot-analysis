'''
Name:   Olugbenga Abdulai
ID:     A20447331
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.cbook import boxplot_stats

# Reading the file
path = r"C:\Users\abdul\Desktop\CS 584\HW\HW 1\NormalSample.csv"
file = pd.read_csv(path)
col = file['x']
N = col.size


'''
Q 2(a): (i) Five number summary of x - the min, max, median, 
        first quartile, and third quartile
        (ii) upper and lower whiskers
'''
print(col.describe())
# getting the quartiles
first_quart, third_quart = np.percentile(col, [25, 75])
iqr = third_quart - first_quart

# getting the whisker points
upper_whisk = third_quart + 1.5 * iqr
lower_whisk = first_quart - 1.5 * iqr

print('upper whisker for overall data: ', upper_whisk)
print('lower whisker for overall data: ', lower_whisk)

'''
Q 2(b): Five number summary of x for each category
        of the group and upper & lower whiskers
'''
# subsetting the two groups from the overall dataframe
group_zero = file.loc[file['group'] == 0, ['x']]
group_one = file.loc[file['group'] == 1, ['x']]

print('summary of group zero:\n', group_zero.describe())
print('summary of group one:\n', group_one.describe())

first_quart, third_quart = np.percentile(group_zero, [25, 75])
iqr = third_quart - first_quart

upper_whisk_group_zero = third_quart + 1.5 * iqr
lower_whisk_group_zero = first_quart - 1.5 * iqr

print('upper whisk group zero: ', upper_whisk_group_zero)
print('lower whisk group zero: ', lower_whisk_group_zero)

first_quart, third_quart = np.percentile(group_one, [25, 75])
iqr = third_quart - first_quart

upper_whisk_group_one = third_quart + 1.5 * iqr
lower_whisk_group_one = first_quart - 1.5 * iqr

print('upper whisk group one: ', upper_whisk_group_one)
print('lower whisk group one: ', lower_whisk_group_one)

'''
Q 2(c): Boxplot of x
'''
sns.boxplot(col, orient='vertical', color='yellow')
plt.show()

'''
Q 2(d): boxplots for each group and overall boxplot
'''
# splitting the overall data into groups
overall_data = file.copy()
overall_data['group'] = 'all data'
group_zero = file.loc[file['group'] == 0, :]
group_one = file.loc[file['group'] == 1, :]

# combining the data segments for the box plot
combined = pd.concat([overall_data, group_zero, group_one], axis=0)
sns.boxplot(x=combined['group'],  y=combined['x'])
plt.show()

# obtaining the outlier values
stats = boxplot_stats(overall_data['x'])
print('outliers for overall data: ', stats[0]['fliers'])

stats = boxplot_stats(group_one['x'])
print('outliers for group one: ', stats[0]['fliers'])

stats = boxplot_stats(group_zero['x'])
print('outliers for group zero: ', stats[0]['fliers'])