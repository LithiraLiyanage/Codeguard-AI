const path = require("path");
const fs = require("fs-extra");
const simpleGit = require("simple-git");
const { v4: uuidv4 } = require("uuid");
const { languageFromExtension, isAllowedFile } = require("../utils/validators");
const { removeSafe } = require("../utils/fileUtils");
const ignoredDirs = ["node_modules", "dist", "build", ".git", "venv", "__pycache__", ".next"];
const collectFiles = async (dir, files = []) => {
  const entries = await fs.readdir(dir, { withFileTypes: true });
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) { if (!ignoredDirs.includes(entry.name)) await collectFiles(fullPath, files); }
    else if (entry.isFile() && isAllowedFile(entry.name)) files.push(fullPath);
  }
  return files;
};
const cloneAndCollect = async (githubUrl, maxFiles = 30) => {
  const tempRoot = path.join(__dirname, "..", "temp"); await fs.ensureDir(tempRoot);
  const repoPath = path.join(tempRoot, uuidv4());
  try {
    await simpleGit().clone(githubUrl, repoPath, ["--depth", "1"]);
    const selected = (await collectFiles(repoPath)).slice(0, maxFiles);
    const codeFiles = [];
    for (const filePath of selected) {
      const stats = await fs.stat(filePath);
      if (stats.size > Number(process.env.MAX_FILE_SIZE || 1048576)) continue;
      const content = await fs.readFile(filePath, "utf-8");
      if (content.includes("\u0000")) continue;
      codeFiles.push({ fileName: path.relative(repoPath, filePath), language: languageFromExtension(filePath), code: content });
    }
    return { repoPath, codeFiles };
  } catch (error) { await removeSafe(repoPath); throw error; }
};
module.exports = { cloneAndCollect };
