import pandas as pd
import import_libraries
import data_exploration as de
import data_cleaning as dc
import finding_errors as fe
import handling_errors as he
import data_visualization as dv
import finding_insights as fi
import summary_insights as si
import conclusion as con

def main():
    df = pd.read_csv('data.csv')  # Load your dataset
    
    de.explore_data(df)
    df = dc.clean_data(df)
    fe.find_errors(df)
    df = he.handle_errors(df)
    
    dv.univariate_analysis(df)
    dv.bivariate_analysis(df)
    dv.multivariate_analysis(df)
    
    fi.find_insights(df)
    
    print(si.summary_of_insights())
    print(con.generate_conclusion())

if __name__ == "__main__":
    main()
