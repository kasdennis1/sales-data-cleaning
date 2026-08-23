# Sales Data Cleaning & Business Risk Analysis

## Project Overview

Cleaned and analyzed a messy sales dataset using Pandas to identify data-quality issues and potential business risks.

## Tools Used

- Python
- Pandas

## Data Quality Issues Identified

- Inconsistent capitalization
- Unnecessary whitespace
- Missing customer information
- Missing sales value
- Duplicate transactions
- Negative sales transaction

## Data Cleaning Performed

- Standardized customer and product names
- Removed unnecessary whitespace
- Replaced missing customer names with "Unknown"
- Replaced missing sales values with 0
- Removed duplicate records
- Flagged negative sales transactions

## Key Business Risk

The most critical issue identified was a negative sales transaction:

**David — Laptop — ₦-45,000**

This transaction should be investigated before the dataset is used for financial reporting because it can distort revenue calculations.

## Output

A cleaned dataset was generated as:

`data/cleaned_sales.csv`
