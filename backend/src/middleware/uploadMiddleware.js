const multer = require("multer");
const { isAllowedFile } = require("../utils/validators");
const storage = multer.diskStorage({ destination(req, file, cb) { cb(null, "src/uploads"); }, filename(req, file, cb) { cb(null, `${Date.now()}-${file.originalname}`); } });
const fileFilter = (req, file, cb) => isAllowedFile(file.originalname) ? cb(null, true) : cb(new Error("Unsupported file type. Allowed: .js, .jsx, .ts, .tsx, .py, .java"));
module.exports = multer({ storage, fileFilter, limits: { fileSize: Number(process.env.MAX_FILE_SIZE || 1048576) } });
