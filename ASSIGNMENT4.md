# Assignment 4 — From sensor 1 to sensor 2

The ward is replacing its heart-rate sensor. Old recordings come from **sensor 1**; the new analysis software only reads the format of **sensor 2**. Your job: a small program that converts a sensor 1 file into a sensor 2 file — and the evidence that the conversion is exact.

Nothing is analysed or cleaned: every reading is copied across as it is. Only the **format** changes.

## The two formats

`data/sensor1_example.csv` and `data/sensor2_example.csv` are **the same recording**, written by the two sensors. Open both in VS Code and compare them line by line before you do anything else: every difference you find is something your program must do.

## The files you start from

| file | what to do with it |
|---|---|
| `sensors.py` | two functions with fixed names: `load_sensor1` reads a sensor 1 file, `save_sensor2` writes a sensor 2 file. Write a prompt for each, and put the bodies that come back under the signatures |
| `test_sensors.py` | your checks, with pytest |
| `main.py` | three lines: load the example, save it converted as `data/sensor2_converted.csv`, print a message |
| `data/` | the two example files; your own small files go here too |
| `README_template.md` | copy it to `README.md` and fill it in |

## What to do

1. **Set up.** Unzip into a new folder, open it in VS Code, create the `.venv`, select the interpreter, `python -m pip install pytest`. Run `python -m pytest`: it should say *no tests ran* — correct, you have not written any yet.
2. **Make one small pair of files by hand**, in `data/`: a sensor 1 file with 3 or 4 readings (include one dropped sample and one decimal value), and the sensor 2 file it **must** become. You wrote both, so you know the right answer before any code exists.
3. **Write the two prompts**, one in the `# PROMPT` block above each function in `sensors.py`. Every difference between the two formats should be decided in them. Put the bodies that come back under the signatures.
4. **Write two tests** in `test_sensors.py`:
   - your small sensor 1 file, converted, is identical to your small sensor 2 file;
   - `sensor1_example.csv`, converted, is identical to `sensor2_example.csv`.

   "Converted" means: load with `load_sensor1`, save with `save_sensor2` into `tmp_path`, then compare the text of the new file with the text of the expected file. You may ask an assistant for the test bodies — in a separate chat that never sees `sensors.py`.
5. Run `python -m pytest` until it says **2 passed**. Then run `main.py`.
6. **Fill in `README.md`** — a short list of the differences, and three questions to reflect on.

## Submit (on Moodle, before next Monday's lecture)

One zip of your folder, **without** `.venv`: `sensors.py`, `test_sensors.py`, `main.py`, `data/` (with your two hand-made files), `README.md`, and the **transcript** of your AI chats.

Submission is anonymous: put no name in any file.
