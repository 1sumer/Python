import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

class TitanicEDA:
    def __init__(self, data):
        self.data = data

    def save_to_excel(self, filepath):
        """Save dataset to an Excel file."""
        self.data.to_excel(filepath, index=False)
        print(f"Data saved to {filepath}")

    def basic_info(self):
        """Display basic information about the dataset."""
        print("Head of the dataset:")
        print(self.data.head())
        print("\nShape of the dataset:", self.data.shape)
        print("\nColumns in the dataset:", self.data.columns.tolist())
        print("\nInfo about the dataset:")
        print(self.data.info())
        print("\nStatistical summary of numeric columns:")
        print(self.data.describe().T)
        print("\nStatistical summary of categorical columns:")
        print(self.data.describe(include='object').T)

    def check_missing_duplicates(self):
        """Check for missing values and duplicates."""
        print("\nMissing values per column:")
        print(self.data.isnull().sum())
        print("\nNumber of duplicate rows:", self.data.duplicated().sum())

    def clean_data(self):
        """Clean the dataset by removing unwanted columns, filling missing values, and dropping duplicates."""
        columns_remove = ['deck', 'embarked', 'alive', 'pclass']
        self.data.drop(columns=columns_remove, inplace=True)
        self.data['age'] = self.data['age'].transform(lambda x: x.fillna(round(x.mean())))
        self.data['embark_town'] = self.data['embark_town'].transform(lambda x: x.fillna(x.mode()[0]))
        self.data.drop_duplicates(inplace=True)
        print("\nData cleaned successfully.")

    def create_age_group(self):
        """Create a new column for age groups."""
        def categorize(age):
            if age < 17.0:
                return 'Young'
            elif age < 34.0:
                return 'Adult'
            elif age < 54.0:
                return 'Middle age'
            else:
                return 'Seniors'
        
        self.data['Age_group'] = self.data['age'].apply(categorize)
        print("\nAge group column added.")

    def display_value_counts(self, column):
        """Display value counts for a categorical column."""
        print(f"\nValue counts for {column}:")
        print(self.data[column].value_counts())

    def univariate_analysis(self):
        """Perform univariate analysis for numeric and categorical columns."""
        print("\nUnivariate Analysis:")
        numeric_cols = self.data.select_dtypes(include=np.number).columns.tolist()
        for col in numeric_cols:
            print(f"\nHistogram for {col}:")
            plt.hist(self.data[col], alpha=0.5, bins=20, color='r', edgecolor='black')
            plt.ylabel('Frequency')
            plt.title(f'Distribution of {col}')
            plt.show()

        categorical_cols = self.data.select_dtypes(exclude=np.number).columns.tolist()
        for col in categorical_cols:
            plt.figure()
            sns.countplot(x=col, data=self.data, order=self.data[col].value_counts().index, palette='viridis')
            plt.title(f'Distribution of {col}')
            plt.show()

    def bivariate_analysis(self):
        cols = ['sex', 'class', 'who', 'embark_town', 'alone', 'adult_male', 'Age_group', 'sibsp', 'parch']
        n_plots = len(cols)
        n_cols = 2  # Number of columns in the grid
        n_rows = math.ceil(n_plots / n_cols)  # Calculate required rows
        
        plt.figure(figsize=(14, n_rows * 7))  # Adjust the figure height dynamically
        for i, col in enumerate(cols):
            plt.subplot(n_rows, n_cols, i + 1)
            sns.countplot(x=col, hue='survived', data=self.data, palette='Set1')
            plt.legend(title='Survived', loc='upper right')
            plt.title(f'Survivor by {col}')
        plt.tight_layout()
        plt.show()

# Example usage
df = sns.load_dataset('titanic')
eda = TitanicEDA(df)

# Save to Excel
eda.save_to_excel(r'D:\Python\Exploratory Data Analysis\Titanic\Titanic.xlsx')

# Display basic info
eda.basic_info()

# Check missing values and duplicates
eda.check_missing_duplicates()

# Clean data
eda.clean_data()

# Create age group column
eda.create_age_group()

# Display value counts
eda.display_value_counts('sex')

# Univariate analysis
eda.univariate_analysis()

# Bivariate analysis
eda.bivariate_analysis()