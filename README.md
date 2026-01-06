# Project Overview
This project focuses on analyzing a large-scale student dataset using the Python Pandas and Matplotlib libraries.
The objective was to clean, inspect, and visualize the data to find patterns between student habits and their academic outcomes.

# What the Code Does
The script performs the following operations:

Loads a local CSV file into a Pandas DataFrame.

Previews the top 5 records to verify data integrity.

Prints the Shape (total rows/columns) to understand the scale of the dataset.

Lists all Column Names for mapping the available variables.

Identifies missing values (nulls) to ensure the analysis isn't full by empty entries.

Calculates meaningful Mean, Median, and Standard Deviation for the academic scores.

Generates three key plots to see the distribution and relationships within the data.

# Observations & Data Insights
By plotting histograms for Math_Score and Science_Score, we can see the "spread" of grades.
If the bars are taller in the middle, the students are performing at an average level. If they are skewed toward the right, the class is performing exceptionally well.

The scatter plot comparing Math_Score against Study_Hours is the most critical visualization in this script.
We are looking for a Positive Correlation. If the dots move upward and to the right, the data proves that as study hours increase, math scores generally improve as well.

The std (Standard Deviation) calculated in the stats table tells us how much student scores vary.
A high standard deviation means there is a wide gap between the highest and lowest-scoring students, whereas a low standard deviation indicates the class is performing at a very similar level.








