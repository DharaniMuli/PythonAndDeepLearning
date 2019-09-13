import pandas as pd


# visualization
import seaborn as sns
import matplotlib.pyplot as plt

##reading data set
train_df = pd.read_csv('../train.csv')
test_df = pd.read_csv('../test.csv')
combine = [train_df, test_df]

# print(train_df.head())

print(train_df[["Sex", "Survived"]].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False))



##Analyze by visualizing data
####Correlating numerical features
g = sns.FacetGrid(train_df, col='Survived')
g.map(plt.hist, 'Sex', bins=20)
plt.show()
