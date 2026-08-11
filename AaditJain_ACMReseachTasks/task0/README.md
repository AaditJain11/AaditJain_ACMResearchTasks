# Sneaky Log Cleaner

This repository contains my solution for **Task 0: Sneaky Log Cleaner**.

The idea is to take a block of raw log text and apply a few transformations to make it cleaner, easier to read, and more structured.

## What the code does

The `transform_logs()` function applies five transformations:

* Hides email addresses by replacing them with `[HIDDEN]`
* Converts timestamps from `DD/MM/YYYY HH:MM` into a more readable format
* Adds `[!]` to `ERROR` messages
* Adds `[?]` to `WARNING` messages
* Adds `[+]` to `SUCCESS` messages

## Repository Contents

```text
.
├── Task_0.py
└── README.md
```

`Task_0.py` contains the main function and allows the user to enter multiple lines of log data.

## How to Run

The project uses only Python's built-in `re` and `datetime` modules, so no additional packages are required.

It can be run using **Google Colab, VS Code, Jupyter Notebook, or any Python 3 compiler**.

To run it locally:

```bash
python Task_0.py
```

After running the program, enter the log text line by line. Press **Enter on an empty line** when you have finished entering the logs.

## Example

### Input

```text
User john@gmail.com logged in at 23/08/2025 14:05.
ERROR: Session timeout.
WARNING: Too many login attempts.
SUCCESS: User logged in successfully.
```

### Output

```text
User [HIDDEN] logged in at 23 August 2025, 02:05 PM.
[!] ERROR: Session timeout.
[?] WARNING: Too many login attempts.
[+] SUCCESS: User logged in successfully.
```

## Approach

I used **regular expressions** to find email addresses and timestamps, `datetime` to format the timestamps, and Python's `replace()` method to add simple flags to different types of log messages.
