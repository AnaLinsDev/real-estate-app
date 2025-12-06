import "./styles/App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import TenantsPage from "./pages/Tenants/Tenants.tsx";
import PropertiesPage from "./pages/Properties/Properties.tsx";
import HomePage from "./pages/Home/Home.tsx";
import DefaultLayout from "./layouts/DefaultLayout.tsx";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<DefaultLayout />}>
          <Route path="/" element={<HomePage />} />
          <Route path="/properties" element={<PropertiesPage />} />
          <Route path="/tenants" element={<TenantsPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
