from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

# Wczytanie danych z plików CSV
file_path1 = "/app/final_data_part1a1_1.csv"
file_path2 = "/app/final_data_part1a1_2.csv"
file_path3 = "/app/final_data_part1a2.csv"
file_path4 = "/app/final_data_part1b.csv"
file_path5 = "/app/final_data_part2.csv"

df1 = pd.read_csv(file_path1)
df2 = pd.read_csv(file_path2)
df3 = pd.read_csv(file_path3)
df4 = pd.read_csv(file_path4)
df5 = pd.read_csv(file_path5)

df = pd.concat([df1, df2, df3, df4, df5])

@app.get("/search")
def search_product(ean: str):
    result = df[df['EuropeanArticleNumber'].astype(str) == ean]
    if result.empty:
        raise HTTPException(status_code=404, detail="Produkt nie znaleziony")
    return result.to_dict(orient='records')[0]
