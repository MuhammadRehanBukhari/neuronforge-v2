# NeuronForge-v2

A from-scratch implementation of Leaky Integrate-and-Fire (LIF) neuron models
and a 3-layer Spiking Neural Network (SNN) in Python.

Built as preparation for research work at the Chair of Highly-Parallel
VLSI-Systems and Neuro-Microelectronics, TU Dresden (SpiNNaker2 / SpiNNcloud).

## What is inside

| File | Description |
|---|---|
| Step1_hello.py | Single LIF neuron simulation with membrane voltage plot |
| network.py | Three LIF neurons showing rate coding at different input strengths |
| snn_network.py | Full 3-layer SNN with synaptic weights and spike propagation |

## Concepts Implemented

- Leaky Integrate-and-Fire neuron model
- Membrane voltage dynamics with leak and reset
- Spike threshold detection
- Rate coding: firing frequency as a function of input strength
- Synaptic weight connections between neuron layers
- Excitatory synapses and weighted spike propagation

## Results

- Single LIF neuron fires regularly at 1 spike per 4ms under constant 0.3 nA input
- Rate coding demo: weak input 14 spikes, medium 25 spikes, strong 33 spikes per 100ms
- 3-layer SNN: spikes propagate from input through hidden to output layer


## PyNN Conceptual Model

PyNN is a simulator-independent Python API for defining spiking neural network models.
The same PyNN code can run on NEST, NEURON, Brian2, or SpiNNaker hardware without changes.
The SpiNNaker-specific backend is called sPyNNaker.

### How it maps to SpiNNaker2

When you run a PyNN model on SpiNNaker2 via sPyNNaker:
- Each `Population` is mapped to one or more ARM Cortex-M4 cores
- Each `Projection` becomes a routing table entry in the Network on Chip (NoC)
- Spike events travel as fixed-length packets across the NoC at hardware speed
- Synaptic weight updates (e.g. STDP) run as firmware on the ARM cores in real time

### Pseudo-code example (not executed -- for reference)

```python
import pyNN.spiNNaker as sim

sim.setup(timestep=1.0)  # ms

# Input population: 100 neurons firing at 10 Hz (Poisson process)
input_pop = sim.Population(100, sim.SpikeSourcePoisson(rate=10.0))

# Hidden population: 50 integrate-and-fire neurons
hidden_pop = sim.Population(50, sim.IF_curr_exp(
    tau_m=20.0,     # membrane time constant (ms)
    v_thresh=-50.0, # spike threshold (mV)
    v_rest=-65.0    # resting potential (mV)
))

# All-to-all connection with static synapses
sim.Projection(
    input_pop, hidden_pop,
    connector=sim.AllToAllConnector(),
    synapse_type=sim.StaticSynapse(weight=0.5, delay=1.0)
)

sim.run(1000)  # simulate 1000 ms
sim.end()
```

### Connection to this project

The LIF neurons implemented manually in Steps 1-5 of this project use the same
parameters as `IF_curr_exp` in PyNN (tau_m, v_thresh, v_rest, v_reset).
The STDP rule in step4_stdp.py mirrors the `STDPMechanism` available in sPyNNaker.
This project builds the foundational understanding before working with the full
PyNN/sPyNNaker stack on real SpiNNaker2 hardware.


## Relevance to SpiNNaker2

SpiNNaker2 simulates LIF neurons across 153 ARM Cortex-M4 cores per chip.
SpiNNcloud (launched April 2025, TU Dresden) scales this to 35,000 chips
and over 5 million cores. The neuron models implemented here are the
fundamental building blocks of that architecture.

## Tools

Python 3.14, NumPy, Matplotlib

## Author

Muhammad Rehan Bukhari
M.Sc. Nanoelectronic Systems, TU Dresden (2nd Semester)