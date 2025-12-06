import "./styles/App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import TenantsPage from "./pages/Tenants/Tenants.tsx";
import PropertiesPage from "./pages/Properties/Properties.tsx";
import HomePage from "./pages/Home/Home.tsx";
import DefaultLayout from "./layouts/DefaultLayout.tsx";
import OccupationPage from "./pages/Occupation/Occupation.tsx";
import BillsPage from "./pages/Bills/Bills.tsx";
import InvestmentsPage from "./pages/Investments/Investments.tsx";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<DefaultLayout />}>

          <Route path="/" element={<HomePage />} />

          <Route path="/properties" element={<PropertiesPage />} />
          <Route path="/tenants" element={<TenantsPage />} />

          <Route path="/occupations" element={<OccupationPage />} />
          <Route path="/bills" element={<BillsPage />} />
          <Route path="/investments" element={<InvestmentsPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
