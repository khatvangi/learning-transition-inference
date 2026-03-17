/**
 * Artificial Grammar definitions and string generation.
 *
 * Three FSA grammars of increasing complexity.
 * Each grammar generates grammatical strings and matched ungrammatical violations.
 */

const GRAMMARS = {
  easy: {
    name: "Easy (3-state)",
    states: ["S0", "S1", "S2"],
    start: "S0",
    accept: ["S2"],
    alphabet: ["M", "V", "X", "R"],
    transitions: {
      S0: { M: "S1", V: "S1", R: "S2" },
      S1: { X: "S1", R: "S2" },
      S2: {},
    },
    // human-readable rule: start with M/V (optional), any X's, end with R
    description: "Strings that optionally start with M or V, have any number of X's, and end with R",
    minLength: 1,
    maxLength: 6,
  },

  medium: {
    name: "Medium (5-state)",
    states: ["S0", "S1", "S2", "S3", "S4"],
    start: "S0",
    accept: ["S4"],
    alphabet: ["M", "V", "X", "R", "T"],
    transitions: {
      S0: { M: "S1", V: "S2" },
      S1: { X: "S3", R: "S3", T: "S4" },
      S2: { X: "S3", T: "S3" },
      S3: { V: "S3", R: "S4" },
      S4: {},
    },
    description: "Two-path grammar with M/V branching and convergence",
    minLength: 2,
    maxLength: 7,
  },

  hard: {
    name: "Hard (7-state)",
    states: ["S0", "S1", "S2", "S3", "S4", "S5", "S6"],
    start: "S0",
    accept: ["S6"],
    alphabet: ["M", "V", "X", "R", "T", "S"],
    transitions: {
      S0: { M: "S1", V: "S2" },
      S1: { X: "S3", S: "S3" },
      S2: { T: "S3", X: "S3" },
      S3: { V: "S4", R: "S4", S: "S6" },
      S4: { M: "S5", X: "S5", T: "S3" },
      S5: { R: "S6", S: "S6" },
      S6: {},
    },
    description: "Complex grammar with loops and multiple paths",
    minLength: 3,
    maxLength: 8,
  },
};

/**
 * generate all grammatical strings up to maxLength using BFS
 */
function generateAllStrings(grammar) {
  const results = [];
  const queue = [{ state: grammar.start, str: "" }];

  while (queue.length > 0) {
    const { state, str } = queue.shift();

    // check if accepting state
    if (grammar.accept.includes(state) && str.length >= grammar.minLength) {
      results.push(str);
    }

    // stop if max length reached
    if (str.length >= grammar.maxLength) continue;

    // explore transitions
    const trans = grammar.transitions[state] || {};
    for (const [letter, nextState] of Object.entries(trans)) {
      queue.push({ state: nextState, str: str + letter });
    }
  }

  return results;
}

/**
 * check if a string is grammatical
 */
function isGrammatical(grammar, str) {
  let state = grammar.start;
  for (const ch of str) {
    const trans = grammar.transitions[state] || {};
    if (!(ch in trans)) return false;
    state = trans[ch];
  }
  return grammar.accept.includes(state);
}

/**
 * generate an ungrammatical string by violating a grammatical one.
 * uses one of three violation types (matched for length).
 */
function generateViolation(grammar, grammaticalStr, rng) {
  const violationType = rng() < 0.33 ? "substitute" : rng() < 0.5 ? "insert" : "delete";

  if (violationType === "substitute" && grammaticalStr.length > 0) {
    // replace one letter with an illegal one at that position
    const pos = Math.floor(rng() * grammaticalStr.length);
    const currentLetter = grammaticalStr[pos];
    const otherLetters = grammar.alphabet.filter((l) => l !== currentLetter);
    if (otherLetters.length > 0) {
      const replacement = otherLetters[Math.floor(rng() * otherLetters.length)];
      const candidate = grammaticalStr.slice(0, pos) + replacement + grammaticalStr.slice(pos + 1);
      if (!isGrammatical(grammar, candidate)) return candidate;
    }
  }

  if (violationType === "insert" && grammaticalStr.length < grammar.maxLength) {
    // insert a random letter at a random position
    const pos = Math.floor(rng() * (grammaticalStr.length + 1));
    const letter = grammar.alphabet[Math.floor(rng() * grammar.alphabet.length)];
    const candidate = grammaticalStr.slice(0, pos) + letter + grammaticalStr.slice(pos);
    if (!isGrammatical(grammar, candidate)) return candidate;
  }

  if (violationType === "delete" && grammaticalStr.length > grammar.minLength) {
    // delete one letter
    const pos = Math.floor(rng() * grammaticalStr.length);
    const candidate = grammaticalStr.slice(0, pos) + grammaticalStr.slice(pos + 1);
    if (!isGrammatical(grammar, candidate)) return candidate;
  }

  // fallback: simple substitution of last character
  const lastChar = grammaticalStr[grammaticalStr.length - 1];
  const others = grammar.alphabet.filter((l) => l !== lastChar);
  const candidate = grammaticalStr.slice(0, -1) + others[Math.floor(rng() * others.length)];
  if (!isGrammatical(grammar, candidate)) return candidate;

  // worst case: reverse the string (almost certainly ungrammatical)
  return grammaticalStr.split("").reverse().join("");
}

/**
 * seeded random number generator (mulberry32)
 */
function createRng(seed) {
  let s = seed | 0;
  return function () {
    s = (s + 0x6d2b79f5) | 0;
    let t = Math.imul(s ^ (s >>> 15), 1 | s);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

/**
 * generate a balanced trial set for one phase.
 * returns array of {string, grammatical, source} objects.
 */
function generateTrialSet(grammar, nTrials, seed) {
  const rng = createRng(seed);
  const allGrammatical = generateAllStrings(grammar);

  if (allGrammatical.length === 0) {
    console.error("no grammatical strings generated for grammar:", grammar.name);
    return [];
  }

  const trials = [];
  const nGram = Math.ceil(nTrials / 2);
  const nUngram = nTrials - nGram;

  // grammatical trials — sample with replacement if needed
  for (let i = 0; i < nGram; i++) {
    const str = allGrammatical[Math.floor(rng() * allGrammatical.length)];
    trials.push({ string: str, grammatical: true, source: "fsa" });
  }

  // ungrammatical trials — generate violations
  for (let i = 0; i < nUngram; i++) {
    const base = allGrammatical[Math.floor(rng() * allGrammatical.length)];
    const violation = generateViolation(grammar, base, rng);
    trials.push({ string: violation, grammatical: false, source: "violation" });
  }

  // shuffle using fisher-yates
  for (let i = trials.length - 1; i > 0; i--) {
    const j = Math.floor(rng() * (i + 1));
    [trials[i], trials[j]] = [trials[j], trials[i]];
  }

  return trials;
}

// export for use in experiment.js
if (typeof module !== "undefined") {
  module.exports = { GRAMMARS, generateTrialSet, isGrammatical, generateAllStrings, createRng };
}
