/**
 * EPT Human Experiment — trial logic, timing, and data collection.
 *
 * manages the experiment flow:
 *   consent → instructions → practice → learning → transfer → debrief → submit
 *
 * all timing uses performance.now() for sub-millisecond precision.
 * data is stored locally and submitted to backend at completion.
 */

class EPTExperiment {
  constructor(config) {
    this.condition = config.condition || "medium"; // easy, medium, hard
    this.participantId = config.participantId || this.generateId();
    this.prolificPid = config.prolificPid || null;

    // trial counts per phase
    this.nPractice = 10;
    this.nLearning = 100;
    this.nTransfer = 40;  // novel strings, no feedback
    this.nOldTest = 20;   // old strings, no feedback
    this.confidenceEvery = 10;

    // grammar
    this.grammar = GRAMMARS[this.condition];

    // generate trial sets with different seeds for novelty
    this.practiceTrials = generateTrialSet(this.grammar, this.nPractice, 1000);
    this.learningTrials = generateTrialSet(this.grammar, this.nLearning, 2000);
    this.transferTrials = generateTrialSet(this.grammar, this.nTransfer, 3000);
    this.oldTestTrials = this.selectOldStrings(this.learningTrials, this.nOldTest);

    // state
    this.phase = "consent"; // consent, instructions, practice, learning, transfer, oldtest, debrief, done
    this.currentTrialIndex = 0;
    this.currentTrials = [];

    // data collection
    this.data = {
      participant_id: this.participantId,
      prolific_pid: this.prolificPid,
      condition: this.condition,
      grammar_name: this.grammar.name,
      start_time: new Date().toISOString(),
      demographics: {},
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
    return "ept-" + Math.random().toString(36).substr(2, 9);
  }

  selectOldStrings(learningTrials, n) {
    // pick n strings from learning phase (seen before)
    const rng = createRng(4000);
    const shuffled = [...learningTrials].sort(() => rng() - 0.5);
    return shuffled.slice(0, n).map((t) => ({
      ...t,
      source: "old_retest",
    }));
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
        "Let's practice! You'll see letter strings and decide if they follow the hidden pattern. You'll get feedback on each answer.",
      learning:
        "Now the real task begins. Keep judging the strings. Press the AHA button whenever you feel you understand the pattern!",
      transfer:
        "Great work! Now you'll see NEW strings from the same pattern. This time, there's no feedback — just do your best.",
      oldtest:
        "Almost done! A few more strings to judge. No feedback.",
    };

    // this would update the DOM — implementation depends on HTML structure
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

    // check if confidence rating is needed
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
      source: trial.source,
      response: response,
      correct: correct,
      rt_ms: Math.round(rt * 100) / 100, // 0.01ms precision
      feedback_shown: showFeedback,
      timestamp: new Date().toISOString(),
    };

    this.data.trials.push(trialData);

    // confidence rating
    if (confidenceRating !== null) {
      this.data.confidence_trajectory.push({
        after_trial: this.totalTrialNum,
        rating: confidenceRating,
        timestamp: new Date().toISOString(),
      });
    }

    // emit for UI feedback
    this.emit("trial-result", {
      correct,
      showFeedback,
      grammatical: trial.grammatical,
    });

    this.currentTrialIndex++;

    // auto-advance to next trial after brief delay
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
    // generate completion code
    const code = "EPT-" + Math.random().toString(36).substr(2, 6).toUpperCase();
    this.data.completion_code = code;
    this.data.end_time = new Date().toISOString();

    // compute summary stats
    this.data.summary = this.computeSummary();

    this.phase = "done";
    this.emit("experiment-complete", { code, data: this.data });
  }

  computeSummary() {
    const learning = this.data.trials.filter((t) => t.phase === "learning");
    const transfer = this.data.trials.filter((t) => t.phase === "transfer");
    const oldtest = this.data.trials.filter((t) => t.phase === "oldtest");

    const acc = (trials) =>
      trials.length > 0 ? trials.filter((t) => t.correct).length / trials.length : 0;

    const lastN = (trials, n) => trials.slice(-n);

    return {
      learning_accuracy: Math.round(acc(learning) * 1000) / 1000,
      learning_last20_accuracy: Math.round(acc(lastN(learning, 20)) * 1000) / 1000,
      transfer_accuracy: Math.round(acc(transfer) * 1000) / 1000,
      oldtest_accuracy: Math.round(acc(oldtest) * 1000) / 1000,
      n_aha_events: this.data.aha_events.length,
      first_aha_trial: this.data.aha_events.length > 0 ? this.data.aha_events[0].trial_num : null,
      total_trials: this.data.trials.length,
      median_rt_ms: this.medianRT(learning),
    };
  }

  medianRT(trials) {
    if (trials.length === 0) return 0;
    const rts = trials.map((t) => t.rt_ms).sort((a, b) => a - b);
    const mid = Math.floor(rts.length / 2);
    return Math.round(rts.length % 2 ? rts[mid] : (rts[mid - 1] + rts[mid]) / 2);
  }

  // ─────────────────────────────────────────────
  // event system (connects to UI)
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
      // fallback: save to localStorage
      localStorage.setItem("ept_backup_" + this.participantId, JSON.stringify(this.data));
      return false;
    }
  }
}

// export
if (typeof module !== "undefined") {
  module.exports = { EPTExperiment };
}
