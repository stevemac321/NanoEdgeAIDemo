import csv

INPUT_CSV = "normal_signals.csv"
OUTPUT_C = "training_data.c"
ARRAY_NAME = "training_data"
ELEMENTS_PER_SIGNAL = 141
MAX_RECORDS = 500  # Limit to 500 records

with open(INPUT_CSV, newline='') as csvfile:
    reader = csv.reader(csvfile)
    rows = [list(map(float, row)) for row in reader if len(row) == ELEMENTS_PER_SIGNAL]

# Trim to the first 500 records
rows = rows[:MAX_RECORDS]

with open(OUTPUT_C, "w") as cfile:
    cfile.write("#include <stddef.h>\n\n")
    cfile.write(f"float {ARRAY_NAME}[][141] = {{\n")

    for row in rows:
        formatted = ", ".join(f"{val:.6f}f" for val in row)
        cfile.write(f"    {{ {formatted} }},\n")

    cfile.write("};\n\n")
    cfile.write(f"size_t training_data_len = sizeof({ARRAY_NAME}) / sizeof({ARRAY_NAME}[0]);\n")
