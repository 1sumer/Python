def clean_data(df):
    print("Handling Missing Values")
    df.fillna(method='ffill', inplace=True)  # Forward Fill
    df.fillna(method='bfill', inplace=True)  # Backward Fill
    df.fillna(df.mean(), inplace=True)  # Mean Imputation
    df.fillna(df.median(), inplace=True)  # Median Imputation
    df.fillna(df.mode().iloc[0], inplace=True)  # Mode Imputation
    df.dropna(inplace=True)  # Drop rows with NaN

    print("Removing Duplicates")
    df.drop_duplicates(inplace=True)

    print("Standardizing Categorical Variables")
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.lower().str.strip()

    return df
