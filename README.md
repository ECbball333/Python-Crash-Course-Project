# Python Crash Course (3rd Ed.) — Labs & Notes

Hands-on exercises and mini-projects I’m completing while working through **Python Crash Course (3rd Edition)**. The repo is organized by chapter for quick navigation and review.

## 📁 Repository Structure

- [Chapter 1 - Introduction/](Chapter%201%20-%20Introduction/) 
- [Chapter 2 - Variables and Simple Data Types](Chapter%202%20-%20Variables%20and%20Simple%20Data%20Types/)
- [Chapter 3 - Introducing Lists/](Chapter%203%20-%20Introducing%20Lists/)  
- [Chapter 4 - Working With Lists/](Chapter%204%20-%20Working%20With%20Lists/)  
- [Chapter 5 - If Statements/](Chapter%205%20-%20If%20Statements/)  
- [Chapter 6 - Dictionaries/](Chapter%206%20-%20Dictionaries/) 
- [Chapter 7 - Input and While Loops/](Chapter%207%20-%20Input%20and%20While%20Loops/)  
- [Chapter 8 - Functions/](Chapter%208%20-%20Functions/)  
- [Chapter 9 - Classes/](Chapter%209%20-%20Classes/)
- [Chapter 10 - Files and Exceptions/](Chapter%2010%20-%20Files%20and%20Exceptions/)
- [Chapter 11 – Testing Your Code](./Chapter%2011%20-%20Testing%20your%20Code/)
- [Chapter 15 — Generating Data/](Chapter%2015%20-%20Generating%20Data/)
- [Chapter 16 — Downloading Data/](./Chapter%2016%20-%20Downloading%20Data/)
- [Chapter 17 — Working with APIs/](./Chapter%2017%20-%20Working%20with%20APIs/)
- `Cisco Scripts/` — a separate area where I jot down networking-related Python snippets  
- `script.py` — scratchpad / quick experiments  

> Tip: Many examples are standalone scripts. If a chapter has multiple files, run them individually from that chapter’s folder.

## 🚀 Getting Started

**Prerequisites**
- Python 3.10+ recommended (any 3.8+ should work)
- Optional: `venv` for an isolated environment
- pip install -r requirements.txt

```bash
# create & activate a virtual environment (optional)
python -m venv .venv
# Windows:
.venv\Scripts\activate
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

## Progress

## Chapter 15: Generating Data

This chapter focused on using Python to generate and visualize datasets. It introduced the use of `matplotlib` for static plotting and `plotly` for interactive data visualizations. The projects involved mathematical data generation, simulations, and visual analysis.

### ✅ Skills Gained

- Generating sequences of numbers (squares, cubes)
- Creating and visualizing 2D random walks
- Writing and using custom classes (`RandomWalk`, `Die`)
- Running simulations and analyzing probability distributions
- Visualizing data using `matplotlib` and `plotly`
- Customizing chart appearance and saving plots to files

### 📂 Projects Completed

| File | Description |
|------|-------------|
| `15.1_cubes.py` | Plotted the first 5 cube numbers using a simple scatter plot |
| `scatter_squares.py` | Plotted 1,000 square numbers with gradient coloring and axis formatting |
| `random_walk.py` & `rw_visual.py` | Created random walk simulations and visualized them with colored point progression |
| `15.3_molecular_motion.py` | Simulated molecular motion using styled random walks with colormaps and endpoint markers |
| `15.6_two_d8s.py` | Simulated 200,000 rolls of two 8-sided dice and visualized results using a bar chart in Plotly |
| `15.7_three_dice.py` | Simulated rolling three 6-sided dice and plotted the resulting frequency distribution |

### 💡 Applications for Network Engineers

- Model unpredictable traffic patterns or packet loss using random walks
- Visualize frequency of events like packet drops or error codes using simulation-based histograms
- Build probability distributions for network simulations or reliability testing
- Apply data visualization techniques to network logs, SNMP data, or telemetry feeds

---

### Chapter 16: Working with CSV and JSON Data

- ✔️ Parsed weather data from Sitka, Death Valley, and San Francisco to visualize temperature and precipitation trends
- ✔️ Implemented error handling to manage missing or malformed data entries
- ✔️ Built side-by-side comparison charts for different geographic climates using `matplotlib`
- ✔️ Refactored data parsing and visualization code for clarity and efficiency
- ✔️ Loaded and explored real-world GeoJSON data from the USGS Earthquake API
- ✔️ Extracted earthquake metadata and used `plotly.express` to create interactive global maps
- ✔️ Used list unpacking and `zip()` to streamline variable assignments from complex nested data
- ✔️ Automated chart titles using dataset metadata
- ✔️ Visualized NASA fire detection data on a world map, with brightness and FRP represented as color and size
- ✔️ Saved visualizations as static images and interactive HTML files

- ### 📂 Projects Completed

| File | Description |
|------|-------------|
| `16.1_sitka_rainfall.py` | Parsed and visualized 2021 precipitation data for Sitka, Alaska using `matplotlib` |
| `16.2_sitka-death_valley_comparison.py` | Compared high/low temperatures between Sitka and Death Valley with enhanced error handling and shaded plots |
| `16.3_san_francisco.py` | Extracted and plotted San Francisco temperature trends using CSV weather data |
| `16.6_refactoring.py` | Refactored earthquake GeoJSON parsing by unpacking variables efficiently with `zip()` and visualized using `plotly.express` |
| `16.7_automated_title.py` | Automated chart title generation using metadata from the GeoJSON dataset |
| `16.8_recent_earthquakes.py` | Created an interactive global earthquake map using recent USGS GeoJSON data |
| `16.9_world_fires.py` | Visualized NASA's satellite-detected fire data on a world map with brightness and confidence as hover info; exported map to PNG |


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
