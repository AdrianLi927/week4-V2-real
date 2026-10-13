# Assignment 4 — sensor 1 to sensor 2

Tool used: VSCode Codex extension, GPT 6 Luna Extra High (github copilot was bugging out)

## The differences I found between the two formats

<!-- A short list: one line per difference, and what your program does about it. -->

- Header format 
- Time format
- Seperator symbol
- bpm decimal symbol
- bpm decimal support
- empty value symbol

## Reflection

<!-- A few sentences each. There are no wrong answers: honest ones are the good ones. -->

**1. What did the assistant decide that I had not asked for?** (Look at its replies and at the code.)

- correctly infering the above format differences by reading the 2 example data files
- opening the file in "w" (overwrite) mode
- raising `ValueError` for invalid intervals (if not positive whole number of seconds)
- sensor2's time format is in mm:ss, not hh:mm

- when I was writing up main I realised `interval_s` had to be filled in manually, I just assumed it was 15 since it was 15 the whole way in both the data sets

**2. What went wrong on the way, and what did I change?** (A test that failed, an error, a prompt I had to rewrite. If nothing went wrong, say what you checked to be sure.)
- I used plan mode for this, where the agent realised that since interval_s is a float (as given by the signature I was told not to change), and that the sensor 2 data only seemed to accept seconds in integers, some conversion would have to be done, which I had missed. I then told it to round to an integer then write since there were not yet examples of sensor2 taking floats as time intervals.
- I forgot to ask it to print the value after saving sensor2, I added it manaully.

**3. Would I trust a converted file from my program enough to hand it to the ward? Why, or why not?**

No, I havent tested this with real sensors yet and a lot of assumptions were made just based on the 2 files. Real data could contain a different error than NA that we wouldnt have picked up, due to the low sample size, which would mess the program up.

## The count

<!-- Paste the last line of  python -m pytest , e.g. "2 passed in 0.03s". -->
