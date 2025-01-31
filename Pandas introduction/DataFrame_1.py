import pandas as pd


def create_companyDF(income, expenses, years):
    dict_data = {'income': income, 'expenses': expenses}
    table = pd.DataFrame(dict_data, index=years)
    return table


def get_profit(df, year):
    try:
        rezn = df.loc[year, 'income'] - df.loc[year, 'expenses']
        return rezn
    except:
        return None
