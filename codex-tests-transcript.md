# Add sensor CSV byte tests

> add 2 pytest tests in the test file (I havent installed them on this environment yet just ignore it), both for checking the that sensors.py's functions load and save correctly. do this by checking that the file contents are eactly identical to the bytes for the 2 pairs of sensor 2 csv files.
> DO NOT CHECK THE `sensors.py` FILE, make NO mistakes

<details><summary>6 previous messages</summary>

> I’ll inspect the existing test file and the CSV paths to add exactly two byte-for-byte load/save tests. I’ll avoid opening or reading `sensors.py`.
>
> <details><summary>Explored 4 files, ran a command</summary>
>
> - Ran `Get-ChildItem -Force | Select-Object Name,Mode; rg --files -g '*test*' -g 'pytest.ini' -g 'pyproject.toml' -g 'conftest.py' -g 'data/*'`
>
> <details><summary>Explored 4 files</summary>
>
> - Read `./ASSIGNMENT4.md`
> - Read `./test_sensors.py`
> - Read `./main.py`
> - Read `./README.md`
>
> </details>
>
> </details>
>
> The assignment notes identify the available API as `load_sensor1` followed by `save_sensor2`, and map the example and small inputs to their corresponding Sensor 2 expected files. I’ll make the two tests generate outputs under `tmp_path` and compare the resulting bytes to those expected files.
>
> <details><summary>Edited a file, ran 3 commands</summary>
>
> - Ran `Get-Item data\sensor1_small.csv,data\sensor2_small.csv,data\sensor2_small_converted.csv,data\sensor1_example.csv,data\sensor2_example.csv,data\sensor2_converted.csv | Select-Object Name,Length; Get-FileHash data\sensor2_small.csv,data\sensor2_small_converted.csv,data\sensor2_example.csv,data\sensor2_converted.csv -Algorithm SHA256 | Select-Object Path,Hash`
> - Ran `Get-Content data\sensor1_small.csv; Get-Content data\sensor2_small.csv; Get-Content data\sensor2_small_converted.csv; Get-Content data\sensor2_example.csv; Get-Content data\sensor2_converted.csv`
> - Ran `$paths = @('data\sensor2_small.csv','data\sensor2_small_converted.csv','data\sensor2_example.csv','data\sensor2_converted.csv'); foreach ($path in $paths) { $bytes = [IO.File]::ReadAllBytes((Resolve-Path $path)); [PSCustomObject]@{File=$path; Length=$bytes.Length; LastBytes=([BitConverter]::ToString($bytes[([Math]::Max(0,$bytes.Length-8))..($bytes.Length-1)]))} }`
> - Wrote `./test_sensors.py` (+24 -2)
>
> </details>
>
> The two tests are in place. Each writes to pytest’s isolated `tmp_path` and compares the generated file’s raw bytes with its Sensor 2 fixture; I’m reviewing the diff now without running pytest.
>
> <details><summary>Explored a file, ran 2 commands</summary>
>
> <details><summary>Explored a file</summary>
>
> - Read `./test_sensors.py`
>
> </details>
>
> - Ran `git diff -- test_sensors.py`
>
> - Ran `rg -n '^def test_' test_sensors.py`
>
> </details>
</details>

Added two tests in [test_sensors.py](/C:/Users/3224313l/Desktop/BME-SKILLS-2/week4-V2/test_sensors.py:34). Each loads a Sensor 1 file, saves to `tmp_path`, and compares the output bytes with its expected Sensor 2 file.

I did not open `sensors.py` or run pytest. The existing small expected and converted CSVs have different line endings, so the byte-for-byte test will detect that difference.
