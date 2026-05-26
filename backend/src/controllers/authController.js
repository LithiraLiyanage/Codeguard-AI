const User = require("../models/User");
const generateToken = require("../utils/generateToken");
const register = async (req, res) => {
  const { name, email, password } = req.body;
  const existing = await User.findOne({ email });
  if (existing) return res.status(400).json({ message: "Email is already registered." });
  const role = email === "admin@example.com" ? "admin" : "developer";
  const user = await User.create({ name, email, password, role });
  res.status(201).json({ _id: user._id, name: user.name, email: user.email, role: user.role, token: generateToken(user._id) });
};
const login = async (req, res) => {
  const { email, password } = req.body;
  const user = await User.findOne({ email });
  if (user && await user.matchPassword(password)) return res.json({ _id: user._id, name: user.name, email: user.email, role: user.role, token: generateToken(user._id) });
  res.status(401).json({ message: "Invalid email or password." });
};
const me = async (req, res) => res.json(req.user);
module.exports = { register, login, me };
