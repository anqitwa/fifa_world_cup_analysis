# FIFA World Cup Analysis

This project analyzes historical FIFA World Cup data to uncover key trends, metrics, and factors that influence World Cup wins. The analysis includes insights into goals scored, attendance, player contributions, and team performance across different tournaments. It is designed to be modular, testable, and portable, adhering to best practices for maintainable code.


## Features

- Modular and maintainable Python code.
- Automatic generation of visualizations and their saving as image files.
- Insights into goals scored, attendance trends, and team performance.
- Testable components with unit tests for each module.
- Portable design to work seamlessly across environments.

## Setup and Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/anqitwa/fifa-worldcup-analysis.git
   cd fifa-worldcup-analysis
   ```

2. **Install dependencies**:

   Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: .\env\Scripts\activate
   ```

   Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the data**:

   Place the provided CSV files (`WorldCupMatches.csv`, `WorldCupPlayers.csv`, `WorldCups.csv`) into the `data/` directory.

4. **Run the analysis**:

   Execute the main script:
   ```bash
   python src/main.py
   ```

   This will:
   - Load and clean the datasets.
   - Perform exploratory data analysis (EDA).
   - Generate visualizations and save them in the `output/plots/` folder.

## Usage

- **For automated analysis**:
  Simply run the `main.py` script to execute the entire pipeline.

- **For interactive exploration**:
  Open the Jupyter notebook in the `notebooks/` folder:
  ```bash
  jupyter notebook notebooks/analysis_notebook.ipynb
  ```

- **For testing**:
  Run unit tests with `pytest`:
  ```bash
  pytest tests/
  ```

## Visualizations

The following visualizations are generated and saved in the `output/plots/` directory:

1. **Trend of Goals Scored Across World Cups**: A line plot showing the total number of goals scored in each tournament over the years.
2. **Average Attendance Per Match Over the Years**: A bar plot showing the average attendance per match for each World Cup.
3. **Distribution of Goals Scored by Home and Away Teams**: A histogram comparing the distribution of goals scored by home and away teams.
4. **Goals Scored by Winning Teams**: A bar plot showing the number of goals scored by each winning team during their victorious tournaments.
5. **Top 10 Teams with the Most Players**: A bar plot showing the top 10 teams with the highest number of players who participated in World Cup tournaments.

All visualizations are saved as PNG files and can be found in the `output/plots/` directory.


Saved visualizations are stored in the `output/plots/` directory.

## License

This project is open-source and available under the [MIT License](LICENSE).

---


