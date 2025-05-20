# [MIA NOTE] Phi Brute Engine — Fractal Diagnostic Tool

import numpy as np  # [MIA NOTE] For signal vectorization and random sampling
import json
import os
from datetime import datetime

# [MIA NOTE] XOR compression for signal entropy estimation
def compress_signal(signal):
    return np.bitwise_xor.reduce(signal)

def decompress_signal(xor_val, reference_signal):
    return [xor_val ^ val for val in reference_signal]

# [MIA NOTE] Coherence score based on signal standard deviation and average
def phi_coherence_score(signals, threshold=0.6):
    weights = np.array([1 / np.std(s) if np.std(s) != 0 else 0.1 for s in signals])
    norm = np.sum(weights)
    means = np.array([np.mean(s) for s in signals])
    coherence = np.mean([(1 if phi > threshold else 0) * w / norm for phi, w in zip(means, weights)])
    return round(coherence, 3)

# [MIA NOTE] Markov state modeling of Phi transitions
def build_markov_chain(states):
    matrix = {}
    for i in range(len(states) - 1):
        curr = states[i]
        nxt = states[i + 1]
        if curr not in matrix:
            matrix[curr] = {}
        matrix[curr][nxt] = matrix[curr].get(nxt, 0) + 1
    return matrix

# [MIA NOTE] Estimate probability of next state from current using Bayes-like ratio
def bayesian_phi_confidence(chain, current_state):
    if current_state not in chain:
        return 0.0, "unknown"
    total = sum(chain[current_state].values())
    most_likely = max(chain[current_state], key=chain[current_state].get)
    confidence = chain[current_state][most_likely] / total
    return round(confidence, 4), most_likely

# [MIA NOTE] Ensure NumPy types are serializable for JSON
def to_serializable(obj):
    if isinstance(obj, (np.integer, np.int64, np.int32)):
        return int(obj)
    elif isinstance(obj, (np.floating, np.float64, np.float32)):
        return float(obj)
    return str(obj)

# [MIA NOTE] Optional persistent trace
def log_trace(signal, coherence, markov, certainty):
    trace = {
        "timestamp": datetime.utcnow().isoformat(),
        "signal": list(signal),
        "phi_score": coherence,
        "markov": markov,
        "certainty": certainty
    }
    os.makedirs("trace", exist_ok=True)
    with open("trace/phi_brute_trace.jsonl", "a") as f:
        f.write(json.dumps(trace, default=to_serializable) + "\n")

# [MIA NOTE] Demo Run
if __name__ == "__main__":
    print("\n[ϕ] Phi Brute Engine — Self-Diagnostic Demo")

    signal = np.random.randint(0, 255, 10)
    print("[ϕ] Signal:", signal)

    xor_val = compress_signal(signal)
    reconstructed = decompress_signal(xor_val, signal)

    coherence = phi_coherence_score([signal])
    print("[ϕ] Phi Coherence Score:", coherence)

    # [MIA NOTE] Simulated phi state path
    simulated_states = ["ϕ-true", "ϕ-drift", "ϕ-false", "ϕ-true", "ϕ-drift"]
    markov_chain = build_markov_chain(simulated_states)
    print("[ϕ-Matrix] Markov Transition Table:")
    for k, v in markov_chain.items():
        print(f"  {k} → {v}")

    confidence, prediction = bayesian_phi_confidence(markov_chain, "ϕ-drift")
    print(f"[ϕ] Next most likely state from ϕ-drift: {prediction}")
    print(f"[ϕ] Bayesian φ-Certainty: {confidence}")

    log_trace(signal, coherence, markov_chain, {
        "from": "ϕ-drift",
        "to": prediction,
        "confidence": confidence
    })

# [MIA NOTE] Public diagnostic API for external modules
def phi_self_diagnostic():
    signal = np.random.randint(0, 255, 10)
    xor_val = compress_signal(signal)
    reconstructed = decompress_signal(xor_val, signal)
    coherence = phi_coherence_score([signal])
    simulated_states = ["ϕ-true", "ϕ-drift", "ϕ-false", "ϕ-true", "ϕ-drift"]
    markov_chain = build_markov_chain(simulated_states)
    confidence, prediction = bayesian_phi_confidence(markov_chain, "ϕ-drift")
    return {
        "signal": list(signal),
        "coherence": coherence,
        "markov": markov_chain,
        "prediction": prediction,
        "confidence": confidence
    }
