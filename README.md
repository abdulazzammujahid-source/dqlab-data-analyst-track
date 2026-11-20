# DQLab Data Analyst Career Track (Python)

Submitted code for DQLab's Data Analyst Career Track (Python), completed 20 Nov 2026.

The track is 15 modules and 581 exercises covering Python fundamentals, SQL, pandas,
Matplotlib, data quality, exploratory data analysis, and machine learning. Each file in
this repo holds the answers I submitted for one module, one block per exercise.

## Capstone

`15-data-analyst-project-business-decision-research.py` is the final project. It works on a
retail transaction dataset (`data_retail.csv`, loaded from DQLab's CDN) and covers:

- data preparation and cleaning (date parsing, churn flagging, dropping unused columns)
- exploratory charts: customer acquisition by year, transactions by year, average
  transaction amount per product, churn proportion per product, transaction count buckets
- a churn model: logistic regression on average transaction amount, transaction count and
  customer tenure, evaluated with a confusion matrix, accuracy, precision and recall

## Modules

| # | Module |
|---|--------|
| 01 | Guide to Learn Python with AI at DQLab |
| 02 | Python for Data Professional Beginner - Part 1 |
| 03 | Python for Data Professional Beginner - Part 2 |
| 04 | Python for Data Professional Beginner - Part 3 |
| 05 | Fundamental SQL Using SELECT Statement |
| 06 | Fundamental SQL Using FUNCTION and GROUP BY |
| 07 | Fundamental SQL Using INNER JOIN and UNION |
| 08 | Exploratory Data Analysis with Python for Beginner |
| 09 | Data Manipulation with Pandas - Part 1 |
| 10 | Data Manipulation with Pandas - Part 2 |
| 11 | Data Visualization with Python Matplotlib for Beginner - Part 1 |
| 12 | Data Visualization with Python Matplotlib for Beginner - Part 2 |
| 13 | Data Quality with Python for Beginner |
| 14 | Machine Learning With Python for Beginner |
| 15 | Data Analyst Project - Business Decision Research |

## Running

The pandas, matplotlib and scikit-learn files expect `pandas`, `numpy`, `matplotlib`,
`seaborn` and `scikit-learn`. The datasets are pulled from DQLab's public CDN, so the
scripts run as-is. SQL files are the queries submitted in the module's editor, run against
DQLab's sample databases.

## Certificate

Data Analyst Python Track, DQLab, 20 Nov 2026, ID `DQLABDATRCJJWWAP`.
Verify: https://academy.dqlab.id/certificate_check/result/DQLABDATRCJJWWAP
