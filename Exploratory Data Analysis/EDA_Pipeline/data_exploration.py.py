def explore_data(df):
    print("Data Shape:", df.shape)
    print("Column Names:", df.columns)
    print("Data Types:\n", df.dtypes)
    print("Missing Values:\n", df.isnull().sum())
    print("Duplicate Rows:", df.duplicated().sum())
    print("Basic Statistics:\n", df.describe(include='all'))
    print("Unique Values per Column:\n", df.nunique())
    print("Correlation Matrix:\n", df.corr())
