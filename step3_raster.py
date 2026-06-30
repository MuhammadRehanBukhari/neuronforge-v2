import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
dt = 1.0          # ms per timestep
T = 100.0         # total time in ms
steps = int(T / dt)

# LIF neuron parameters
tau_m   = 20.0    # membrane time constant (ms)
V_rest  = -65.0   # resting potential (mV)
V_thresh = -50.0  # spike threshold (mV)
V_reset = -65.0   # reset after spike (mV)
R       = 10.0    # membrane resistance (MOhm)

# 10 neurons, each gets a different input current
n_neurons = 10
I_inputs = np.linspace(1.5, 3.5, n_neurons)

# Storage
spike_times = [[] for _ in range(n_neurons)]
V = np.full(n_neurons, V_rest)

# Simulation loop
for t in range(steps):
    dV = (-(V - V_rest) + R * I_inputs) / tau_m * dt
    V += dV
    fired = V >= V_thresh
    for i in range(n_neurons):
        if fired[i]:
            spike_times[i].append(t * dt)
    V[fired] = V_reset

# Raster plot
fig, ax = plt.subplots(figsize=(10, 5))
for i, times in enumerate(spike_times):
    ax.scatter(times, [i] * len(times), s=6, c='black')

ax.set_xlabel("Time (ms)")
ax.set_ylabel("Neuron index")
ax.set_title("Spike Raster Plot -- 10 LIF Neurons with Varying Input Current")
ax.set_yticks(range(n_neurons))
plt.tight_layout()
plt.savefig("raster_plot.png", dpi=150)
plt.show()
print("Raster plot saved as raster_plot.png")
print("Neuron 0 gets lowest current, Neuron 9 gets highest.")
print("Higher current = higher firing rate. That is rate coding.")