import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

# 8.g
print("Question 8.g:")
fig, ax = plt.subplots(nrows=2, ncols=2)
ax[0,0].title.set_text("Grad.Rate")
college.plot.hist(density=True, column='Grad.Rate', ax=ax[0,0], edgecolor='White', bins=np.arange(0, max(college['Grad.Rate']) + 1, 10))
ax[0,1].title.set_text("Enroll")
college.plot.hist(density=True, column='Enroll', ax=ax[0,1], edgecolor='White', bins=np.arange(0, max(college['Enroll']) + 1, 500))
ax[1,0].title.set_text("S.F.Ratio")
college.plot.hist(density=True, column='S.F.Ratio', ax=ax[1,0], edgecolor='White', bins=np.arange(0, max(college['S.F.Ratio']) + 1, 10))
ax[1,1].title.set_text("Top10perc")
college.plot.hist(density=True, column='Top10perc', ax=ax[1,1], edgecolor='White', bins=np.arange(0, max(college['Top10perc']) + 1, 10))
print("*******************************\n\n\n")

# 8.h
print("Question 8.g:")
print("The data of Grad.Rate is wrong. We have values like 118, how can you graduate at 118%? doesn't make sense.")
print("*******************************\n\n\n")

















plt.show()