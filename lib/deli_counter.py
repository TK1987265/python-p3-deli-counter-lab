def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        current_line = "The line is currently: "
        current_line += " ".join(f"{index + 1}. {name}" for index, name in enumerate(katz_deli))
        print(current_line)

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line.")

def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli.pop(0)}.")

if __name__ == "__main__":
    katz_deli = []

    take_a_number(katz_deli, "Ada")
    take_a_number(katz_deli, "Grace")
    take_a_number(katz_deli, "Kent")

    line(katz_deli)
    now_serving(katz_deli)
    line(katz_deli)

    take_a_number(katz_deli, "Matz")
    line(katz_deli)
    now_serving(katz_deli)
    line(katz_deli)
