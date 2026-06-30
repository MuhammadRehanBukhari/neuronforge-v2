# Step 8 - Multiple LIF neurons with different input strengths
import matplotlib.pyplot as plt

def lif_neuron(input_currents, threshold=1.0, leak=0.9, reset=0.0):
    voltage = 0.0
    voltage_trace = []
    spike_times = []

    for t in range(len(input_currents)):
        voltage = voltage * leak
        voltage = voltage + input_currents[t]

        if voltage >= threshold:
            spike_times.append(t)
            voltage_trace.append(1.5)
            voltage = reset
        else:
            voltage_trace.append(voltage)

    return voltage_trace, spike_times

# Three neurons with different input strengths
T = 100
weak_input   = [0.2] * T
medium_input = [0.3] * T
strong_input = [0.5] * T

v1, s1 = lif_neuron(weak_input)
v2, s2 = lif_neuron(medium_input)
v3, s3 = lif_neuron(strong_input)

time = list(range(T))

print("Weak neuron fired", len(s1), "times")
print("Medium neuron fired", len(s2), "times")
print("Strong neuron fired", len(s3), "times")

# Plot all three
fig, axes = plt.subplots(3, 1, figsize=(12, 8))

axes[0].plot(time, v1, color="blue")
axes[0].axhline(y=1.0, color="red", linestyle="--")
axes[0].set_title("Weak Input (0.2 nA) - " + str(len(s1)) + " spikes")
axes[0].set_ylabel("Voltage")

axes[1].plot(time, v2, color="green")
axes[1].axhline(y=1.0, color="red", linestyle="--")
axes[1].set_title("Medium Input (0.3 nA) - " + str(len(s2)) + " spikes")
axes[1].set_ylabel("Voltage")

axes[2].plot(time, v3, color="orange")
axes[2].axhline(y=1.0, color="red", linestyle="--")
axes[2].set_title("Strong Input (0.5 nA) - " + str(len(s3)) + " spikes")
axes[2].set_ylabel("Voltage")
axes[2].set_xlabel("Time (ms)")

plt.tight_layout()
plt.savefig("three_neurons.png")
plt.show()
print("Plot saved as three_neurons.png")