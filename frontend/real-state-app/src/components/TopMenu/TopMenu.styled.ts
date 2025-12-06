import styled from "styled-components";

export const AppBar = styled.header`
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background: #19d288ff;
  padding: 0 16px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.15);
  z-index: 1000;
`;

export const Toolbar = styled.nav`
  height: 64px;
  display: flex;
  align-items: center;
  gap: 20px;
  min-width: 0;      
  overflow: hidden;   
`;

export const Spacer = styled.div`
  flex-grow: 1;    
  min-width: 0;
`;

export const MenuButton = styled.a`
  color: white;
  text-decoration: none;
  font-size: 16px;
  padding: 6px 12px;
  border-radius: 6px;
  white-space: nowrap;  
  min-width: 0;   
  padding-right: 32px;

  transition: background 0.2s ease;

  &:hover {
    background: rgba(255, 255, 255, 0.15);
    color: rebeccapurple;
  }
`;
