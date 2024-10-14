# packages
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics import gofplots as gf # for qq plots
from statsmodels.graphics.mosaicplot import mosaic # for mosaic plot

# load the data
file_name = ""
df = pd.read_csv(file_name)

# check for null values
print(df.isnull().sum())
df = df.dropna()

# get statistics
df.describe()

# get column names
column_names = df.columns.values
print(column_names)

# separate data using column values
survived = df.loc[df['Survive']=="survived"]
# variable_name = df.loc[df['column name']=="value"]

# separate data using both rows and columns

# histogram
figure, axes = plt.subplots()
sns.histplot(survived_group, bins=30, kde=True, ax=axes, label="Survived")
sns.histplot(dead_group, bins= 30, kde=True, ax= axes, label="Dead")
plt.title("Histograms for data distribution of two groups")
plt.legend()
plt.savefig("sfaaa.jpg")


# qq plots
figure, axes = plt.subplots(nrows=1, ncols=2)
gf.qqplot(survived_group['Squamosal horn length'], ax=axes[0], line='s')
axes[0].title.set_text('QQplot of the survived group')
gf.qqplot(dead_group['Squamosal horn length'], ax=axes[1], line='s')
axes[1].title.set_text('QQplot of the dead group')
plt.savefig("sfaaa.jpg")

# boxplots
figure, axes = plt.subplots()
sns.boxplot(x= df['Survive'], y= df['Squamosal horn length'], ax= axes)
plt.savefig("sfaaa.jpg")

# violinplots
figure, axes = plt.subplots()
sns.violinplot(x= df['Survive'], y= df['Squamosal horn length'], ax= axes)
plt.savefig("sfaaa.jpg")

# shapiro test
test_stat, p_value = stats.shapiro(survived_group['Squamosal horn length'])
print(test_stat)
print(p_value)

# one sample t test
test_statistic, p_value = stats.ttest_1samp(temp_data, 98.6)
print(test_statistic)
print(p_value)

# independent t test
test_stat, p_value = stats.ttest_ind(survived_group['Squamosal horn length'], dead_group['Squamosal horn length'], alternative="two-sided")
print(test_stat)
print(p_value)

# paired t test
statis, p = stats.ttest_rel(dataset['Before'], dataset['After'], alternative= "less")
print("============================Paired t test===========================")
print("Test statistic : ",statis)
print("P_value : ",p)

# Create contingency table
contingency_table = pd.DataFrame([[1, 10, 37],[49, 35, 9]], columns=['Uninfected', 'Lightly infected', 'Highly infected']
                                 , index= ['Eaten','Not-eaten'])
contingency_table.loc['Column total'] = contingency_table.sum()
contingency_table['Row total'] = contingency_table['Uninfected'] + \
                                 contingency_table['Lightly infected'] + \
                                 contingency_table['Highly infected']
# Stack the created contingency table
contingency_table_stacked = contingency_table.iloc[0:2,0:3].stack()

# Mosaic plot
mosaic(contingency_table_stacked, [0,1])
plt.title("Mosaic table for observed data")
plt.show()

# Chi square contingency test
test_result = stats.chi2_contingency(contingency_table)
print("========================Chi-square contingency test==============================")
print("Chi square statistic :",test_result.statistic)
print("P-value",test_result.pvalue)
print("Degrees of Freedom",test_result.dof)

# Expected frequencies of the test
expected = pd.DataFrame(test_result.expected_freq, columns=['Uninfected', 'Lightly infected', 'Highly infected', 'Row total'],
                        index= ['Eaten','Not-eaten','Column total'])
print(expected)