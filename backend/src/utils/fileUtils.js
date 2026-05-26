const fs = require("fs-extra");
const removeSafe = async (path) => { try { await fs.remove(path); } catch (err) { console.error(`Cleanup failed: ${err.message}`); } };
module.exports = { removeSafe };
