# Python Crash Course (3rd Ed.) — Labs & Notes

Hands-on exercises and mini-projects I’m completing while working through **Python Crash Course (3rd Edition)**. The repo is organized by chapter for quick navigation and review.

## 📁 Repository Structure

- `Chapter 1 - Introduction/`  
- `Chapter 2 - Variables and Simple Data Types/`  
- `Chapter 3 - Introducing Lists/`  
- `Chapter 4 - Working With Lists/`  
- `Chapter 5 - If Statements/`  
- `Chapter 6 - Dictionaries/`  
- `Chapter 7 - Input and While Loops/`  
- `Chapter 8 - Functions/`  
- `Chapter 9 - Classes/`
- `Chapter 10 - Files and Exceptions/`
- `Chapter 11 - Testing your Code/`
- `Chapter 15 - Generating Data/`
- `Cisco Scripts/` — a separate area where I jot down networking-related Python snippets  
- `script.py` — scratchpad / quick experiments  

> Tip: Many examples are standalone scripts. If a chapter has multiple files, run them individually from that chapter’s folder.

## 🚀 Getting Started

**Prerequisites**
- Python 3.10+ recommended (any 3.8+ should work)
- Optional: `venv` for an isolated environment

```bash
# create & activate a virtual environment (optional)
pip install -r requirements.txt
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

**Run any example**
```bash
# from a chapter folder:
python some_example.py
```

## ✅ Progress Snapshot

| Chapter | Topic                           | Status |
|--------:|----------------------------------|:------:|
| 1       | Introduction                     |  ✅    |
| 2       | Variables & Simple Data Types    |  ✅    |
| 3       | Introducing Lists                |  ✅    |
| 4       | Working With Lists               |  ✅    |
| 5       | If Statements                    |  ✅    |
| 6       | Dictionaries                     |  ✅    |
| 7       | Input & While Loops              |  ✅    |
| 8       | Functions                        |  ✅    |
| 9       | Classes                          |  ✅    |

Update the table as you progress.

## 🧪 Testing & Linting (optional)

If/when I add tests:
```bash
pip install pytest
pytest -q
```

Code style (optional):
```bash
pip install black ruff
black .
ruff check .
```

## 📚 Reference

- *Python Crash Course, 3rd Edition* by Eric Matthes
- Official Python docs: https://docs.python.org/3/

## 📄 License

Licensed under the MIT License — see LICENSE for details.
