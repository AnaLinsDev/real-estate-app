import { Outlet } from "react-router-dom";
import TopMenu from "../components/TopMenu/TopMenu"

export default function DefaultLayout() {
  return (
    <div style={{ display: "flex" }}>
      
      <TopMenu />

      {/* CONTEÚDO DAS PÁGINAS */}
      <main style={{ padding: "20px", flexGrow: 1 }}>
        <Outlet /> {/* Onde as páginas aparecem */}
      </main>
    </div>
  );
}
