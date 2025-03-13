from fastapi import FastAPI, HTTPException
import pandas as pd
from typing import List

# Wczytanie przetworzonych danych
file_path = "/final_data_part2.csv"  # Możesz podmienić na właściwy plik

df = pd.read_csv(file_path)

app = FastAPI()

@app.get("/search")
def search_product(ean: str):
    result = df[df['EuropeanArticleNumber'].astype(str) == ean]
    
    if result.empty:
        raise HTTPException(status_code=404, detail="Produkt nie znaleziony")
    
    return result.to_dict(orient='records')[0]

# Uruchomienie aplikacji
# Komenda: uvicorn backend:app --reload
