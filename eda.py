"""
CodeAlpha Data Analytics Internship - Task 2: Exploratory Data Analysis (EDA)
-------------------------------------------------------------------------------
Explores the books_data.csv produced by scraper.py:
- data structure & types
- missing values / anomalies
- summary statistics
- trends and simple hypothesis checks

Requirements:
    pip install pandas numpy scipy

Usage:
    python eda.py   (run this AFTER scraper.py has created books_data.csv)
"""

import pandas as pd
import numpy as np
from scipy import stats

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

CSV_PATH = "books_data.csv"


def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def main():
    df = pd.read_csv(CSV_PATH)

    # ---------- 1. Structure & data types ----------
    section("1. DATASET STRUCTURE")
    print(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns\n")
    print(df.dtypes)
    print("\nFirst 5 rows:")
    print(df.head())

    # ---------- 2. Missing values & anomalies ----------
    section("2. MISSING VALUES & DATA ISSUES")
    missing = df.isnull().sum()
    print("Missing values per column:")
    print(missing)

    duplicate_titles = df["title"].duplicated().sum()
    print(f"\nDuplicate titles: {duplicate_titles}")

    # Anomaly check: any negative or zero prices?
    bad_prices = df[df["price_gbp"] <= 0]
    print(f"Books with price <= 0 (anomaly check): {len(bad_prices)}")

    # Anomaly check: ratings outside 1-5
    bad_ratings = df[~df["rating"].between(1, 5)]
    print(f"Books with invalid rating (outside 1-5): {len(bad_ratings)}")

    # ---------- 3. Summary statistics ----------
    section("3. SUMMARY STATISTICS")
    print(df[["price_gbp", "rating"]].describe())

    # ---------- 4. Category breakdown ----------
    section("4. CATEGORY BREAKDOWN")
    cat_counts = df["category"].value_counts()
    print(f"Number of unique categories: {df['category'].nunique()}")
    print("\nTop 10 categories by book count:")
    print(cat_counts.head(10))

    # ---------- 5. Trends: price by category ----------
    section("5. AVERAGE PRICE BY CATEGORY (Top 10 by count)")
    top_cats = cat_counts.head(10).index
    avg_price_by_cat = (
        df[df["category"].isin(top_cats)]
        .groupby("category")["price_gbp"]
        .mean()
        .sort_values(ascending=False)
    )
    print(avg_price_by_cat.round(2))

    # ---------- 6. Rating distribution ----------
    section("6. RATING DISTRIBUTION")
    rating_counts = df["rating"].value_counts().sort_index()
    print(rating_counts)
    print(f"\nAverage rating across all books: {df['rating'].mean():.2f}")

    # ---------- 7. Hypothesis test: does price differ by rating? ----------
    section("7. HYPOTHESIS TEST")
    print("H0: Average price is the same across rating groups (1-5 stars).")
    print("H1: Average price differs across rating groups.\n")

    groups = [df[df["rating"] == r]["price_gbp"].values for r in sorted(df["rating"].dropna().unique())]
    f_stat, p_value = stats.f_oneway(*groups)
    print(f"ANOVA result -> F-statistic: {f_stat:.3f}, p-value: {p_value:.4f}")
    if p_value < 0.05:
        print("Result: p < 0.05 -> reject H0. Price differs significantly across rating groups.")
    else:
        print("Result: p >= 0.05 -> fail to reject H0. No significant price difference by rating.")

    # ---------- 8. Correlation ----------
    section("8. CORRELATION")
    corr = df[["price_gbp", "rating"]].corr().iloc[0, 1]
    print(f"Correlation between price and rating: {corr:.3f}")

    # ---------- 9. Availability check ----------
    section("9. STOCK AVAILABILITY")
    print(df["availability"].value_counts())

    section("EDA COMPLETE")
    print("Findings summary saved conceptually above. Use visualize.py next to turn")
    print("these into charts for your report / portfolio.")


if __name__ == "__main__":
    main()
