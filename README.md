# Educational Keylogger Project

This repository contains an educational project demonstrating how to create and disguise a keylogger for security awareness purposes. This project is intended solely for educational and ethical purposes to highlight potential security vulnerabilities and ways to mitigate them.

---

## Features

- **Keylogger Implementation**: Tracks and records keystrokes using Python.
- **Disguised Appearance**: The executable file is modified to appear as a `.pdf` using **Resource Hacker** and the Unicode **202E RTLO** character.
- **Data Logging**: Captured data is sent to **webhook.site** for anonymous viewing and processing.

---

## How It Works

### 1. Keylogger Creation
- Implemented using Python and the `keyboard` library.
- The script captures keystrokes and processes them for logging.

### 2. Disguising the Keylogger
- **Resource Hacker**: Used to modify the appearance of the executable file to mimic a `.pdf` file.
  - Resource Hacker enables editing resources within executables.
- **RTLO (Right-to-Left Override)**:
  - Unicode character `202E` reverses text direction, making filenames like `Blueprint_ann fdp.exe` appear as `Blueprint_ann exe.pdf`.

### 3. Storing Data
- Captured keystroke data is sent to **webhook.site** using event-driven API calls. This data can be viewed and formatted for storage as needed.

---

## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/username/repo-name.git
