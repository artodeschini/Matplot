import pandas as pd


raw_data = {'names': ['Artur', 'Manu', 'Catia', 'Liria'],
            'jar_ir': [124, 112, 111, 234],
            'feb_ir': [100, 143, 145, 198],
            'march_ir': [2, 3, 7, 6]}

df = pd.DataFrame(raw_data, columns=['names', 'jar_ir', 'feb_ir', 'march_ir'])
df['total_ir'] = df['jar_ir'] + df['feb_ir'] + df['march_ir']

print(df)
