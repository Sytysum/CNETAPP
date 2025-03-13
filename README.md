# Produkt Szukaj (FastAPI + React)

Aplikacja webowa do wyszukiwania produktów po kodzie EAN.

## 📌 Instalacja backendu

1. Zainstaluj zależności:
   ```bash
   pip install fastapi uvicorn pandas
   ```

2. Uruchom backend:
   ```bash
   uvicorn backend_fastapi:app --host 0.0.0.0 --port 8000
   ```

## 📌 Instalacja frontendu

1. Przejdź do katalogu `frontend/` i zainstaluj zależności:
   ```bash
   npm install
   ```

2. Uruchom aplikację React:
   ```bash
   npm start
   ```

3. Otwórz w przeglądarce `http://localhost:3000`

## 📌 Wdrożenie na Railway

1. Skonfiguruj projekt w **Railway.app**
2. Ustaw zmienne środowiskowe:
   ```
   FILE_PATH = /app/final_data_part1a1_1.csv
   ```
3. Kliknij **Deploy**
