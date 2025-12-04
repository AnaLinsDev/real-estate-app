import './styles/App.css'
import { useEffect, useState } from "react";
import { propertiesApi } from "./api/propertiesApi.ts";
import type { Property } from './types/types.ts';


function App() {
  const [properties, setProperties] = useState<Property[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchProperties() {
      try {
        const data = await propertiesApi.getAll();
        setProperties(data);
      } catch (error) {
        console.error("Erro ao carregar propriedades:", error);
      } finally {
        setLoading(false);
      }
    }

    fetchProperties();
  }, []);

  if (loading) return <p>Loading properties...</p>;

  return (
    <div>
      <h1>Lista de Imóveis</h1>

      {properties.length === 0 && <p>No properties found.</p>}

      <ul>
        {properties.map((p) => (
          <li key={p.id}>
            <strong>{p.name}</strong> — {p.type}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
