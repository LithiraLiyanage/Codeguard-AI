const express = require("express");
const { getStats, getReviews, getUsers } = require("../controllers/adminController");
const { protect, adminOnly } = require("../middleware/authMiddleware");
const router = express.Router();
router.get("/stats", protect, adminOnly, getStats);
router.get("/reviews", protect, adminOnly, getReviews);
router.get("/users", protect, adminOnly, getUsers);
module.exports = router;
