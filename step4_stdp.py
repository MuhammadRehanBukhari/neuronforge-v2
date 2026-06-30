import numpy as np
import matplotlib.pyplot as plt

# STDP window parameters
A_plus  = 0.01    # max weight increase (LTP)
A_minus = 0.01    # max weight decrease (LTD)
tau_plus  = 20.0  # LTP time constant (ms)
tau_minus = 20.0  # LTD time constant (ms)

# Range of spike timing differences
# delta_t = t_pre - t_post
# positive = pre fired before post = LTP (synapse strengthens)
# negative = post fired before pre = LTD (synapse weakens)
delta_t = np.linspace(-50, 50, 1000)

delta_w = np.where(
    delta_t > 0,
    A_plus  * np.exp(-delta_t / tau_plus),
    -A_minus * np.exp(delta_t / tau_minus)
)

# Plot
fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(delta_t, delta_w, 'b-', linewidth=2)
ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax.axvline(0, color='red',   linewidth=0.8, linestyle='--', label='Spike coincidence')
ax.fill_between(delta_t, delta_w, 0,
                where=(delta_t > 0), alpha=0.15, color='green', label='LTP (pre before post)')
ax.fill_between(delta_t, delta_w, 0,
                where=(delta_t < 0), alpha=0.15, color='red',   label='LTD (post before pre)')

ax.set_xlabel("Delta t = t_pre - t_post (ms)")
ax.set_ylabel("Weight change (delta_w)")
ax.set_title("STDP Learning Window")
ax.legend()
plt.tight_layout()
plt.savefig("stdp_window.png", dpi=150)
plt.show()

print("STDP plot saved as stdp_window.png")
print("Green region: pre before post -> synapse strengthens (LTP)")
print("Red region:   post before pre -> synapse weakens (LTD)")
print("This is the biological learning rule SpiNNaker2 runs on its ARM cores.")