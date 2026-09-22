# CodeAlpha Data Analytics Internship — Exploratory Data Analysis

## Overview

This project was completed as part of the **CodeAlpha Data Analytics Internship**.

The objective was to perform exploratory data analysis on a dataset of books collected through web scraping.

## Dataset

The dataset contains **1,000 book records** across **50 categories**.

The analysis included:

* Data quality checks
* Missing-value analysis
* Duplicate detection
* Descriptive statistics
* Category analysis
* Rating analysis
* Price analysis
* Correlation analysis
* ANOVA statistical testing

## Key Findings

* Dataset size: **1,000 rows**
* Number of categories: **50**
* Average price: **£35.07**
* Average rating: **2.92 / 5**
* Price-rating correlation: **0.028**
* Duplicate titles identified: **1**
* Missing values: **0**
* ANOVA: **F = 0.366, p = 0.8330**

The analysis did not find evidence of a statistically significant difference in book price across rating groups.

## Technologies Used

* Python
* Pandas
* NumPy
* SciPy

## Files

```text
codealpha_eda/
├── README.md
├── eda.py
└── books_data.csv
```

## Setup

Install the required libraries:

```bash
pip install pandas numpy scipy
```

## Usage

Run the analysis with:

```bash
python eda.py
```

The script performs the exploratory analysis and displays the results in the terminal.

## Internship Task

**CodeAlpha Data Analytics Internship — Task 2: Exploratory Data Analysis**
