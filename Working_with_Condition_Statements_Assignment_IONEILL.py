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

# Extract unique employee IDs, names, and wages
employee_ids = []
employee_names = []
hourly_wages = []
seen_ids = set()

i = 0
while i < len(raw_data):
    # Looks for valid patterns
    if (i + 2 < len(raw_data) and
        isinstance(raw_data[i], int) and
        isinstance(raw_data[i+1], str) and
        isinstance(raw_data[i+2], (int, float)) and
        not isinstance(raw_data[i+2], bool)):
        
        emp_id = raw_data[i]
        name = raw_data[i+1]
        wage = float(raw_data[i+2])
        
        # Only adds if this employee ID hasn't been seen before
        if emp_id not in seen_ids:
            employee_ids.append(emp_id)
            employee_names.append(name)
            hourly_wages.append(wage)
            seen_ids.add(emp_id)
        
        i += 3
    else:
        i += 1

# Calculate total hourly rate with 30% benefits and check budget
total_hourly_rate = [wage * 1.3 for wage in hourly_wages]

highest_total_pay = max(total_hourly_rate)
if highest_total_pay > 37.30:
    print(f"Budget Alert: Someone earns ${highest_total_pay:.2f}/hr with benefits — possible budget concern!")

# Find underpaid employees (pay between $28.15 and $30.65)
underpaid_salaries = []
for total in total_hourly_rate:
    if 28.15 <= total <= 30.65:
        underpaid_salaries.append(round(total, 2))

# Apply tiered raises and store in company_raises
company_raises = []
for wage in hourly_wages:
    if 22.0 <= wage <= 24.0:
        new_wage = wage * 1.05
    elif 24.0 < wage <= 26.0:
        new_wage = wage * 1.04
    elif 26.0 < wage <= 28.0:
        new_wage = wage * 1.03
    else:
        new_wage = wage * 1.02
    company_raises.append(round(new_wage, 2))

# Flags employees who earn under $25 per hour base, get less than 4% raise and have total pay with benefits under $32 per hour and appear more than once in the raw data
print("\nEmployees who may need special attention:")
for i in range(len(hourly_wages)):
    base_wage = hourly_wages[i]
    total_with_benefits = total_hourly_rate[i]
    new_wage = company_raises[i]
    raise_percent = (new_wage / base_wage - 1) * 100
    name = employee_names[i]

    if (base_wage < 25.0 and raise_percent < 4.0 and total_with_benefits < 32.0 and raw_data.count(name) > 1):
        print(f" → {name}: ${base_wage}/hr → ${new_wage} ({raise_percent:.1f}% raise) "
              f"— low pay + low raise + low total + duplicate entry in data")