def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"year {year}: ${amount:.2f}")

def main():
    principal = float(input("Enter the initial amount: "))
    rate = float(input("Enter the annual rate of return (as a decimal, e.g., 0.05 for 5%): "))
    years = int(input("Enter the number of years: "))
    invest(principal, rate, years)

if __name__ == "__main__":
    main()
