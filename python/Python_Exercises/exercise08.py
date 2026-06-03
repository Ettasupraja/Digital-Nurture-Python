def salary_stats(salaries):
    if not salaries:
        return "Empty List"

    return f"Highest: {max(salaries)}, Lowest: {min(salaries)}"

salaries = [50000, 75000, 62000, 95000]

print(salary_stats(salaries))