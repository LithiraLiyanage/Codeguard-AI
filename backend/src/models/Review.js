const mongoose = require("mongoose");
const issueSchema = new mongoose.Schema({ title:String, severity:{type:String, enum:["low","medium","high"], default:"low"}, line:Number, description:String, recommendation:String, safeFix:String }, { _id:false });
const smellSchema = new mongoose.Schema({ title:String, description:String, recommendation:String }, { _id:false });
const reviewSchema = new mongoose.Schema({
  user: { type: mongoose.Schema.Types.ObjectId, ref: "User", required: true },
  projectName: { type: String, default: "Untitled Project" },
  fileName: { type: String, default: "Untitled File" },
  language: { type: String, enum: ["javascript", "python", "java"], required: true },
  sourceType: { type: String, enum: ["paste", "file", "github"], required: true },
  githubUrl: String,
  codePreview: String,
  qualityScore: Number,
  maintainabilityScore: Number,
  complexityScore: Number,
  bugs: [issueSchema],
  securityIssues: [issueSchema],
  codeSmells: [smellSchema],
  refactorSuggestions: [String],
  bestPractices: [String],
  complexityExplanation: String,
  summary: String,
  improvedCode: String,
  repositorySummary: mongoose.Schema.Types.Mixed
}, { timestamps: true });
module.exports = mongoose.model("Review", reviewSchema);
