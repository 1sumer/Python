import numpy as np

def handle_errors(df):
    print("Handling Negative Values")
    df[df < 0] = np.nan  # Replace negatives with NaN
    df.fillna(df.mean(), inplace=True)  # Fill NaN with mean
    
    print("Handling Outliers with Capping")
    for col in df.select_dtypes(include=[np.number]):
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        df[col] = np.where(df[col] < lower_bound, lower_bound, df[col])
        df[col] = np.where(df[col] > upper_bound, upper_bound, df[col])
    
    return df