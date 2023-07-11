import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

temperature_step = 0.4
temperatures_celsius = np.arange(-10, 0+temperature_step, temperature_step)
temperatures_kelvin = [T+273.15 for T in temperatures_celsius]

pressures_pascal = [
	259.98, 269.44, 279.04, 289.04, 299.44, 310.11, 321.04, 
	332.37, 344.10, 356.24, 368.64, 381.57, 394.90, 408.63, 422.76, 437.30, 
	452.36, 467.83, 487.96, 500.36, 517.29, 534.89, 552.89, 571.55, 590.75, 610.48
]

T1 = temperatures_kelvin.pop(0)
p1 = pressures_pascal.pop(0)

pressures_log = [np.log(p2/p1) for p2 in pressures_pascal]
temperatures_inv = [1/T2-1/T1 for T2 in temperatures_kelvin]

regression = scipy.stats.linregress(temperatures_inv, pressures_log)
R = 8.314
H = -R*regression.slope
err = R*regression.stderr
print(f"Fit: mx+b mit m = {regression.slope:.3E} und b = {regression.intercept:.3E}")
print(f"Molare Sublimationsenthalpie: H = {H:0.3E} +- {err:0.3E}")

fit_x = np.linspace(temperatures_inv[0], temperatures_inv[-1], 100)
fit_y = [regression.slope*x + regression.intercept for x in fit_x]
plt.plot(fit_x, fit_y, '--', label="Linearer fit")

plt.plot(temperatures_inv, pressures_log, 'o', label="Messdaten", markersize=5)
plt.xlabel("$\\frac{1}{T_2}-\\frac{1}{T_1} \\left[\\frac{1}{K}\\right]$")
plt.ylabel("$\\ln{\\left(\\frac{p_2}{p_1}\\right)}$")
plt.legend()
plt.title("Logarithmierte Drücke aufgetragen gegen Temperaturkehrwerte gemäß\nder Clausius-Clapeyron-Gleichung")
plt.savefig("Figure_1.png", dpi=300)
plt.show()
