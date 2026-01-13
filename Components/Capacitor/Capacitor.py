import math

#ErEo * (A/d)
def get_capacitance_by_material(permeability, area, distance):
    dielectriccon = 8.864 * 10e-12 #F/m
    capacitance = (permeability * dielectriccon * area) / distance
    print(f"Capacitance of materia is: {capacitance}")
    return capacitance

def get_capacitance_by_cv(charge, voltage):
    capacitance = charge / voltage
    print(f"Capacitance by CV: {capacitance} Farad")
    return capacitance

# i = C dv/dt

def get_capacitance_current(capacitance, dvoverdt):
    ic = capacitance * dvoverdt
    print(f"Capacitor Current: {ic}")
    return ic

def get_capacitive_reactance(frequency, capacitance):
    reactance = 1 / (2 * math.pi * frequency * capacitance)
    print(f"capacitive reactance is: ", reactance)
    return reactance

if __name__ == '__main__':
    get_capacitance_by_cv(0.5, 5)