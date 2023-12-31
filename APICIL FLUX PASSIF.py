# -*- coding: utf-8 -*-
import pandas as pd

# Load both sheets from the Excel file into separate dataframes
file_path = r'C:\Users\rosee\Downloads\Contrôle_flux_passif.xlsx'

df1 = pd.read_excel(file_path, sheet_name='Suivi des flux', engine='openpyxl')
df2 = pd.read_excel(file_path, sheet_name='Data_outil_passif', engine='openpyxl')

# Rename columns in df2
header_mapping = {
    'Date opération': 'Impact Date',
    'Code du titre': 'Isin',
    'Entité juridique (libellé)': 'Client',
    'Type Operation (code)': 'Side',
    'Quantité': 'Quantity',
    'Montant Règlement': 'Amount'
}
df2.rename(columns=header_mapping, inplace=True)

# 将 "Quantité" 和 "Quantity" 四舍五入到两位小数
df1['Quantité'] = df1['Quantité'].round(2)
df2['Quantity'] = df2['Quantity'].round(2)

# Filtering based on criteria
df1_filtered = df1[(df1['Emetteur (libellé)'] == "Apicil asset management sa") & (df1['Type Operation (code)'] == "VENTE")]
df2_filtered = df2[(df2['Side'] == "RACHAT")]

# Extracting relevant columns to new dataframes
df1_relevant = df1_filtered[['Code du titre', 'Date opération', 'Quantité', 'Montant Règlement','Entité juridique (libellé)']].copy()
df2_relevant = df2_filtered[['Isin', 'Impact Date', 'Quantity', 'Amount','Client']].copy()

# Comparing the two dataframes
extra_in_df1 = df1_relevant.merge(df2_relevant, left_on=['Code du titre', 'Date opération', 'Quantité'], 
                                  right_on=['Isin', 'Impact Date', 'Quantity'], how='left', indicator=True).query('_merge == "left_only"').drop('_merge', axis=1)

extra_in_df2 = df2_relevant.merge(df1_relevant, left_on=['Isin', 'Impact Date', 'Quantity'], 
                                  right_on=['Code du titre', 'Date opération', 'Quantité'], how='left', indicator=True).query('_merge == "left_only"').drop('_merge', axis=1)

# Finding differences in Amount value
matched_rows = df1_relevant.merge(df2_relevant, left_on=['Code du titre', 'Date opération', 'Quantité'], 
                                  right_on=['Isin', 'Impact Date', 'Quantity'], how='inner')
amount_differs = matched_rows[matched_rows['Montant Règlement'] != matched_rows['Amount']]

# Save to Excel
with pd.ExcelWriter(file_path, engine='openpyxl', mode='a') as writer:
    extra_in_df1.to_excel(writer, sheet_name='Extra_in_suivi', index=False)
    extra_in_df2.to_excel(writer, sheet_name='Extra_in_passif', index=False)
    amount_differs[['Code du titre', 'Date opération', 'Quantité', 'Montant Règlement', 'Entité juridique (libellé)', 'Isin', 'Impact Date', 'Quantity', 'Amount', 'Client']].to_excel(writer, sheet_name='Amount_Differs', index=False)
