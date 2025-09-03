
***

# Keylogger Automation Tool  

This project provides a simple educational **Python keylogger** that captures keystrokes and writes them to a file. It also includes a terminal-based spinner animation indicating that logging is running.  

⚠️ **Disclaimer:** This tool is provided strictly for **educational purposes** (e.g., learning about monitoring software, system defenses, or building your own parental monitoring / usability tracking tool).  
- **Do NOT use it on machines you do not own or have explicit permission to monitor.**  
- Unauthorized use is illegal and unethical.  

***

## Prerequisites  

- **Operating System**: Linux, macOS, or Windows  
- **Python Version**: Python 3.7+  
- **Dependencies**:  
  - [`pynput`](https://pypi.org/project/pynput/) – keyboard event capturing library  

Install dependencies via:  

```bash
pip install pynput
```

***

## Script  

**File:** `keylogger.py`  

This script:  
1. Listens for all keystrokes.  
2. Logs them into a text file (`keystrokes.txt`).  
3. Displays a live "spinner" animation in the terminal while running.  
4. Stops when the user presses the `Escape` key or interrupts with `Ctrl+C`.  

***

## Usage  

### Run the Script  

```bash
python keylogger.py
```

### Output  

- Logged keystrokes are stored inside a file:  

```
keystrokes.txt
```

- On-screen animation shows:  

```
Keylogger is running... |
```

…and updates dynamically.  

- Stopping the script:  
  - Press `Esc` → gracefully stops and prints `Keylogger stopped.`  
  - Or press `Ctrl+C` → forcefully stops the script.  

***

## Ethical Considerations  

- **Authorization**: Only use this script on systems you own or have explicit consent to monitor.  
- **Legal Compliance**: In most jurisdictions, unauthorized surveillance of keystrokes is **illegal** (computer misuse / privacy laws).  
- **Educational Value**: This project is intended for:  
  - Demonstrating Python event listeners  
  - Learning about OS-level input capture  
  - Testing defensive countermeasures against keyloggers  

***

## Disclaimer  

The author is **not responsible** for any misuse of this tool.  
Always ensure **proper authorization** before running this script. **Use responsibly.**  

***

## Contributing  

Contributions (e.g., enhancements, making the logger stealthier *for legitimate research*, security hardening, visualization tools) are welcome. Fork and submit pull requests.  

***

## License  

This project is licensed under the **MIT License**. See the `LICENSE` file for details.  

***
