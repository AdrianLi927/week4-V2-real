"""Assignment 4: the checks. Run them with   python -m pytest   from this folder.

Two tests are enough: your small pair of files, and the given example pair.
How to fill this file:
  - one test function per check, its name starting with  test_
  - a docstring saying what goes in, what must come out, and where that
    expected value came from (written by hand, or the given example file)
  - body:  assert False, "body not written yet"  until the bodies are filled in,
    in a NEW chat that never sees sensors.py
  - put the prompt you used for the bodies in the PROMPT block below

A test that writes a file should write it into  tmp_path : put tmp_path in the
brackets of the test, and pytest gives that test a fresh, empty folder.
Example of the shape (fill in the body yourself):

    def test_example_converts_exactly(tmp_path):
        '''data/sensor1_example.csv, converted, must be identical to
        data/sensor2_example.csv (given with the assignment).'''
        assert False, "body not written yet"
"""
# PROMPT (final version used, for the test bodies):
# Add exactly two pytest tests for the small and example sensor 1 files. In
# each test, load with sensors.load_sensor1, save with sensors.save_sensor2
# into tmp_path at 15-second intervals, and assert the output bytes exactly
# match the corresponding expected Sensor 2 CSV file. Do not inspect sensors.py.
import pytest
import sensors
from pathlib import Path


DATA_DIR = Path(__file__).parent / "data"


def test_small_conversion_matches_sensor2_bytes(tmp_path):
    """The small Sensor 1 file must convert to the bytes in sensor2_small.csv."""
    output_path = tmp_path / "sensor2_small_converted.csv"
    readings = sensors.load_sensor1(str(DATA_DIR / "sensor1_small.csv"))
    sensors.save_sensor2(str(output_path), readings, 15)

    assert output_path.read_bytes() == (DATA_DIR / "sensor2_small.csv").read_bytes()


def test_example_conversion_matches_sensor2_bytes(tmp_path):
    """The example Sensor 1 file must convert to the bytes in sensor2_example.csv."""
    output_path = tmp_path / "sensor2_converted.csv"
    readings = sensors.load_sensor1(str(DATA_DIR / "sensor1_example.csv"))
    sensors.save_sensor2(str(output_path), readings, 15)

    assert output_path.read_bytes() == (DATA_DIR / "sensor2_example.csv").read_bytes()
