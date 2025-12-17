# Week 1 – Ingestion Gate (Python)

This project simulates a simple ingestion boundary in a data pipeline.

## Purpose
Validate incoming filenames before they are allowed to enter downstream processing.

## Rules enforced
- Only `.csv` and `.txt` files are accepted
- Filenames must contain exactly one dot
- Filenames may only contain alphanumeric characters (dots allowed as separators)

## Output
- Each file is classified as Accepted or Rejected
- Rejected files include an explicit rejection reason
- A summary is printed showing totals processed, accepted, and rejected

## Why this matters
Early validation prevents bad inputs from polluting downstream data models, analytics, and reports.
This mirrors real ingestion checks used before loading data into warehouses like Snowflake.
