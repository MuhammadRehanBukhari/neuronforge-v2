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