# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ucimlrepo import fetch_ucirepo


# Fetch the dataset
iris = fetch_ucirepo(id=53)
X = iris.data.features
y = iris.data.targets 
z = iris.data.original
df = pd.DataFrame(z)

# Print dataset to repository
df.to_csv("/workspaces/pands-project/data.csv")

# Print description of variables to repository
text = df.describe().T
text.index.name = 'variable'
text1 = text.round(1)
text1.to_csv("/workspaces/pands-project/iris_variables_description.txt")

# Improve dataset readability
df.columns = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'species']
df['species'] = df['species'].replace({'Iris-setosa': 'Setosa', 'Iris-versicolor':'Versicolor', 'Iris-virginica': 'Virginica'}, regex=True)

# Generating a histogram of the Iris dataset which includes a breakdown
fig, axes = plt.subplots(2, 2, figsize=(12, 10), gridspec_kw={'hspace': 0.3})
sns.histplot(df, x="sepal length (cm)", hue="species", kde=True,  alpha=.4, edgecolor=(1, 1, 1, .4), ax=axes[0, 0]) 
axes[0, 0].set_title('Sepal Length Distribution')
sns.histplot(df, x="sepal width (cm)", hue="species", kde=True,  alpha=.4, edgecolor=(1, 1, 1, .4), ax=axes[0, 1])
axes[0, 1].set_title('Sepal Width Distribution')
sns.histplot(df, x="petal length (cm)",hue="species", kde=True,  alpha=.4, edgecolor=(1, 1, 1, .4), ax=axes[1, 0])
axes[1, 0].set_title('Petal Length Distribution')
sns.histplot(df, x="petal width (cm)", hue="species", kde=True,  alpha=.4, edgecolor=(1, 1, 1, .4), ax=axes[1, 1])
axes[1, 1].set_title('Sepal Width Distribution - Histograms')
plt.suptitle('Iris Dataset Variables - Breakdown by Histogram', fontweight="bold", y=0.93)


# Define the output directory and file path
name  = 'iris_histogram.png'
plt.savefig('/workspaces/pands-project/graphs/{}'.format(name))


# create scatter plot of the petal variables
fig, axes = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'hspace': 0.3})
ax = sns.scatterplot(data=df, x='petal length (cm)', y='petal width (cm)', color='steelblue', hue='species', palette= 'viridis', ax=axes[0])
axes[0].set_title('Petal Length/Width')
ax = sns.scatterplot(data=df, x='sepal length (cm)', y='sepal width (cm)', color='steelblue', hue='species', palette= 'viridis', ax=axes[1])
axes[1].set_title('Sepal Length/Width')
plt.suptitle('Iris Dataset Variables - Breakdown by Scatterchart', fontweight="bold", y=0.97)

# Saving the histogram into the directory
name  = 'iris_scatter.png'
plt.savefig('/workspaces/pands-project/graphs/{}'.format(name))