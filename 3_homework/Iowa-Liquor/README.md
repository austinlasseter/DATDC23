# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 1: Iowa Liqour Sales

You are a data scientist in residence at the Iowa State tax board. The Iowa State legislature is considering changes in the liquor tax rates and wants a report of current liquor sales by county and projections for the rest of the year. 


Your task is as follows:

* Calculate the yearly liquor sales for each store using the provided data. You can add up the transactions for each year, and store sales in 2015 specifically will be used later as your target variable.
* Use the data from 2015 to make a linear model using as many variables as you find useful to predict the yearly sales of all stores. You must use the sales from Jan to March as one of your variables.
* Use your model for 2015 to estimate total sales in 2016, extrapolating from the sales so far for Jan-March of 2016.
* Report your findings, including any projected increase or decrease in total sales (over the entire state) for the tax committee of the Iowa legislature.
* Use cross-validation to check how your model predicts to held out data compared to the model metrics on the full dataset.
* Fit your model(s) using one or both of the regularization tactics covered. Explain whether the regularized or the non-regularized model performed better and what the selected regression(s) are doing.


### Project Overview

The state of Iowa provides many data sets on their website, including [this dataset](https://data.iowa.gov/Economy/Iowa-Liquor-Sales/m3tr-qhgy) which contains transactions for all stores that have a class E liquor license.

Using the provided sample of this data set, you will create a model to accurately predict year-end liquor sales for each store based on data from the first quarter of the year.

In Part 1 of the project you will formulate a problem statement and identify SMART goals, aquire and clean the data, and perform exploratory data analysis.

In Part 2 of the project you will transform the data, engineer features, identify trends that will help your predictions, build a predictive model, tune your model, then present your results and evaluate your findings.


# Part 1 - Data Cleaning and Exploratory Data Analysis (EDA)

Remember the data science workflow:
![](../../1_lessons/01-what-is-data-science/assets/images/data-science-workflow-final.jpg)

In Part 1 of this two-part project, you will apply the skills you have learned manipulating data in Python with Pandas, Numpy, Matplotlib, Seaborn and other tools to import the Iowa Liquor data, clean the dataset, then perform exploratory analysis using visual and statistical methods.

In terms of the data science workflow, Part 1 will take you through 

## Files

- 3_homework/Iowa-Liquor/Assets/Iowa_Liquor_sample.csv - the dataset for this project
- 3_homework/Iowa-Liquor/Code/Project1-iowa_liquor_part_1_starter.ipynb - Jupyter Notebook for Part 1 of the Iowa Liquor Project

## Requirements 

In a Jupyter notebook (.ipynb), import, clean, and explore the Iowa Liquor dataset.

Your work must:
**Identify the problem**
- Write a high quality problem statement
- Describe the goals of your study and criteria for success

**Acquire and clean the data**
- Data has been provided from [Iowa.gov](https://data.iowa.gov/Economy/Iowa-Liquor-Sales/m3tr-qhgy), filtered and
reduced
- Import data using the Pandas Library
- Format, clean, slice, and combine the data in Python

**Explore the data**
- Perform exploratory analysis methods with visualization and statistical analysis
- Determine outliers, skew distribution of important variables (if any)
- Determine correlations / causations in the data
- State the risks and assumptions of your data
