import math
def get_inductor_value_of_material(relativep, permeability, turns, area, length):
    inductance = (relativep * permeability * turns * turns * area) / length
    print(f"Inductor Value: {inductance}")
    return inductance


def get_inductive_reactance(frequency, inductance):
    reactance = 1 / (2 * math.pi * frequency * inductance)
    print(f"inductive reactance is: ", reactance)
    return reactance

# VL = L di/dt
# Ic = C dv/dt

if __name__ == "__main__":
    get_inductive_reactance(5000, 0.00045)