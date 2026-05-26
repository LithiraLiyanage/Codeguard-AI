export const allowedExtensions = [".js", ".jsx", ".ts", ".tsx", ".py", ".java"];
export const getLanguageFromFile = (name = "") => { const lower = name.toLowerCase(); if ([".js", ".jsx", ".ts", ".tsx"].some((ext) => lower.endsWith(ext))) return "javascript"; if (lower.endsWith(".py")) return "python"; if (lower.endsWith(".java")) return "java"; return ""; };
export const isValidFile = (file) => { if (!file) return "File is required."; if (!allowedExtensions.some((ext) => file.name.toLowerCase().endsWith(ext))) return "Unsupported file type."; if (file.size > 1024 * 1024) return "File size must be less than 1MB."; return ""; };
export const isValidGithubUrl = (url) => /^https:\/\/github\.com\/[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+\/?$/.test(url);
