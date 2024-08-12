import random

def random_num(lo, up):
    """Generate a random number between lo and up, inclusive."""
    return random.randint(lo, up)

def main():
    random.seed()  # Seed the random number generator

    # Get probabilities from the user
    try:
        fProb = float(input("Enter the probability for Forward (0-1): "))
        lProb = float(input("Enter the probability for Left (0-1): "))
        rProb = float(input("Enter the probability for Right (0-1): "))

        if not (0 <= fProb <= 1 and 0 <= lProb <= 1 and 0 <= rProb <= 1):
            raise ValueError("Probabilities must be between 0 and 1.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    # Get increment/decrement values and axes
    faxis = input("Enter for which axis you want to select for Forward (x // y): ").strip().lower()
    if faxis not in {'x', 'y'}:
        print("Invalid axis for Forward. Use 'x' or 'y'.")
        return
    try:
        fID = int(input("Enter the incrementation/decrementation value for Forward (1 // -1): "))
    except ValueError:
        print("Invalid input for Forward ID. Must be an integer.")
        return

    laxis = input("Enter for which axis you want to select for Left (x // y): ").strip().lower()
    if laxis not in {'x', 'y'}:
        print("Invalid axis for Left. Use 'x' or 'y'.")
        return
    try:
        lID = int(input("Enter the incrementation/decrementation value for Left (1 // -1): "))
    except ValueError:
        print("Invalid input for Left ID. Must be an integer.")
        return

    raxis = input("Enter for which axis you want to select for Right (x // y): ").strip().lower()
    if raxis not in {'x', 'y'}:
        print("Invalid axis for Right. Use 'x' or 'y'.")
        return
    try:
        rID = int(input("Enter the incrementation/decrementation value for Right (1 // -1): "))
    except ValueError:
        print("Invalid input for Right ID. Must be an integer.")
        return

    # Get starting positions and number of simulation steps
    try:
        x = int(input("Enter the starting position for x (0): "))
        y = int(input("Enter the starting position for y (0): "))
        step = int(input("Enter how many simulation steps: "))
    except ValueError:
        print("Invalid input. Starting positions and steps must be integers.")
        return

    # Calculate the number of random values needed
    Fn = int(fProb * 10)
    Rn = int(rProb * 10)
    Ln = int(lProb * 10)

    # Generate random values for Forward, Left, and Right
    Frand = [random_num(0, 9) for _ in range(Fn)]
    Rrand = [random_num(10, 19) for _ in range(Rn)]
    Lrand = [random_num(20, 29) for _ in range(Ln)]
    stepRand = [random.randint(0, 29) for _ in range(step)]

    # Simulation steps
    for j in range(step):
        rand_num = stepRand[j]

        if rand_num in Frand:
            if faxis == 'x':
                x += fID
            elif faxis == 'y':
                y += fID

        if rand_num in Rrand:
            if raxis == 'x':
                x += rID
            elif raxis == 'y':
                y += rID

        if rand_num in Lrand:
            if laxis == 'x':
                x += lID
            elif laxis == 'y':
                y += lID

        print(f"\n\nStep: {j} \n RandomNumber: {rand_num} \n PositionX: {x} \n PositionY: {y}\n\n")

    # Print results
    print("\n\nForward: [", " ".join(map(str, Frand)), "]")
    print("\n\nLeft: [", " ".join(map(str, Lrand)), "]")
    print("\n\nRight: [", " ".join(map(str, Rrand)), "]")
    print(f"\n\n(x,y) = ({x} , {y})\n")

if __name__ == "__main__":
    main()
