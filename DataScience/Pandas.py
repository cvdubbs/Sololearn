import pandas as pd

series = pd.Series({'a': 1, 'b': 2, 'c':3})
print(series['a'])

wine_dict = {
    'red_wine': [3, 6, 5],
    'white_wine':[5, 0, 10]
}
sales = pd.DataFrame(wine_dict, index=["adam", "bob", "charles"])
print(sales['white_wine'])

#Exploring Dataframes
import pandas as pd

presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
                                  
print(presidents_df.head(n=3))
print(presidents_df.tail(n=3))
print(presidents_df.columns)
print(presidents_df.index)
print(presidents_df.info)
print(presidents_df.describe())
print(presidents_df.T)
print(presidents_df.sort_values(by='height'))
print(presidents_df.sort_values(by='height', ascending=False))
print(presidents_df.sort_values(by='height', ascending=False).head(n=3))