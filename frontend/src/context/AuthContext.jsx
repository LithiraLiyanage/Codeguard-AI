import React, { createContext, useContext, useState } from "react";
import api from "../services/api";
const AuthContext = createContext();
export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(JSON.parse(localStorage.getItem("codeguard_user") || "null"));
  const login = async (email, password) => { const { data } = await api.post("/auth/login", { email, password }); localStorage.setItem("codeguard_user", JSON.stringify(data)); setUser(data); };
  const register = async (name, email, password, confirmPassword) => { const { data } = await api.post("/auth/register", { name, email, password, confirmPassword }); localStorage.setItem("codeguard_user", JSON.stringify(data)); setUser(data); };
  const logout = () => { localStorage.removeItem("codeguard_user"); setUser(null); };
  return <AuthContext.Provider value={{ user, login, register, logout }}>{children}</AuthContext.Provider>;
};
export const useAuth = () => useContext(AuthContext);
