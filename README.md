# NameCrack

**NameCrack** is a sophisticated password generation and security analysis tool that creates potential passwords from text input using various transformation techniques. The tool helps security researchers and penetration testers generate realistic password dictionaries based on personal information, while simultaneously checking generated passwords against known breach databases.

## 🚀 Features

- **Multi-source Data Extraction**: Automatically extracts names, dates, numbers, colors, emails, and usernames from input text
- **Advanced Text Processing**: Uses spaCy NLP for intelligent name recognition
- **Leet Speak Transformation**: Converts text to leet speak with customizable patterns (even/odd character replacement)
- **Password Variations**: Generates lowercase, uppercase, and reversed versions
- **Permutation Generation**: Creates combinations of extracted elements
- **Breach Database Check**: Validates passwords against HaveIBeenPwned API
- **Multiple Export Formats**: Supports JSON and XML export
- **Rich Terminal Interface**: Beautiful console output with colored text and progress indicators

## 📋 Requirements

- Python 3.7+
- spaCy English language model
- Internet connection (for breach checking)

For downloading use `python` or `python3`

## 🛠 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/anonymmized/NameCrack.git
   cd NameCrack
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download spaCy English model:**
   ```bash
   python -m spacy download en_core_web_sm
   ```

## 💻 Usage

### Basic Usage

```bash
python main.py -t "John Smith born 1990 email john.smith@example.com"
```

### Advanced Options

```bash
# Generate passwords with leet speak transformation
python main.py -t "Alice Johnson 1985" --leet

# Include reversed and uppercase variations
python main.py -t "Bob Wilson 1975" --reverse --upper

# Set custom password length constraints
python main.py -t "Sarah Davis" --min-length 8 --max-length 16

# Export results to JSON
python main.py -t "Mike Brown 1980" --json

# Export results to XML
python main.py -t "Lisa Taylor" --xml
```

### Command Line Arguments

| Argument | Short | Description | Required |
|----------|--------|-------------|----------|
| `--text` | `-t` | Input text for analysis | Yes |
| `--leet` | `-lt` | Enable leet speak transformations | No |
| `--reverse` | `-rv` | Add reversed password variations | No |
| `--upper` | `-up` | Add uppercase password variations | No |
| `--min-length` | | Minimum password length (default: 6) | No |
| `--max-length` | | Maximum password length (default: 12) | No |
| `--json` | | Export passwords to JSON format | No |
| `--xml` | | Export passwords to XML format | No |

## 🔍 How It Works

### Data Extraction Modules

1. **Name Recognition** (`find_names.py`): Uses spaCy NLP to identify person names
2. **Date Processing** (`find_dates.py`): Extracts dates in various formats
3. **Number Processing** (`find_number.py`): Identifies significant numbers
4. **Color Recognition** (`find_colors_nums.py`): Finds color names and associated numbers
5. **Email/Login Processing** (`find_mails_logins.py`): Extracts email addresses and potential usernames

### Password Generation Process

1. **Text Analysis**: Input text is processed by specialized extraction modules
2. **Permutation Generation**: Creates combinations of extracted elements
3. **Transformation Application**: Applies leet speak, case changes, and reversals
4. **Length Filtering**: Filters passwords based on specified length constraints
5. **Uniqueness**: Removes duplicate passwords

### Security Validation

- **Breach Checking**: Uses HaveIBeenPwned API to check if generated passwords have been compromised
- **Secure Hashing**: Uses SHA-1 with k-anonymity (only first 5 characters of hash sent)
- **Rate Limiting**: Implements proper API usage guidelines

## 📊 Output Example

```
🔍 Checking passwords against breach databases...

📊 Results:
Total passwords generated: 847
Compromised passwords found: 23

⚠️  Compromised passwords:
  - john1990: 1,247 breaches
  - password123: 9,545,824 breaches
  - smith85: 89 breaches

✅ 824 unique, uncompromised passwords generated!
```

## 🔒 Security Considerations

⚠️ **Important**: This tool is designed for:
- **Authorized security testing**
- **Educational purposes**
- **Personal password strength analysis**
- **Legitimate penetration testing**

**Do NOT use this tool for:**
- Unauthorized access attempts
- Malicious hacking
- Any illegal activities

## 🧪 Testing

```bash
# Run basic functionality test
python main.py -t "Test User 1995 test@example.com" --min-length 4 --max-length 10
```

## 📁 Project Structure

```
NameCrack/
├── main.py                 # Main application entry point
├── check_pas.py           # Password breach checking
├── do_leet_speak.py       # Leet speak transformations
├── export_data.py         # Data export functionality
├── find_colors_nums.py    # Color and number extraction
├── find_dates.py          # Date pattern recognition
├── find_mails_logins.py   # Email and login extraction
├── find_names.py          # Name recognition using NLP
├── find_number.py         # Number pattern extraction
├── project_ascii.py       # ASCII art display
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🛠 Dependencies

- **rich**: Beautiful terminal formatting
- **spacy**: Natural language processing
- **requests**: HTTP API communication
- **colour**: Color name recognition

## 📄 License

This project is intended for educational and authorized security testing purposes only. Users are responsible for ensuring they comply with all applicable laws and regulations.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📞 Support

For issues, questions, or contributions, please open an issue on GitHub.

---

**Disclaimer**: This tool is for educational and authorized testing purposes only. The authors are not responsible for any misuse or damage caused by this software.
