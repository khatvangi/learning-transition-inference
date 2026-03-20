/**
 * AGL experiment — trial logic, timing, and data collection.
 *
 * flow: consent → instructions → EXPOSURE → practice → learning → transfer → oldtest → debrief
 *
 * exposure phase: show grammatical-only strings for passive study (classic Reber AGL).
 * participants memorize the strings without knowing there's a hidden rule.
 * then test phases probe whether they absorbed the pattern.
 *
 * quality controls:
 *   - 500ms minimum display before response buttons activate
 *   - 3 catch trials (obvious strings) during learning
 *   - quality flags in summary: streak, fast-rate, response bias
 *
 * all timing uses performance.now() for sub-millisecond precision.
 */

class EPTExperiment {
  constructor(config) {
    this.condition = config.condition || "medium";
    this.participantId = config.participantId || this.generateId();
    this.prolificPid = config.prolificPid || null;

    // trial counts per phase
    this.nExposure = 15;
    this.exposureDuration = 3000;
    this.nPractice = 10;
    this.nLearning = 100;
    this.nTransfer = 40;
    this.nOldTest = 20;
    this.confidenceEvery = 10;
    this.minResponseTime = 500; // ms — buttons disabled until this elapses

    // grammar
    this.grammar = GRAMMARS[this.condition];

    // generate exposure set: grammatical strings only, for passive study
    this.exposureStrings = this.generateExposureSet(this.nExposure, 500);

    // generate trial sets with different seeds
    this.practiceTrials = generateTrialSet(this.grammar, this.nPractice, 1000);
    this.learningTrials = this.insertCatchTrials(
      generateTrialSet(this.grammar, this.nLearning, 2000)
    );
    this.transferTrials = generateTrialSet(this.grammar, this.nTransfer, 3000);
    this.oldTestTrials = this.selectOldStrings(this.learningTrials, this.nOldTest);

    // state
    this.phase = "consent";
    this.currentTrialIndex = 0;
    this.currentTrials = [];
    this.exposureIndex = 0;

    // data collection
    this.data = {
      participant_id: this.participantId,
      prolific_pid: this.prolificPid,
      condition: this.condition,
      grammar_name: this.grammar.name,
      start_time: new Date().toISOString(),
      demographics: {},
      exposure_strings: [],
      exposure_timing: [],
      trials: [],
      aha_events: [],
      confidence_trajectory: [],
      debrief: {},
      completion_code: null,
    };

    this.trialStartTime = 0;
    this.totalTrialNum = 0;
  }

  generateId() {
    return "lti-" + Math.random().toString(36).substr(2, 9);
  }

  generateExposureSet(n, seed) {
    const rng = createRng(seed);
    const allGram = generateAllStrings(this.grammar);
    if (allGram.length === 0) return [];
    const strings = [];
    for (let i = 0; i < n; i++) {
      strings.push(allGram[Math.floor(rng() * allGram.length)]);
    }
    return strings;
  }

  selectOldStrings(learningTrials, n) {
    const rng = createRng(4000);
    // exclude catch trials from old-string pool
    const real = learningTrials.filter(t => !t.is_catch);
    const shuffled = [...real].sort(() => rng() - 0.5);
    return shuffled.slice(0, n).map((t) => ({
      ...t,
      source: "old_retest",
    }));
  }

  // ─────────────────────────────────────────────
  // catch trials — detect inattentive participants
  // ─────────────────────────────────────────────

  insertCatchTrials(trials) {
    // insert 3 catch trials at roughly trial 25, 55, 85
    const catchPositions = [25, 55, 85];
    const catches = this.generateCatchStrings();

    let offset = 0;
    for (let i = 0; i < catches.length && i < catchPositions.length; i++) {
      const pos = Math.min(catchPositions[i] + offset, trials.length);
      trials.splice(pos, 0, catches[i]);
      offset++;
    }
    return trials;
  }

  generateCatchStrings() {
    // catch trial 1: obviously ungrammatical (random letters not in alphabet)
    // catch trial 2: obviously ungrammatical (way too long, repeated character)
    // catch trial 3: obviously grammatical (exact exposure string)
    const alphabet = this.grammar.alphabet;
    const catches = [];

    // obvious non-grammatical: string of Zs (not in any grammar alphabet)
    catches.push({
      string: "ZZZZ",
      grammatical: false,
      source: "catch_obvious_wrong",
      is_catch: true,
    });

    // obvious non-grammatical: impossibly long repetition
    catches.push({
      string: alphabet[0].repeat(12),
      grammatical: false,
      source: "catch_obvious_wrong",
      is_catch: true,
    });

    // obvious grammatical: an exposure string they already saw
    if (this.exposureStrings.length > 0) {
      const str = this.exposureStrings[0];
      catches.push({
        string: str,
        grammatical: true,
        source: "catch_obvious_right",
        is_catch: true,
      });
    }

    return catches;
  }

  // ─────────────────────────────────────────────
  // exposure phase (passive study, no response needed)
  // ─────────────────────────────────────────────

  startExposure() {
    this.phase = "exposure";
    this.exposureIndex = 0;
    this.data.exposure_strings = [...this.exposureStrings];
    this.data.exposure_timing = [];
    this.lastExposureTime = performance.now();
    this.presentExposureString();
  }

  presentExposureString() {
    if (this.exposureIndex >= this.exposureStrings.length) {
      this.startPhase("practice");
      return;
    }

    const now = performance.now();
    if (this.exposureIndex > 0) {
      const actualDuration = now - this.lastExposureTime;
      this.data.exposure_timing.push({
        index: this.exposureIndex - 1,
        actual_ms: Math.round(actualDuration * 10) / 10,
        nominal_ms: this.exposureDuration,
      });
    }
    this.lastExposureTime = now;

    const str = this.exposureStrings[this.exposureIndex];
    this.emit("show-exposure", {
      string: str,
      index: this.exposureIndex,
      total: this.exposureStrings.length,
    });

    this.exposureIndex++;
    setTimeout(() => this.presentExposureString(), this.exposureDuration);
  }

  // ─────────────────────────────────────────────
  // phase management
  // ─────────────────────────────────────────────

  startPhase(phase) {
    this.phase = phase;
    this.currentTrialIndex = 0;

    switch (phase) {
      case "practice":
        this.currentTrials = this.practiceTrials;
        break;
      case "learning":
        this.currentTrials = this.learningTrials;
        break;
      case "transfer":
        this.currentTrials = this.transferTrials;
        break;
      case "oldtest":
        this.currentTrials = this.oldTestTrials;
        break;
    }

    this.showPhaseIntro(phase);
  }

  showPhaseIntro(phase) {
    const intros = {
      practice:
        "Now let's practice. You'll see letter strings and decide if they follow the same pattern as the ones you just studied. You'll get feedback on each answer.",
      learning:
        "Good. Now the main task begins. Keep classifying strings — you'll still get feedback. Press the AHA button whenever you feel you've figured out the pattern!",
      transfer:
        "Great work! Now you'll see NEW strings. This time there's no feedback — just use what you've learned.",
      oldtest:
        "Almost done! A few more strings to classify. No feedback.",
    };

    this.emit("phase-intro", { phase, message: intros[phase] });
  }

  // ─────────────────────────────────────────────
  // trial presentation and response
  // ─────────────────────────────────────────────

  presentTrial() {
    if (this.currentTrialIndex >= this.currentTrials.length) {
      this.advancePhase();
      return;
    }

    const trial = this.currentTrials[this.currentTrialIndex];
    this.trialStartTime = performance.now();
    this.totalTrialNum++;

    const needsConfidence =
      this.phase === "learning" &&
      this.totalTrialNum > 0 &&
      this.totalTrialNum % this.confidenceEvery === 0;

    this.emit("show-trial", {
      string: trial.string,
      trialNum: this.totalTrialNum,
      phase: this.phase,
      showFeedback: this.phase === "practice" || this.phase === "learning",
      needsConfidence,
      minResponseTime: this.minResponseTime,
    });
  }

  recordResponse(response, confidenceRating = null) {
    const rt = performance.now() - this.trialStartTime;
    const trial = this.currentTrials[this.currentTrialIndex];
    const correct = (response === "grammatical") === trial.grammatical;
    const showFeedback = this.phase === "practice" || this.phase === "learning";

    const trialData = {
      trial_num: this.totalTrialNum,
      phase: this.phase,
      string: trial.string,
      grammatical: trial.grammatical,
      source: trial.source || "fsa",
      is_catch: trial.is_catch || false,
      response: response,
      correct: correct,
      rt_ms: Math.round(rt * 100) / 100,
      feedback_shown: showFeedback,
      timestamp: new Date().toISOString(),
    };

    this.data.trials.push(trialData);

    if (confidenceRating !== null) {
      this.data.confidence_trajectory.push({
        after_trial: this.totalTrialNum,
        rating: confidenceRating,
        timestamp: new Date().toISOString(),
      });
    }

    this.emit("trial-result", {
      correct,
      showFeedback,
      grammatical: trial.grammatical,
    });

    this.currentTrialIndex++;
    setTimeout(() => this.presentTrial(), showFeedback ? 1000 : 500);
  }

  // ─────────────────────────────────────────────
  // aha button
  // ─────────────────────────────────────────────

  recordAha() {
    this.data.aha_events.push({
      trial_num: this.totalTrialNum,
      phase: this.phase,
      timestamp: new Date().toISOString(),
      rt_since_trial_start: Math.round((performance.now() - this.trialStartTime) * 100) / 100,
    });
    this.emit("aha-recorded", { count: this.data.aha_events.length });
  }

  // ─────────────────────────────────────────────
  // phase transitions
  // ─────────────────────────────────────────────

  advancePhase() {
    const order = ["practice", "learning", "transfer", "oldtest", "debrief"];
    const current = order.indexOf(this.phase);
    if (current < order.length - 1) {
      this.startPhase(order[current + 1]);
    } else {
      this.finishExperiment();
    }
  }

  recordDebrief(debriefData) {
    this.data.debrief = {
      ...debriefData,
      timestamp: new Date().toISOString(),
    };
    this.finishExperiment();
  }

  // ─────────────────────────────────────────────
  // completion
  // ─────────────────────────────────────────────

  finishExperiment() {
    const code = "LTI-" + Math.random().toString(36).substr(2, 6).toUpperCase();
    this.data.completion_code = code;
    this.data.end_time = new Date().toISOString();
    this.data.summary = this.computeSummary();
    this.data.quality_flags = this.computeQualityFlags();
    this.phase = "done";
    this.emit("experiment-complete", { code, data: this.data });
  }

  computeSummary() {
    const learning = this.data.trials.filter((t) => t.phase === "learning" && !t.is_catch);
    const transfer = this.data.trials.filter((t) => t.phase === "transfer");
    const oldtest = this.data.trials.filter((t) => t.phase === "oldtest");
    const catches = this.data.trials.filter((t) => t.is_catch);

    const acc = (trials) =>
      trials.length > 0 ? trials.filter((t) => t.correct).length / trials.length : 0;
    const lastN = (trials, n) => trials.slice(-n);

    return {
      n_exposure_strings: this.nExposure,
      learning_accuracy: Math.round(acc(learning) * 1000) / 1000,
      learning_last20_accuracy: Math.round(acc(lastN(learning, 20)) * 1000) / 1000,
      transfer_accuracy: Math.round(acc(transfer) * 1000) / 1000,
      oldtest_accuracy: Math.round(acc(oldtest) * 1000) / 1000,
      catch_accuracy: Math.round(acc(catches) * 1000) / 1000,
      n_catch_trials: catches.length,
      n_catch_correct: catches.filter((t) => t.correct).length,
      n_aha_events: this.data.aha_events.length,
      first_aha_trial: this.data.aha_events.length > 0 ? this.data.aha_events[0].trial_num : null,
      total_trials: this.data.trials.length,
      median_rt_ms: this.medianRT(learning),
    };
  }

  computeQualityFlags() {
    const allTrials = this.data.trials;
    const rts = allTrials.map(t => t.rt_ms);
    const responses = allTrials.map(t => t.response);

    // flag 1: fast responses (< 500ms) — likely not reading
    const nFast = rts.filter(r => r < 500).length;
    const fastRate = nFast / rts.length;

    // flag 2: response bias — pressing same button > 80%
    const nGram = responses.filter(r => r === "grammatical").length;
    const biasRate = Math.max(nGram, responses.length - nGram) / responses.length;

    // flag 3: longest streak of identical responses
    let maxStreak = 1;
    let currentStreak = 1;
    for (let i = 1; i < responses.length; i++) {
      if (responses[i] === responses[i - 1]) {
        currentStreak++;
        maxStreak = Math.max(maxStreak, currentStreak);
      } else {
        currentStreak = 1;
      }
    }

    // flag 4: catch trial performance
    const catches = allTrials.filter(t => t.is_catch);
    const catchCorrect = catches.filter(t => t.correct).length;

    // overall quality assessment
    const flags = [];
    if (fastRate > 0.20) flags.push("high_fast_rate");
    if (biasRate > 0.80) flags.push("response_bias");
    if (maxStreak > 15) flags.push("long_streak");
    if (catches.length > 0 && catchCorrect === 0) flags.push("failed_all_catches");

    return {
      n_fast_responses: nFast,
      fast_rate: Math.round(fastRate * 1000) / 1000,
      response_bias: Math.round(biasRate * 1000) / 1000,
      max_same_response_streak: maxStreak,
      catch_correct: catchCorrect,
      catch_total: catches.length,
      flags: flags,
      flagged: flags.length > 0,
    };
  }

  medianRT(trials) {
    if (trials.length === 0) return 0;
    const rts = trials.map((t) => t.rt_ms).sort((a, b) => a - b);
    const mid = Math.floor(rts.length / 2);
    return Math.round(rts.length % 2 ? rts[mid] : (rts[mid - 1] + rts[mid]) / 2);
  }

  // ─────────────────────────────────────────────
  // event system
  // ─────────────────────────────────────────────

  emit(event, data) {
    if (this.onEvent) {
      this.onEvent(event, data);
    }
  }

  // ─────────────────────────────────────────────
  // data submission
  // ─────────────────────────────────────────────

  async submitData(apiUrl) {
    try {
      const response = await fetch(apiUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(this.data),
      });
      return response.ok;
    } catch (e) {
      console.error("data submission failed:", e);
      localStorage.setItem("lti_backup_" + this.participantId, JSON.stringify(this.data));
      return false;
    }
  }
}

if (typeof module !== "undefined") {
  module.exports = { EPTExperiment };
}
