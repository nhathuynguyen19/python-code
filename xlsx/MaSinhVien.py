import pandas as pd
from tabulate import tabulate as tb

df = pd.read_excel("/home/nhathuy/Downloads/MaSinhVien.xlsx", engine="openpyxl")

def truncate(val):
    return str(val)[:17] + "..." if isinstance(val, str) and len(val) > 20 else val

df = df.applymap(truncate)

print(tb(df, headers='keys', tablefmt='grid'))

markdown_table = tb(df, headers='keys', tablefmt='github')

with open("MaSinhVien.md", "w", encoding='utf-8') as f:
    f.write(markdown_table)

print("Da luu vao MaSinhVien.md")