# pands-project

# Programming and Scripting

This README has been written with [GitHub's documentation on README's](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) in mind.

## About this Project

This repository contains my weekly assignments for ATU module 4122 -- PROGRAMMING AND SCRIPTING. It contains the project work for the course, which is focused on the Iris dataset. As part of this, this project intends to:

1. Provide an outline of the Iris dataset and the data it contains.
2. Download a copy of the data set into the repository.
3. Write a program called analysis.py that: 
    - Outputs a summary of each variable to a single text file.
    - Saves a histogram of each variable to png files.
    - Outputs a scatter plot of each pair of variables.
    - Performs any other analysis you think is appropriate.


## About the Dataset

First published in 1936, the Iris dataset is one of the earliest datasets used in the literature on classification methods.  Originally published by the UCI Machine Learning Repository, the dataset consists of 150 rows, each row representing an Iris plant. There are three major subdivisons, each representing a different species of Iris with the 150 rows being equally divided amoung these three types. These three species are:
 - Iris setosa: Characterized by its relatively small size, with distinctive characteristics in sepal and petal dimensions.
 - Iris versicolor: Moderate in size, with features falling between those of Iris setosa and Iris virginica.
 - Iris virginica: Generally larger in size, with notable differences in sepal and petal dimensions compared to the other two species.

The dataset includes further information on features related to each species flower. The are four key variables for each flower, which include:
 - Sepal Length: The length of the iris flower's sepals 
 - Sepal Width: The width of the iris flower's sepals.
 - Petal Length: The length of the iris flower's petals.
 - Petal Width: The width of the iris flower's petals.

 This dataset is often used for testing machine learning algorathims due to its simplicity, versatility and ubiquitousness. For these reasons, the dataset remains a common point of reference for many people starting to look into statistics, programming and data science.

## Use of this Project

This repository may be of some interest to other students engaged in similar projects around programming and scripting. Feel free to use whatever you like from it (though if another party has been referenced, I would ask that you likewise cite them).

## Getting Started

The workbook is structured in a linear fashion, so reading through it from start to finish is the best approach.

To understand how the workbook has developped to date, please see below a timeline of the work done on the notebook and the material referenced in the course of this work:

- 21/03/2025 - Created ReadMe and Gitignore file. Gitignore file generated using the template at Python gitignore template at https://github.com/github/gitignore/blob/main/Python.gitignore, the Windows gitignore template at https://github.com/github/gitignore/blob/main/Global/Windows.gitignore, the MacOS gitignore template at https://github.com/github/gitignore/blob/main/Global/macOS.gitignore and the Linux gitignore template at https://github.com/github/gitignore/blob/main/Global/Linux.gitignore.
- 22/03/2025 - Created analysis.py and Iris.ipynb. Loaded in the Iris dataset, using the instructions at: https://archive.ics.uci.edu/dataset/53/iris and https://github.com/uci-ml-repo/ucimlrepo.
- 23/03/2025 - Saved a copy of the Iris dataset into the directory ("data.csv"). External materials referenced: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html (how to save a dataset as a csv dataframe).
- 28/03/2025 - Added a desciption of the dataset to the ReadMe. External materials referenced: https://www.geeksforgeeks.org/iris-dataset/, https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/, https://en.wikipedia.org/wiki/Iris_flower_data_set, https://archive.ics.uci.edu/dataset/53/iris, https://gist.github.com/curran/a08a1080b88344b0c8a7 (all links referenced are introductions to the dataset).
- 29/03/2025 - Plotted histograms of each of the main Iris variables. Created "iris_variables.png" as part of this process. External materials referenced: https://www.geeksforgeeks.org/plotting-histogram-in-python-using-matplotlib/ (plotting histograms in Python).
- 31/03/2025 - Started work on scatter plots. Had to halt early due to issues with accessing the server with the Iris dataset. External materials referenced: https://www.statology.org/pandas-scatter-plot-multiple-columns/ (creating a scatter plot with multiple variables on it).
- 04/04/2025 - Swapped to using seaborn for the scatter charts to better differencitate the types of Iris in the data. External material referenced: https://www.geeksforgeeks.org/scatterplot-using-seaborn-in-python/ (scatterplots in seaborn).
- 06/04/2025 - Fixed "data.csv" so that the Class column no longer includes the word Iris. Added in a heatmap showing how all the various External materials referenced: https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/ (how to generate a heatmap of the Iris dataset).
- 07/04/2025 - Added text summary of each variable ("iris_variables_description.txt"). External material referenced: https://www.geeksforgeeks.org/python-pandas-dataframe-transpose/ (how to flip a datasets rows and columns).
- 08/04/2025 - Added new histograms which break down analysis by species. External materials referenced: https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/ (generating an advanced histogram of the Iris dataset), https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751 (adjusting histplot to look like distplot). Copilot referenced, prompt "how to group multiple histograms into one png". Also, adjusted dataframe to improve its readability in the graphs (adding "(cm)" to variable headers and changing "class" to "species").
- 09/04/2025 - Added in header image, tidied up section hears and improved the readability of the code in some sections.
- 10/04/2025 - Added in some text to improve the readability of the "iris.ipynb" and tidied up some of the graphs a bit. Copilot referenced, prompt "how to add in some white sapce between grouped charts in a png which have been assembled using python".

## Getting help

Queries about this repository can be directed directly to my GitHub account (NeilTynan).

## Other References

Iris, UCI Machine Learning Repository - https://archive.ics.uci.edu/dataset/53/iris

## Author

I am student Atlantic Technological University's Higher Diploma in Data Science.
