from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

# Wczytanie danych z plików CSV
file_path = "/app/final_data_part2.csv"

df1 = pd.read_csv(file_path)


df = pd.concat([df1])

@app.get("/search")
def search_product(ean: str):
    result = df[df['EuropeanArticleNumber'].astype(str) == ean]
    if result.empty:
        raise HTTPException(status_code=404, detail="Produkt nie znaleziony")
    return result.to_dict(orient='records')[0]
