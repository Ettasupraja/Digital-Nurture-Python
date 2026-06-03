def split_bill(total_bill, people):
    if total_bill <= 0 or people <= 0:
        return "Invalid Input"

    share = total_bill // people
    return f"Each person pays: {share}"

print(split_bill(1250, 4))