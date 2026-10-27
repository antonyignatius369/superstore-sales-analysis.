# Superstore Sales Analysis

A beginner-friendly Data Science case study exploring retail sales, profitability, customer segments, regions, discounts, and sales trends using Python. This project answers the 10 questions in the supplied case-study brief.

## Business questions

1. What is the size and structure of the dataset?
2. Are there missing values or duplicate records?
3. What are total sales, total profit, and average order-line sales?
4. Which product categories generate the most sales?
5. Which sub-categories generate the highest and lowest profit?
6. Which region has the highest sales?
7. Which customer segment contributes the most sales?
8. How do discounts relate to profit?
9. How do sales change over time?
10. What business recommendations can be made?

## Dataset

Download **Sample - Superstore.csv** from the [Kaggle Superstore dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final). The analysis expects the standard CSV file with columns such as `Order Date`, `Sales`, `Profit`, `Category`, `Sub-Category`, `Region`, `Segment`, and `Discount`. The CSV is not included in this repository; place it next to the Python script or upload it to Colab.

> This is a historical educational sample of US retail data (2014–2017), not current data from a real retailer. Use the results as a learning exercise, not as current business facts.

## Repository contents

- `Superstore_Sales_Analysis.ipynb` — notebook for Google Colab/Jupyter.
- `superstore_analysis.py` — complete Python analysis script.
- `Superstore_Sales_Analysis_Case_Study.docx` — report covering methodology, findings, recommendations, limitations, and references.
- `requirements.txt` — Python dependencies.
- `.gitignore` — excludes local datasets and Python-generated files.

## Run in Google Colab

1. Download the CSV from Kaggle.
2. Open `Superstore_Sales_Analysis.ipynb` in [Google Colab](https://colab.research.google.com/).
3. Upload `Sample - Superstore.csv` to the Colab session.
4. Run the notebook. If your filename differs, update `CSV_PATH` in the code.
5. Review the printed outputs and charts. Confirm the numbers against the exact CSV you downloaded before submitting the report.

## Run locally

```bash
python -m pip install -r requirements.txt
python superstore_analysis.py
```

If the CSV is stored elsewhere, change `CSV_PATH` near the top of `superstore_analysis.py`.

## Methods

- Dataset shape, column types, missing-value and duplicate checks
- Aggregation with Pandas `groupby`
- Sales/profit summaries by category, sub-category, region, segment, and discount
- Discount-profit correlation and scatter plot
- Annual and monthly sales trend charts

## Key findings to verify by running the notebook

For the standard version of this dataset, published summaries typically show total sales of about **$2.297 million**, total profit of about **$286,397**, highest category sales in **Technology**, highest regional sales in the **West**, highest segment sales in **Consumer**, and the lowest sub-category profit in **Tables**. The notebook computes the exact figures from the local CSV; use those computed values as the final authority if your copy differs.

## Recommendations

- Review negative-profit sub-categories and assess pricing, shipping, sourcing, and discounting.
- Track profit and margin alongside revenue when evaluating promotions.
- Compare region and segment performance before allocating marketing resources.
- Use monthly trends to inform inventory and campaign planning.
- Validate these historical patterns with current business data before making decisions.

## Limitations

- The dataset is historical and geographically limited.
- Rows represent order lines, not necessarily unique orders.
- Discount-profit patterns show association, not proof of causation.
- The report includes standard reference values; run the notebook and check them against the downloaded file before final submission.

## Source

Vivek Chowdhury, [Superstore Dataset on Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final).
