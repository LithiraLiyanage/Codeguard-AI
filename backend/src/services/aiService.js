const axios = require("axios");
const analyzeCodeWithAI = async ({ language, code, fileName }) => {
  const { data } = await axios.post(`${process.env.AI_SERVICE_URL}/analyze-code`, { language, code, file_name: fileName || "" });
  return data;
};
const summarizeRepository = async (reviews) => {
  const { data } = await axios.post(`${process.env.AI_SERVICE_URL}/analyze-repository-summary`, { reviews });
  return data;
};
module.exports = { analyzeCodeWithAI, summarizeRepository };
