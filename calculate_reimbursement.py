import sys


def calculate_reimbursement(days: int, miles: float, receipts: float) -> float:
    reimburse = 100.0 * days
    return round(reimburse, 2)

if __name__ == "__main__":
    days = int(sys.argv[1])
    miles = float(sys.argv[2])
    receipts = float(sys.argv[3])

    result = calculate_reimbursement(days, miles, receipts)
    print(result)
