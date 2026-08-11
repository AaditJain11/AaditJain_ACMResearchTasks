```markdown
# Netflix Titles — Exploratory Data Analysis (EDA)

A beginner-to-intermediate EDA project on the **Netflix Movies and TV Shows** dataset, covering data cleaning, missing value handling, and visual analysis of content trends by year, country, genre, and rating.

## 📌 Overview

This notebook explores the Netflix titles dataset to answer questions like:
- How has Netflix's content library grown over time?
- Which countries and genres dominate the catalogue?
- How are movies vs TV shows distributed?
- What's the typical movie duration and content rating?

## 📁 Dataset

- **Name:** Netflix Movies and TV Shows
- **File:** `netflix_titles.csv`
- **Source:** [Kaggle - Netflix Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- **Rows/Columns:** 8,807 rows × 12 columns

> Download `netflix_titles.csv` from the Kaggle link above and place it in the project root (same folder as the notebook).

## ⚙️ Requirements

- Python 3.8+
- Jupyter Notebook / JupyterLab

### Python Libraries

```
pandas
numpy
matplotlib
seaborn
```

Install via:

```bash
pip install pandas numpy matplotlib seaborn
```

Or using a `requirements.txt`:

```
pandas>=1.5.0
numpy>=1.23.0
matplotlib>=3.6.0
seaborn>=0.12.0
```

```bash
pip install -r requirements.txt
```

## 🚀 How to Run

1. **Clone or download** this repository.
2. **Add the dataset** — place `netflix_titles.csv` in the same directory as the notebook.
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Launch Jupyter:**
   ```bash
   jupyter notebook eda.ipynb
   ```
5. **Run all cells** in order (Cell → Run All), since each step builds on the previous one.

## 🧹 What the Notebook Covers

1. Data loading and initial inspection (`shape`, `info`, `describe`)
2. Duplicate and missing value checks
3. Handling missing values in `director` and `country`
4. Fixing `date_added` data type and extracting `year_added`
5. Movies vs TV Shows distribution
6. Top 5 content-producing countries
7. Genre leaders by country
8. Netflix's busiest content-addition year
9. Movie duration distribution
10. Content rating breakdown
11. Content growth trend over the years
12. Content age distribution

## 📊 Key Outputs

- Bar charts, pie charts, histograms, and line plots for each analysis step
- Written observations after each visualization

## 📄 License

For educational/practice purposes only. Dataset © original Kaggle uploader.
```

Want this saved as an actual `README.md` file too, or is the copy-paste block enough?
