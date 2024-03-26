import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class AutomatedEDA:
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None
        self.cat_columns = None
        self.num_columns = None

    def load_data(self):
        self.df = pd.read_excel(self.data_path)

    def explore_data(self):
        print("Head of the DataFrame:")
        print(self.df.head())
        print("\nTail of the DataFrame:")
        print(self.df.tail())
        print("\nShape of the DataFrame:")
        print(self.df.shape)
        print("\nColumns of the DataFrame:")
        print(self.df.columns)
        print("\nInformation about the DataFrame:")
        print(self.df.info())
        print("\nNumber of missing values:")
        print(self.df.isnull().sum())
        print("\nNumber of duplicated rows:")
        print(self.df.duplicated().sum())

    def remove_duplicates(self):
        self.df = self.df.drop_duplicates()

    def remove_column(self, column):
        self.df = self.df.drop(column, axis=1)

    def extract_datetime_features(self, column):
        self.df['Year'] = pd.DatetimeIndex(self.df[column]).year
        self.df['Month'] = pd.DatetimeIndex(self.df[column]).month

    def handle_missing_values(self):
        total_rows = len(self.df)
        for col in self.df.columns:
            missing_percent = (self.df[col].isnull().sum() / total_rows) * 100
            if missing_percent > 20:
                self.df = self.df.drop(columns=[col])
            elif missing_percent > 0:
                if self.df[col].dtype == 'object':
                    mode_value = self.df[col].mode()[0]
                    self.df[col].fillna(mode_value, inplace=True)
                else:
                    median_value = self.df[col].median()
                    self.df[col].fillna(median_value, inplace=True)

    def plot_histograms(self):
        for col in self.num_columns:
            plt.figure(figsize=(8, 6))
            sns.histplot(self.df[col], kde=True)
            plt.title(f'Histogram of {col}')
            plt.xlabel(col)
            plt.ylabel('Count')
            plt.show()

    def plot_countplots(self):
        for col in self.cat_columns:
            plt.figure(figsize=(10, 6))
            sns.countplot(x=col, data=self.df, order=self.df[col].value_counts().index)
            plt.title(f'Count Plot of {col}')
            plt.xlabel(col)
            plt.ylabel('Count')
            plt.xticks(rotation=45)
            plt.show()

    def plot_pairplot(self):
        plt.figure(figsize=(10, 10))
        sns.pairplot(self.df)
        plt.show()

    def plot_heatmap(self):
        plt.figure(figsize=(10, 8))
        corr = self.df[self.num_columns].corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        plt.title('Correlation Heatmap')
        plt.show()

    def analyze_target_columns(self, target_columns):
        for col in target_columns:
            plt.figure(figsize=(10, 6))
            sns.lineplot(x='Year', y=col, data=self.df)
            plt.title(f'Trend of {col} Over Years')
            plt.xlabel('Year')
            plt.ylabel(col)
            plt.show()

if __name__ == "__main__":
    # Example usage:
    eda = AutomatedEDA(r"D:\Python\10.EDA\Euromart\EuroMart_Stores_RETAIL_DATA.xlsx")
    eda.load_data()
    eda.remove_duplicates()
    eda.remove_column('Order ID')
    eda.extract_datetime_features('Order Date')

    # Handle missing values
    eda.handle_missing_values()

    # Extract categorical and numerical columns
    eda.cat_columns = eda.df.select_dtypes(include='object').columns.tolist()
    eda.num_columns = eda.df.select_dtypes(include=np.number).columns.tolist()

    eda.explore_data()
    eda.plot_histograms()
    eda.plot_countplots()
    eda.plot_pairplot()
    eda.plot_heatmap()

    # Analyze target columns
    target_columns = ['Sales', 'Profit']  # Specify the target columns you want to analyze
    eda.analyze_target_columns(target_columns)