import random
import time

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def randomize(arr, n):
    random.seed(time.time())
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        swap(arr, i, j)

def main():
    demand = [0] * 4
    lead_time = [0] * 3
    demand_prob = [0.0] * 4
    lead_prob = [0.0] * 3

    RP1 = RP2 = days = 0

    demand = list(map(int, input("\n\nEnter the demand (4 demand values): ").split()))
    demand_prob = list(map(float, input("\n\nEnter the Probabilities for demand (4 values): ").split()))

    lead_time = list(map(int, input("\n\nEnter the Lead Time (3 lead times): ").split()))
    lead_prob = list(map(float, input("\n\nEnter the Probabilities for Lead Time (3 values): ").split()))

    RP1, RP2 = map(int, input("\n\nEnter the value of reorder points respectively: ").split())
    days = int(input("\n\nHow many days do you want to simulate the system: "))

    demand_nums = [int(days * prob) for prob in demand_prob]
    lead_nums = [int(days * prob) for prob in lead_prob]

    demand_list = []
    lead_list = []

    for i in range(4):
        demand_list.extend([demand[i]] * demand_nums[i])

    for i in range(3):
        lead_list.extend([lead_time[i]] * lead_nums[i])

    randomize(demand_list, len(demand_list))
    randomize(lead_list, len(lead_list))

    stock = [0] * days
    Cstock = [0] * days
    Ord1 = [0] * days
    DDate1 = [0] * days
    Ord2 = [0] * days
    DDate2 = [0] * days
    CDemand = [0] * days
    Shortage = [0] * days
    CShortage = [0] * days

    stock[0] = int(input("Enter the initial Stock: "))
    Cstock[0] = stock[0]
    CDemand[0] = demand_list[0]
    Shortage[0] = CShortage[0] = 0

    for i in range(days):
        if stock[i] > 5 and stock[i] <= 10:
            Ord1[i] = 15
            DDate1[i] = lead_list[i] + i
        elif stock[i] > 0 and stock[i] <= 5:
            Ord2[i] = 15
            DDate2[i] = lead_list[i] + i

        if stock[i] - demand_list[i] > 0:
            Shortage[i] = 0
            if i > 0:
                CShortage[i] = CShortage[i - 1] + Shortage[i]

    print("\n\nDemand: [", " ".join(map(str, demand_list)), "]")
    print("\n\nLead: [", " ".join(map(str, lead_list)), "]")

if __name__ == "__main__":
    main()
