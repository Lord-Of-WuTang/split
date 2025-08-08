# Department Cleaner

Simple Python script to merge split department names from a CSV file.

## What it does
- Reads `departments_split.csv` with columns `Part1` and `Part2`
- Combines them into a single `Department` column
- Removes extra whitespace
- Saves cleaned data to `cleaned_departments.csv`

## Usage
```bash
python department_cleaner.py
```

## Requirements
- pandas
- Input file: `departments_split.csv`

## Output
- `cleaned_departments.csv` with merged department names