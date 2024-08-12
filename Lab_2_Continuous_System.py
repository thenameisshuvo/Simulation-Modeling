import math

def main():
    # Initial data
    time = list(range(16))
    xb = [100, 110, 120, 129, 140, 149, 158, 168, 179, 188, 198, 209, 219, 226, 234, 240]
    yb = [0, 3, 6, 10, 15, 20, 26, 32, 37, 34, 30, 27, 23, 19, 16, 14]

    # Initialize arrays
    xf = [0] * 17  # One extra element for the next position
    yf = [0] * 17  # One extra element for the next position

    # Get user's initial position and speed
    xf[0] = float(input("Enter Fighter's Initial Position x: "))
    yf[0] = float(input("Enter Fighter's Initial Position y: "))
    S = int(input("\nEnter the Fighter speed: "))

    # Initialize arrays for calculations
    sin = [0] * 16
    cos = [0] * 16
    dist = [0] * 16

    for i in range(16):
        dist[i] = math.sqrt((yb[i] - yf[i]) ** 2 + (xb[i] - xf[i]) ** 2)
        sin[i] = (yb[i] - yf[i]) / dist[i]
        cos[i] = (xb[i] - xf[i]) / dist[i]
        xf[i+1] = xf[i] + S * cos[i]
        yf[i+1] = yf[i] + S * sin[i]

    # Print results
    print("\n\nxb[t] : ", xb)
    print("\n\nyb[t] : ", yb)
    print("\n\nxf[t] : ", xf[:16])  # Printing only up to the 16th element
    print("\n\nyf[t] : ", yf[:16])  # Printing only up to the 16th element
    print("\n\ndist[t] : ", dist)
    print("\n\nsin[t] : ", sin)
    print("\n\ncos[t] : ", cos)

if __name__ == "__main__":
    main()
