import pandas as pd #The library pandas for interpretation of data
import matplotlib.pyplot as plt #This helps to plot graph of our data

df = pd.read_csv("C:\\Users\\Keshav\\Downloads\\student_bigdata.csv")


# 1. Display the first 5 rows
print("--- First 5 Rows ---",df.head())

# 2. Display the Shape (Rows, Columns)
print("\nShape of the dataset:\n", df.shape)

# 3. Display Column Names
print(f"\nColumn names:\n {df.columns.tolist()}")

# 4. Find missing values in each column
print("\n--- Missing Values Per Column ---",df.isnull().sum())

#5. Computing mean, median, and standard deviation for numerical columns
stats=df.drop(columns=['Student_ID']).describe().loc[['mean', '50%', 'std']]

print(stats.T)

#Histogram of the graph for Maths_Score
df['Math_Score'].plot(kind='hist')
plt.show()

#Histogram of the graph for Science_Score
df['Science_Score'].plot(kind='hist')
plt.show()

#Scatter Plot for Maths_Score vs Study_Hours
df.plot(kind='scatter', x='Math_Score', y='Study_Hours')
plt.show()

