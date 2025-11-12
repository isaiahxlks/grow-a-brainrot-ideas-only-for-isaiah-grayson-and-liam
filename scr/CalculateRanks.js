function calculateRanks(scores) {
  // Create an array of objects with original index and score
  const scored = scores.map((score, index) => ({ index, score }));

  // Sort descending by score
  scored.sort((a, b) => b.score - a.score);

  // Assign ranks with tie handling
  let rank = 1;
  let prevScore = null;
  let offset = 0;

  for (let i = 0; i < scored.length; i++) {
    if (scored[i].score !== prevScore) {
      rank = i + 1;
      prevScore = scored[i].score;
    } else {
      offset++;
    }
    scored[i].rank = rank;
  }

  // Restore original order
  scored.sort((a, b) => a.index - b.index);

  // Return ranks only or full info
  return scored.map(({ score, rank }) => ({ score, rank }));
}

// Example usage
const scores = [100, 90, 90, 80, 75, 60];
const ranked = calculateRanks(scores);
console.log(ranked);
[
  { score: 100, rank: 1 },
  { score: 90, rank: 2 },
  { score: 90, rank: 2 },
  { score: 80, rank: 4 },
  { score: 75, rank: 5 },
  { score: 60, rank: 6 }
]
