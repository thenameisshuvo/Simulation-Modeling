import math
import random

def random_num(lo, up):
    num = random.uniform(lo, up)
    return num

def main():
    diameter = float(input("Enter the Diameter: "))
    radius = diameter / 2
    m = 0

    range_steps = int(input("\nEnter How many steps should be printed: "))
    
    R1 = [random_num(0, radius) for _ in range(range_steps)]
    R2 = [random_num(0, radius) for _ in range(range_steps)]
    
    check_value = [math.sqrt(radius * radius - R1[i] * R1[i]) for i in range(range_steps)]
    
    m_values = [0]
    n_values = [1]
    
    for i in range(range_steps):
        if R2[i] <= check_value[i]:
            m += 1
        m_values.append(m)
        n_values.append(i + 2)
    
    print("\nR1:", R1)
    print("\nR2:", R2)
    print("\nsqrt(1-R1^2):", check_value)
    print("\nM:", m_values[:-1])  # exclude the last value which is not needed
    print("\nN:", n_values[:-1])  # exclude the last value which is not needed
    
    pi_value = (m - 1) * 4 / (range_steps)
    print(f"\n\nThe value of pi is: {pi_value}\n\n")

if __name__ == "__main__":
    main()
