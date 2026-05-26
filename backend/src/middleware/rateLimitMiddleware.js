const rateLimit = require("express-rate-limit");
const analysisLimiter = rateLimit({ windowMs: 15 * 60 * 1000, limit: 40, message: { message: "Too many analysis requests. Please try again later." } });
module.exports = { analysisLimiter };
