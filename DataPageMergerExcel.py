import pandas as pd

# Załadowanie danych z pliku Excel
df = pd.read_excel(r'OCR_VERSION.xlsx')
print(df.columns)

# Sortowanie danych wg 'SCIEZKA' i 'NUMER STRONY' dla upewnienia się, że kolejność jest zachowana
df = df.sort_values(by=['SCIEZKA', 'NUMER STRONY'])

# Użyjemy pivot_table, aby zrestrukturyzować DataFrame
df_pivot = df.pivot_table(index='SCIEZKA', 
                          aggfunc=lambda x: x,  # Agregacja bez zmian
                          columns=df.groupby('SCIEZKA').cumcount() + 1)  # Dodajemy numer strony jako sufiks do kolumn

# Spłaszczanie MultiIndex w kolumnach
df_pivot.columns = [f'{x}{y}' for x, y in df_pivot.columns]

# Resetowanie indeksu
df_pivot.reset_index(inplace=True)

# Opcjonalnie zapisujemy wyniki do Excela

# Zapis nowego DataFrame do pliku Excel
df_pivot.to_excel(r'EXCEL_TRANSFORM_VERSION.xlsx.xlsx', index=False)
