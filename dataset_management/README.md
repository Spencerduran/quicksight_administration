# QuickSight Summary Script
This script generates a summary of AWS QuickSight datasets, analyses, and dashboards, showing which datasets are used by which analyses and dashboards. The summary is exported to an Excel file named `quicksight_summary.xlsx`.

## Prerequisites
- Python 3.x
- Boto3 library
- Pandas library
- AWS credentials with QuickSight access

Install the required libraries using pip:

`pip install boto3 pandas`

## Usage
Run the script without any arguments to generate the summary:

`python quicksight_summary.py`

Upon successful execution, the script will create an Excel file named `quicksight_summary.xlsx` with the summary of datasets, analyses, and dashboards.

## Overview
The script performs the following steps:

1. Set up AWS credentials and region.
2. Initialize the QuickSight client.
3. Get the datasets, analyses, and dashboards.
4. Fetch the analysis and dashboard details.
5. Create a summary DataFrame and fill in the data.
6. Write the DataFrame to an Excel file.
