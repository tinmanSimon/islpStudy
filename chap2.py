import pandas as pd
import matplotlib.pyplot as plt

# 8.a
print("Question 8.a:")
collegePath = 'College.csv'
college = pd.read_csv(collegePath)
print(college)
print("*******************************\n\n\n")

# 8.b
print("Question 8.b:")
college = college.rename({ "Unnamed: 0" : "College" }, axis=1)
college = college.set_index("College")
print(college)
print("*******************************\n\n\n")

# 8.c
print("Question 8.c:")
print(college.describe())
print("*******************************\n\n\n")

# 8.d
print("Question 8.d:")
pd.plotting.scatter_matrix(college[['Top10perc', 'Apps', 'Enroll']])
plt.suptitle('8.d Top10perc, Apps, Enroll scatter matrix')
print("*******************************\n\n\n")

# 8.e
print("Question 8.e:")
college.boxplot(column='Outstate', by='Private')
plt.suptitle('8.e Outstate/Private Boxplot')
print("*******************************\n\n\n")

# 8.f
print("Question 8.f:")
college['Elite'] = pd.cut(college['Top10perc'], [0, 50, 100], labels=['No', 'Yes'])
print(college)
print("College Elite value counts:")
print(college['Elite'].value_counts())
college.boxplot(column='Outstate', by='Elite')
plt.suptitle('8.f Outstate/Elite Boxplot')
print("*******************************\n\n\n")























plt.show()