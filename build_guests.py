#!/usr/bin/env python3
"""Reads guests.xlsx and generates guests.js for the seating chart website."""
import json, openpyxl, os

dir_path = os.path.dirname(os.path.abspath(__file__))
wb = openpyxl.load_workbook(os.path.join(dir_path, "guests.xlsx"))
sheet = wb.active

rows = []
for row in sheet.iter_rows(min_row=2, values_only=True):
    name, table = row[0], row[1]
    if name and table is not None:
        rows.append({"Guest": str(name).strip(), "Table": int(table)})

js = f"const guestData = {json.dumps(rows, indent=2)};\n"
out_path = os.path.join(dir_path, "guests.js")
with open(out_path, "w") as f:
    f.write(js)

print(f"Generated guests.js with {len(rows)} guests.")
