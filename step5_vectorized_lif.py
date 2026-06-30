import numpy as np
import matplotlib.pyplot as plt
import time

# -------------------------------------------------------
# PART A: Slow version -- Python loop over neurons
# -------------------------------------------------------

def simulate_loop(n_neurons, steps, dt, tau_m, V_rest, V_thresh, V_reset, R, I):
    V = np.full(n_neurons, V_rest)
    spike_count = np.zeros(n_neurons, dtype=int)
    for t in range(steps):
        for i in range(n_neurons):
            dV = (-(V[i] - V_rest) + R * I[i]) / tau_m * dt
            V[i] += dV
            if V[i] >= V_thresh:
                spike_count[i] += 1
                V[i] = V_reset
    return spike_count

# -------------------------------------------------------
# PART B: Fast version -- NumPy vectorized over neurons
# -------------------------------------------------------

def simulate_vectorized(n_neurons, steps, dt, tau_m, V_rest, V_thresh, V_reset, R, I):
    V = np.full(n_neurons, V_rest)
    spike_count = np.zeros(n_neurons, dtype=int)
    for t in range(steps):
        dV = (-(V - V_rest) + R * I) / tau_m * dt  # all neurons at once
        V += dV
        fired = V >= V_thresh
        spike_count += fired.astype(int)
        V[fired] = V_reset
    return spike_count

# -------------------------------------------------------
# Benchmark
# -------------------------------------------------------

n_neurons = 500
steps     = 5000
dt        = 1.0
tau_m     = 20.0
V_rest    = -65.0
V_thresh  = -50.0
V_reset   = -65.0
R         = 10.0
np.random.seed(42)
I = np.random.uniform(1.5, 3.5, n_neurons)

print(f"Simulating {n_neurons} neurons x {steps} timesteps...\n")

start = time.time()
spikes_loop = simulate_loop(n_neurons, steps, dt, tau_m, V_rest, V_thresh, V_reset, R, I)
t_loop = time.time() - start
print(f"Loop version:       {t_loop:.3f} s")

start = time.time()
spikes_vec = simulate_vectorized(n_neurons, steps, dt, tau_m, V_rest, V_thresh, V_reset, R, I)
t_vec = time.time() - start
print(f"Vectorized version: {t_vec:.3f} s")

speedup = t_loop / t_vec
print(f"\nSpeedup: {speedup:.1f}x")
print(f"Results match: {np.array_equal(spikes_loop, spikes_vec)}")

# -------------------------------------------------------
# Plot firing rates
# -------------------------------------------------------

firing_rate = spikes_vec / (steps * dt / 1000.0)  # Hz

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].bar(range(n_neurons), firing_rate, color='steelblue', width=1.0)
axes[0].set_xlabel("Neuron index")
axes[0].set_ylabel("Firing rate (Hz)")
axes[0].set_title("Firing Rate vs Neuron Index")

axes[1].scatter(I, firing_rate, s=8, c='steelblue', alpha=0.6)
axes[1].set_xlabel("Input current I (nA)")
axes[1].set_ylabel("Firing rate (Hz)")
axes[1].set_title("F-I Curve: Firing Rate vs Input Current")

plt.tight_layout()
plt.savefig("vectorized_benchmark.png", dpi=150)
plt.show()

print("\nPlot saved as vectorized_benchmark.png")
print("The F-I curve on the right is a classic neuroscience result.")