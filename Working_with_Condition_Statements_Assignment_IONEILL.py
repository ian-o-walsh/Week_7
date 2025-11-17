# Ian O'Neill
# IT-410
# Week 7 - Working with Condition Statements Assignment
# Professor Charnesky

# Original data from Excel export
raw_data = [
    1121, "Jackie Grainger", 22.22,
    1122, "Jignesh Thrakkar", 25.25,
    1127, "Dion Green", 28.75, False,
    24.32, 1132, "Jacob Gerber",
    "Sarah Sanderson", 23.45, 1137, True,
    "Brandon Heck", 1138, 25.84, True,
    1152, "David Toma", 22.65,
    23.75, 1157, "Charles King", False,
    "Jackie Grainger", 1121, 22.22, False,
    22.65, 1152, "David Toma"
]

# Extract unique employee info from the data
employee_ids = []
employee_names = []
hourly_wages = []

i = 0
while i < len(raw_data):
    value = raw_data[i]

    # Get employee ID
    if isinstance(value, int):
        if value not in employee_ids:
            employee_ids.append(value)

    # Get employee name
    elif isinstance(value, str) and value not in ["True", "False"]:
        if value not in employee_names:
            employee_names.append(value)

    # Get hourly wage (numbers with decimals)
    elif isinstance(value, float):
        if value not in hourly_wages:
            hourly_wages.append(value)

    i += 1

# Calculate total pay including 30% benefits
total_pay_with_benefits = [wage * 1.3 for wage in hourly_wages]

# Check for anyone over budget ($37.30 total is limit)
highest_total_pay = max(total_pay_with_benefits)
if highest_total_pay > 37.30:
    print(f"Budget Alert: Someone earns ${highest_total_pay:.2f}/hr with benefits — possible budget concern!")

# Find underpaid employees (pay between $28.15 and $30.65)
underpaid_employees = []
for total in total_pay_with_benefits:
    if 28.15 <= total <= 30.65:
        underpaid_employees.append(round(total, 2))

# Calculate new salary after company raise
salaries_after_raise = []
for wage in hourly_wages:
    if 22.0 <= wage <= 24.0:
        new_wage = wage * 1.05
    elif 24.0 < wage <= 26.0:
        new_wage = wage * 1.04
    elif 26.0 < wage <= 28.0:
        new_wage = wage * 1.03
    else:
        new_wage = wage * 1.02
    salaries_after_raise.append(round(new_wage, 2))

# Flags low-paid employees with <4% raise, total<32, and duplicate raw entries
print("\nEmployees who may need special attention:")
for i in range(len(hourly_wages)):
    base_wage = hourly_wages[i]
    total_with_benefits = total_pay_with_benefits[i]
    new_wage = salaries_after_raise[i]
    raise_percent = (new_wage / base_wage - 1) * 100
    name = employee_names[i] if i < len(employee_names) else "Name Missing"

    if (base_wage < 25.0 and 
        raise_percent < 4.0 and 
        total_with_benefits < 32.0 and 
        raw_data.count(name) > 1):
        print(f" → {name}: ${base_wage}/hr → ${new_wage} ({raise_percent:.1f}% raise) — low pay + low raise + duplicate entry")