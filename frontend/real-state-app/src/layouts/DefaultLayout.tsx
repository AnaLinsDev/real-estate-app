import { Outlet, Link } from "react-router-dom";

export default function DefaultLayout() {
  return (
    <div style={{ display: "flex" }}>
      
      {/* MENU LATERAL */}
      <nav>
        <h2>Menu</h2>

        <ul style={{ listStyle: "none", padding: 0 }}>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/properties">Imóveis</Link></li>
          <li><Link to="/tenants">Inquilinos</Link></li>
          <li><Link to="/bills">Boletos</Link></li>
        </ul>
      </nav>

      {/* CONTEÚDO DAS PÁGINAS */}
      <main style={{ padding: "20px", flexGrow: 1 }}>
        <Outlet /> {/* Onde as páginas aparecem */}
      </main>
    </div>
  );
}
