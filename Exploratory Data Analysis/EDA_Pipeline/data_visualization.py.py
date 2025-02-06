import matplotlib.pyplot as plt
import seaborn as sns

def univariate_analysis(df):
    for col in df.select_dtypes(include=[np.number]):
        plt.figure()
        sns.histplot(df[col], kde=True)
        plt.title(f"Univariate Analysis of {col}")
        plt.show()

def bivariate_analysis(df):
    sns.pairplot(df)
    plt.show()

def multivariate_analysis(df):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()
