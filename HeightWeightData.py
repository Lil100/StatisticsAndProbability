import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import ttest_ind

url = "https://www4.stat.ncsu.edu/~boos/var.select/diabetes.tab.txt"
df = pd.read_csv(url,  delimiter="\t")
mean = df[['AGE', 'SEX', 'BMI', 'BP', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'Y']].mean()
var = df[['AGE', 'SEX', 'BMI', 'BP', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'Y']].var()
print(f"The mean of the values is \n{mean} \nand the variance is\n{var}")

#Boxplots for BMI, BP and Y against SEX
df.boxplot(column= 'BMI', by= 'SEX')
df.boxplot(column= 'BP', by= 'SEX')
df.boxplot(column= 'Y', by= 'SEX')

#Distribution of AGE, SEX, BMI And Y
plt.figure()
plt.hist(df['AGE'], edgecolor='black')  # Plot histogram
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Age')  # Set title

# Plot histogram for 'Sex'
plt.figure()
plt.hist(df['SEX'], bins=2, edgecolor='black')  # Plot histogram
plt.xlabel('Sex')
plt.ylabel('Frequency')
plt.title('Distribution of Sex')

# Plot histogram for 'BMI'
plt.figure()
plt.hist(df['BMI'], bins=20, edgecolor='black')
plt.xlabel('BMI')
plt.ylabel('Frequency')
plt.title('Distribution of BMI')

# Plot histogram for 'Y'
plt.figure()
plt.hist(df['Y'], bins=10, edgecolor='black')
plt.xlabel('Y')
plt.ylabel('Frequency')
plt.title('Distribution of Y')

#Testing the correlation between different variables and disease progression (Y)
correlation_matrix = df[['AGE', 'SEX', 'BMI', 'BP', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'Y']].corr()['Y']
print(correlation_matrix)

#Testing the hypothesis that the degree of diabetes progression is different between men and women
men_data = df[df['SEX']== 1]['Y']
women_data = df[df['SEX'] == 2]['Y']

#independent t-test
t_statistic, p_value = ttest_ind(men_data, women_data)

print("T-Statistic:", t_statistic)
print("P-Value:", p_value)

#conclusion:There is insufficient evidence to conclude that there is a significant difference in the degree of diabetes progression between men and women in the given dataset.