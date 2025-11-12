// 🧠 utils.js — General helpers + branded signal logic

// Format a number with commas (e.g., 1000 → "1,000")
function formatNumber(n) {
  return n.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

// Clamp a value between min and max
function clamp(value, min, max) {
  return Math.max(min, Math.min(max, value));
}

// Shuffle an array (Fisher-Yates)
function shuffle(array) {
  let a = array.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

// Generate a branded signal hash from a string
function generateSignal(input) {
  let hash = 0;
  for (let i = 0; i < input.length; i++) {
    hash = (hash << 5) - hash + input.charCodeAt(i);
    hash |= 0;
  }
  return `sigil:${Math.abs(hash).toString(36)}`;
}

// Check if a signal is branded
function isBrandedSignal(signal) {
  return typeof signal === "string" && signal.startsWith("sigil:");
}

// Export for use in other files
module.exports = {
  formatNumber,
  clamp,
  shuffle,
  generateSignal,
  isBrandedSignal
};
