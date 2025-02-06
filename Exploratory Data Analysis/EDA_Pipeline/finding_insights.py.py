def find_insights(df):
    print("Top Correlated Features:")
    print(df.corr().abs().unstack().sort_values(ascending=False)[:10])
