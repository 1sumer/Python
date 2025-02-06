import numpy as np

def find_errors(df):
    print("Checking for Negative Values in Numerical Columns:")
    for col in df.select_dtypes(include=[np.number]):
        if (df[col] < 0).any():
            print(f"Column {col} has negative values.")
    
    print("Checking for Outliers")
    for col in df.select_dtypes(include=[np.number]):
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        outliers = df[(df[col] < (q1 - 1.5 * iqr)) | (df[col] > (q3 + 1.5 * iqr))]
        if not outliers.empty:
            print(f"Outliers detected in {col}")
