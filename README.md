# Python Help Caller

## Overview
Python Help Caller is a project designed to trigger help‑call events using physical buttons connected through microcontrollers. When a button is pressed, the system automatically detects the event and processes it through either a local all‑in‑one interface or a cloud‑connected Google Sheets workflow.

This project was originally assigned as a challenge to design a reliable, scalable button‑based help‑calling system.

---

## Features
- **Automatic multi‑device detection**  
  Seamlessly connects to multiple microcontrollers over USB serial.

- **Scalable architecture**  
  Supports a theoretically unlimited number of microcontrollers and buttons.

- **Dynamic updating**  
  Devices can connect or disconnect at any time without restarting the system.

- **All‑in‑One Suite**  
  A standalone Python script that opens its own window for help‑call monitoring.

- **Google Sheets integration**  
  Cloud‑based configuration and storage using the Sheets API via `gspread`.

- **Basic backend mode**  
  A simplified version for understanding the core logic and data flow.

---

## AI Usage in This Project
AI tools were used throughout development to support:

- **Debugging**  
  Helping interpret error messages and identify root causes.

- **Research**  
  Finding reliable methods for interfacing Python with Arduino devices.

- **Documentation**  
  Assisting with structuring and improving readability of the README and other project notes.

---

## Installation
1. Clone the project folder for the suite you want to use.  
2. Follow the included instructions inside that folder for setup and configuration.

---

## Usage
- Run the included Python script for the suite you selected.  
- The All‑in‑One Suite will open its own window.  
- The Google Sheets Suite will sync with your configured spreadsheet.

---

## Project Structure

### All‑in‑One Suite
- A single Python script containing all logic  
- Includes helper JSON files for:
  - Persistent storage  
  - Easy configuration  

### Google Sheets Suite
- Uses the Google Sheets API through `gspread`  
- Designed for cloud‑based logging, configuration, and monitoring  

---

## Contributing
Contributions are unlikely but welcome.  
If you want to contribute:
- Fork the repository  
- Follow the project license when submitting changes  

---

## License
This project is licensed under **GPL‑2.0**.
