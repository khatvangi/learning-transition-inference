# inference — domain-agnostic transition detection for learning curves
#
# this module detects transition signatures in ANY time-series of
# learning performance. it knows nothing about AGL, grokking, or EPT.
# it answers: did this trajectory change abruptly? how abruptly?
# did the change persist? do multiple channels agree?
#
# usage:
#   from inference import detect_transitions
#   result = detect_transitions(accuracy_series, confidence_series=None, rt_series=None)

from .changepoint import detect_changepoints, pelt, bocpd
from .psi import compute_psi, compute_psi_smooth
from .model_compare import fit_and_compare, ContinuousModel, ChangepointModel, HMMModel
from .classify import classify_learner
from .persistence import test_persistence
from .convergence import test_convergence
from .pipeline import detect_transitions
