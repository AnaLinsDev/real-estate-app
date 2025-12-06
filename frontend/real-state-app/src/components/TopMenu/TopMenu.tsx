import { Link } from "react-router-dom";
import {
  AppBar,
  Toolbar,
  Spacer,
  MenuButton
} from "./TopMenu.styled";

export default function TopMenu() {
  return (
    <AppBar>
      <Toolbar>
       

        <MenuButton as={Link} to="/">Home</MenuButton>

        <Spacer />
        
        <MenuButton as={Link} to="/properties">Imóveis</MenuButton>
        <MenuButton as={Link} to="/tenants">Inquilinos</MenuButton>
        
        <MenuButton as={Link} to="/bills">Contas</MenuButton>
        <MenuButton as={Link} to="/occupations">Vínculos</MenuButton>
        <MenuButton as={Link} to="/investments">Investimentos</MenuButton>
     
      </Toolbar>
    </AppBar>
  );
}
