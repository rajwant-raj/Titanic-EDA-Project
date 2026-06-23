<<<<<<< HEAD
# Titanic-EDA-Project
=======
# Titanic EDA (Exploratory Data Analysis) Project

This project contains tools to perform basic Exploratory Data Analysis (EDA) on the classic Titanic dataset. It automatically generates key visualizations to understand passenger demographics, correlation, and factors affecting survival.

## Folder Structure

```text
EDA_Project/
│
├── eda_titanic.py
├── outputs/
│   ├── age_distribution.png
│   ├── gender_distribution.png
│   ├── survival_distribution.png
│   ├── survival_by_gender.png
│   ├── survival_by_class.png
│   ├── correlation_heatmap.png
│
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Prerequisites

Make sure you have Python 3.8+ installed.

### 2. Install Dependencies

You can install all necessary packages using `pip`:

```bash
pip install -r requirements.txt
```

### 3. Run the EDA Script

Run the following command to load the dataset, perform analysis, and generate the plots:

```bash
python eda_titanic.py
```

The script will automatically create an `outputs/` folder and populate it with the following visualizations:
*   `age_distribution.png`: Histogram showing passenger age distributions.
*   `gender_distribution.png`: Bar chart representing gender demographics.
*   `survival_distribution.png`: Count of overall survivors vs non-survivors.
*   `survival_by_gender.png`: Survival counts grouped by gender.
*   `survival_by_class.png`: Survival counts grouped by passenger class.
*   `correlation_heatmap.png`: Heatmap showing correlations between numeric features.
>>>>>>> 239a8b0 (Initial commit: Add Titanic EDA project files)
