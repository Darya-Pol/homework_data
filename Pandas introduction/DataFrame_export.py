import pandas as pd
melb_data = pd.read_csv('D:\Dasha\Универ\IDE\homework_data\data/melb_data.csv', sep=',')
print(melb_data['Bedroom'].mode())
