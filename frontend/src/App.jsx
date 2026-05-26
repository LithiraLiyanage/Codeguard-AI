import { Routes, Route, Navigate } from "react-router-dom";
import Navbar from "./components/Navbar";
import ProtectedRoute from "./components/ProtectedRoute";
import AdminRoute from "./components/AdminRoute";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import CodeAnalyzer from "./pages/CodeAnalyzer";
import FileAnalyzer from "./pages/FileAnalyzer";
import GitHubAnalyzer from "./pages/GitHubAnalyzer";
import ReviewHistory from "./pages/ReviewHistory";
import ReviewDetails from "./pages/ReviewDetails";
import AdminDashboard from "./pages/AdminDashboard";
function App() { return <div className="min-h-screen bg-slate-950 text-slate-100"><Navbar /><Routes><Route path="/" element={<Home />} /><Route path="/login" element={<Login />} /><Route path="/register" element={<Register />} /><Route path="/analyze" element={<ProtectedRoute><CodeAnalyzer /></ProtectedRoute>} /><Route path="/file-analyzer" element={<ProtectedRoute><FileAnalyzer /></ProtectedRoute>} /><Route path="/github-analyzer" element={<ProtectedRoute><GitHubAnalyzer /></ProtectedRoute>} /><Route path="/history" element={<ProtectedRoute><ReviewHistory /></ProtectedRoute>} /><Route path="/reviews/:id" element={<ProtectedRoute><ReviewDetails /></ProtectedRoute>} /><Route path="/admin" element={<AdminRoute><AdminDashboard /></AdminRoute>} /><Route path="*" element={<Navigate to="/" />} /></Routes></div>; }
export default App;
