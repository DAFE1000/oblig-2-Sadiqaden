import math
import matplotlib.pyplot as plt

# Funksjonen fra oppgaven
def f(x):
    return math.exp(-x / 4) * math.atan(x)

# Likningen vi skal løse numerisk: phi(x) = 0
def phi(x):
    return math.atan(x) - 4 / (x**2 + 1)

# Enkel halveringsmetode
a = 1.0
b = 2.0

# Sjekker at vi faktisk har fortegnsskifte
if phi(a) * phi(b) > 0:
    raise ValueError("Ingen rot garantert i intervallet [a, b].")

tol = 1e-10

while b - a > tol:
    m = (a + b) / 2
    if phi(a) * phi(m) <= 0:
        b = m
    else:
        a = m

x_topp = (a + b) / 2
y_topp = f(x_topp)

print(f"x-koordinat til toppunkt: {x_topp:.10f}")
print(f"y-koordinat til toppunkt: {y_topp:.10f}")
print(f"Toppunkt avrundet til fire desimaler: ({x_topp:.4f}, {y_topp:.4f})")

# Lager punkter til plottet
x_values = [i / 100 for i in range(-200, 601)]   # fra -2.00 til 6.00
y_values = [f(x) for x in x_values]

# Plotter funksjonen
plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, label=r"$f(x)=e^{-x/4}\arctan(x)$")
plt.scatter([x_topp], [y_topp], label=f"Toppunkt ({x_topp:.4f}, {y_topp:.4f})")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot av funksjonen med toppunkt")
plt.grid(True)
plt.legend()
plt.tight_layout()

# Lagrer plottet i repoet
plt.savefig("plot.png", dpi=200)
plt.show()