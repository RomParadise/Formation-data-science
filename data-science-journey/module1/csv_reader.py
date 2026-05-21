import csv
def column_mean(csv_path: str, column: str) -> float:

    """Return arithmetic mean of a numeric column in a CSV file.

    Raises:
        FileNotFoundError: if csv_path doesn't exist.
        KeyError: if column doesn't exist.
        ValueError: if column contains non-numeric values.
    """
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        total = 0.0
        count = 0
        for row in reader:
            if column not in row:
                raise KeyError(f"Column '{column}' not found in CSV.")
            try:
                value = float(row[column])
            except ValueError:
                raise ValueError(f"Non-numeric value '{row[column]}' in column '{column}'.")
            total += value
            count += 1
    if count == 0:
        raise ValueError(f"No numeric values found in column '{column}'.")
    return total / count 