const mongoose = require("mongoose");
const bcrypt = require("bcryptjs");
const userSchema = new mongoose.Schema({
  name: { type: String, required: true, trim: true, maxlength: 80 },
  email: { type: String, required: true, unique: true, lowercase: true, trim: true },
  password: { type: String, required: true, minlength: 6 },
  role: { type: String, enum: ["developer", "admin"], default: "developer" }
}, { timestamps: true });
userSchema.pre("save", async function(next) { if (!this.isModified("password")) return next(); this.password = await bcrypt.hash(this.password, await bcrypt.genSalt(10)); next(); });
userSchema.methods.matchPassword = function(password) { return bcrypt.compare(password, this.password); };
module.exports = mongoose.model("User", userSchema);
