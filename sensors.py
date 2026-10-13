"""Assignment 4: convert heart-rate files from sensor 1 to sensor 2.

Definitions only: importing this file must print nothing.

The two function names and their parameters are FIXED (your tests will be
run automatically against them): do not rename them, do not change the
parameters. For each function:
  1. replace the placeholder PROMPT with the final prompt you sent, word for word;
  2. replace  raise NotImplementedError  with the body that came back.
"""

import csv
from decimal import Decimal

# PROMPT (final version used):
# Fill in `load_sensor1` and `save_sensor2` in `sensors.py`, view the `data/` folder for examples
# Do not fill in or run anything else like tests yet. Do not delete any comments, but you can add extra ones.
# Make no mistakes.
def load_sensor1(path: str) -> list[float]:
    """Return the heart rates in bpm from a sensor 1 file, as a list of floats,
    in file order. A dropped sample is returned as 0.0."""
    with open(path, newline="", encoding="utf-8") as sensor_file:
        content = (line for line in sensor_file if not line.lstrip().startswith("#"))
        rows = csv.DictReader(content)
        readings = []
        for row in rows:
            value = row["hr_bpm"]
            readings.append(0.0 if value is None or not value.strip() else float(value))
    return readings


# PROMPT (final version used):
# Fill in `load_sensor1` and `save_sensor2` in `sensors.py`, view the `data/` folder for examples
# Do not fill in or run anything else like tests yet. Do not delete any comments, but you can add extra ones.
# Make no mistakes.
def save_sensor2(path: str, readings_bpm: list[float|int], interval_s: float) -> None:
    """Write the heart rates (bpm) to a new file in the sensor 2 format,
    one reading every interval_s seconds, starting at 0."""
    interval = float(interval_s)
    if not interval.is_integer() or interval <= 0:
        raise ValueError("interval_s must be a positive whole number of seconds")

    interval = int(interval)
    with open(path, "w", newline="", encoding="utf-8") as sensor_file:
        writer = csv.writer(sensor_file, delimiter=";", lineterminator="\n")
        writer.writerow(("time", "HR [bpm]"))

        for index, reading in enumerate(readings_bpm):
            total_seconds = index * interval
            minutes, seconds = divmod(total_seconds, 60)
            timestamp = f"{minutes:02d}:{seconds:02d}"

            if reading == 0:
                formatted_reading = "NA"
            elif isinstance(reading, int):
                formatted_reading = f"{reading},0"
            else:
                decimal_text = format(Decimal(repr(reading)), "f")
                if "." not in decimal_text:
                    decimal_text += ".0"
                formatted_reading = decimal_text.replace(".", ",")

            writer.writerow((timestamp, formatted_reading))
