import numpy as np
import matplotlib.pyplot as plt


# for a given specificity, sensitivity, and prevalence, calculate the probability that a person is infected, given that they had a positive test
# using the Bayes' formula we derive the following formula
def prob_infected_given_pos(spec, prev, sens):
    prob = sens * prev / (sens * prev + (100 - spec) * (100 - prev))
    return prob

specificity = [99, 99.9, 99.99, 99.999]

sensitivity = 99

prevalence = np.logspace(-3, np.log10(50), 100)

# Plot
plt.figure(figsize=(8, 5))


for spec in specificity:
    print(spec)
    P_infected_given_pos = prob_infected_given_pos(spec, prevalence, sensitivity)
    plt.plot(prevalence, P_infected_given_pos, label=f"Specificity = {spec}%")

# use log-scale for prevalence to better distinguish what happens for small values
plt.xscale("log")

# Plot labels and title
plt.xlabel("Prevalence (%)")
plt.ylabel("P(Infected | Positive)")
plt.title(f"P(Infected | Positive) vs. Prevalence")
plt.legend() 
plt.grid(True, linestyle="--", linewidth=0.5)
plt.show()