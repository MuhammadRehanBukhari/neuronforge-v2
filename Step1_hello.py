# Step 7 - LIF Neuron with Plot
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
            voltage_trace.append(1.5)  # show spike as tall bar on plot
            voltage = reset
        else:
            voltage_trace.append(voltage)

    return voltage_trace, spike_times

# Run simulation
input_currents = [0.3] * 50
voltage_trace, spike_times = lif_neuron(input_currents)

# Plot
time = list(range(50))

plt.figure(figsize=(12, 5))
plt.plot(time, voltage_trace, color="blue", label="Membrane Voltage")
plt.axhline(y=1.0, color="red", linestyle="--", label="Threshold = 1.0")
plt.scatter(spike_times, [1.5] * len(spike_times), color="orange", zorder=5, label="Spikes")
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (a.u.)")
plt.title("LIF Neuron - Membrane Voltage Over Time")
plt.legend()
plt.tight_layout()
plt.savefig("lif_neuron.png")
plt.show()
print("Plot saved as lif_neuron.png")