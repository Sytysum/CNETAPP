import { useState } from "react";
import axios from "axios";

export default function App() {
  const [ean, setEan] = useState("");
  const [product, setProduct] = useState(null);
  const [error, setError] = useState(null);

  const searchProduct = async () => {
    try {
      setError(null);
      const response = await axios.get(`/search?ean=${ean}`);
      setProduct(response.data);
    } catch (err) {
      setError("Produkt nie znaleziony");
      setProduct(null);
    }
  };

  return (
    <div className="p-4 max-w-lg mx-auto">
      <h1 className="text-xl font-bold mb-4">Wyszukiwarka Produktów</h1>
      <input
        type="text"
        value={ean}
        onChange={(e) => setEan(e.target.value)}
        placeholder="Wpisz kod EAN"
        className="border p-2 w-full"
      />
      <button onClick={searchProduct} className="bg-blue-500 text-white p-2 mt-2 w-full">
        Szukaj
      </button>
      {error && <p className="text-red-500 mt-2">{error}</p>}
      {product && (
        <div className="mt-4 p-4 border">
          <h2 className="text-lg font-bold">{product.CategoryText1} - {product.CategoryText2}</h2>
          <p>{product.Description}</p>
          <p className="mt-2 font-semibold">Kod EAN: {product.EuropeanArticleNumber}</p>
          <p className="mt-2">{product.Text}</p>
          <a href={product.DatasheetUrl} target="_blank" className="text-blue-500">
            Karta produktu
          </a>
          <div className="mt-2">
            <img src={product.StandardImage} alt="Product Image" className="w-32" />
          </div>
        </div>
      )}
    </div>
  );
}
