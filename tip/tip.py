def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    do = d.replace("$", "")
    return float(do)

def percent_to_float(p):
    po = p.replace("%", "")
    convert = float(po)/ 100
    return (convert)

main()
