# Step 9 - Spiking Neural Network with synaptic connections
# Input layer -> Hidden layer -> Output layer
import matplotlib.pyplot as plt
import numpy as np

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

# Simulation settings
T = 100  # total time steps in milliseconds

# --- INPUT LAYER ---
# 3 input neurons with different strengths
input_currents_1 = [0.4] * T
input_currents_2 = [0.2] * T
input_currents_3 = [0.5] * T

v_in1, s_in1 = lif_neuron(input_currents_1)
v_in2, s_in2 = lif_neuron(input_currents_2)
v_in3, s_in3 = lif_neuron(input_currents_3)

# --- SYNAPTIC WEIGHTS ---
# How strongly each input neuron connects to the hidden neuron
# Positive weight = excitatory (pushes voltage up)
# Negative weight = inhibitory (pushes voltage down)
w1 = 0.6   # input 1 -> hidden
w2 = 0.3   # input 2 -> hidden
w3 = 0.5   # input 3 -> hidden

# --- HIDDEN LAYER ---
# Build the input current for the hidden neuron from spikes of input layer
hidden_input = [0.0] * T

for t in range(T):
    current = 0.0
    if t in s_in1:
        current = current + w1
    if t in s_in2:
        current = current + w2
    if t in s_in3:
        current = current + w3
    hidden_input[t] = current

v_hidden, s_hidden = lif_neuron(hidden_input, threshold=0.8)

# --- OUTPUT LAYER ---
# Output neuron receives spikes from hidden neuron
w_hidden_out = 0.9
output_input = [0.0] * T

for t in range(T):
    if t in s_hidden:
        output_input[t] = w_hidden_out

v_output, s_output = lif_neuron(output_input, threshold=0.7)

# --- PRINT SUMMARY ---
print("Input neuron 1 fired:", len(s_in1), "times")
print("Input neuron 2 fired:", len(s_in2), "times")
print("Input neuron 3 fired:", len(s_in3), "times")
print("Hidden neuron fired:", len(s_hidden), "times")
print("Output neuron fired:", len(s_output), "times")

# --- PLOT ---
time = list(range(T))

fig, axes = plt.subplots(5, 1, figsize=(14, 12))

axes[0].plot(time, v_in1, color="blue")
axes[0].axhline(y=1.0, color="red", linestyle="--", alpha=0.5)
axes[0].set_title("Input Neuron 1 (0.4 nA) - " + str(len(s_in1)) + " spikes")
axes[0].set_ylabel("Voltage")

axes[1].plot(time, v_in2, color="blue")
axes[1].axhline(y=1.0, color="red", linestyle="--", alpha=0.5)
axes[1].set_title("Input Neuron 2 (0.2 nA) - " + str(len(s_in2)) + " spikes")
axes[1].set_ylabel("Voltage")

axes[2].plot(time, v_in3, color="blue")
axes[2].axhline(y=1.0, color="red", linestyle="--", alpha=0.5)
axes[2].set_title("Input Neuron 3 (0.5 nA) - " + str(len(s_in3)) + " spikes")
axes[2].set_ylabel("Voltage")

axes[3].plot(time, v_hidden, color="green")
axes[3].axhline(y=0.8, color="red", linestyle="--", alpha=0.5)
axes[3].set_title("Hidden Neuron (receives weighted spikes) - " + str(len(s_hidden)) + " spikes")
axes[3].set_ylabel("Voltage")

axes[4].plot(time, v_output, color="orange")
axes[4].axhline(y=0.7, color="red", linestyle="--", alpha=0.5)
axes[4].set_title("Output Neuron - " + str(len(s_output)) + " spikes")
axes[4].set_ylabel("Voltage")
axes[4].set_xlabel("Time (ms)")

plt.tight_layout()
plt.savefig("snn_network.png")
plt.show()
print("Plot saved as snn_network.png")