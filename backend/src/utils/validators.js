const allowedExtensions = [".js", ".jsx", ".ts", ".tsx", ".py", ".java"];
const languageFromExtension = (filename = "") => {
  const lower = filename.toLowerCase();
  if ([".js", ".jsx", ".ts", ".tsx"].some(ext => lower.endsWith(ext))) return "javascript";
  if (lower.endsWith(".py")) return "python";
  if (lower.endsWith(".java")) return "java";
  return null;
};
const isAllowedFile = (filename = "") => allowedExtensions.some(ext => filename.toLowerCase().endsWith(ext));
const isValidGithubUrl = (url = "") => /^https:\/\/github\.com\/[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+\/?$/.test(url);
module.exports = { allowedExtensions, languageFromExtension, isAllowedFile, isValidGithubUrl };
