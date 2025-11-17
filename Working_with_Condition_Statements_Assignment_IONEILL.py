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
