def get_matter(resistivity, length, area):
    resistance = resistivity * (length / area)
    print(f"Resistance of material is: ", resistance)
    return resistance


def get_ohms_law(voltage, current):
    resistance = current / voltage
    print(f"Resistance is: ", resistance)
    return resistance


if __name__ == "__main__":
    get_ohms_law(10, 15)