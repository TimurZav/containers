import csv
import pandas as pd

sheets = ['ЯНВАРЬ', 'ФЕВРАЛЬ', 'МАРТ', 'АПРЕЛЬ', 'МАЙ', 'ИЮНЬ', 'ИЮЛЬ', 'АВГУСТ', 'СЕНТЯБРЬ', 'ОКТЯБРЬ', 'НОЯБРЬ', 'ДЕКАБРЬ']

for sheet in sheets:
    xlsx_data = pd.read_excel("/home/timur/PycharmWork/containers/statistics_2021/СТАТИСТИКА_2021.xls", sheet, index_col=None)
    csv_as_string = xlsx_data.to_csv(index=False)
    reader = csv.DictReader(csv_as_string.splitlines())

    df = pd.DataFrame(reader)
    df.to_csv(f'/home/timur/PycharmWork/containers/statistics_2021/csv/СТАТИСТИКА_2021_{sheet}.csv', index=False)
    print(df)

