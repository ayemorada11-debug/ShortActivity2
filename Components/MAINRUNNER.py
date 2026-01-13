from Capacitor import Capacitor
from Inductor import Inductor
from Resistor import Resistor

while True:
    selector = input("Select Calculator : ")

    match selector.upper():
        case "CC_CV" :
            print("Calculating Capacitance")

            charge = float(input("Please enter charge: "))
            voltage = float(input("Please enter voltage: "))

            Capacitor.get_capacitance_by_cv(charge, voltage)

        case "R_OHM" :
            print("Calculating Resistance")

            current = float(input("Please enter current: "))
            voltage = float(input("Please enter voltage: "))

            Resistor.get_ohms_law(current, voltage)

        case "L_REAC":
            print("Inductive Reactant Calculator")

            freq = float(input("Please enter frequency (HZ): "))
            inductance = float(input("Please enter inductance (H): "))

            Inductor.get_inductive_reactance(freq, inductance)