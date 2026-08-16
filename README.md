# Student Entrance Examination Performance Analysis

## Project Overview

This project analyzes student entrance-examination performance using a dataset containing academic, coaching, demographic, and family-background attributes.

The main objective is to identify relationships between student preparation factors and entrance-examination performance using exploratory data analysis, statistical testing, and interactive visualization.

The project also provides an interactive Streamlit dashboard for exploring the results.

---

## Objectives

The project aims to:

- Clean and prepare the student dataset.
- Explore the distribution of entrance-examination performance.
- Investigate the relationship between coaching participation and performance.
- Investigate the relationship between Class XII academic performance and entrance-examination performance.
- Investigate the relationship between reported coaching duration and performance.
- Apply statistical tests to quantify associations.
- Visualize important patterns.
- Provide an interactive Streamlit dashboard.
- Summarize the main findings and recommendations.

---

## Dataset

The project uses the **Student Performance on an Entrance Examination** dataset.

The dataset contains information about students who qualified for admission to medical colleges in Assam.

## Decisions Made

### 1. Duplicate Handling

The dataset contains exact duplicate feature rows. These were retained because
there is no student identifier, so identical feature values do not prove that
two records represent the same student.

### 2. Missing Values

The dataset was checked for missing values. No missing values were found.

### 3. Statistical Test

Chi-square tests of independence were used for categorical variables.

Cramer's V was used to describe the strength of association.

### 4. Sparse Categories

The coaching-duration variable contains very small categories. Because the
chi-square approximation becomes unreliable when expected frequencies are
small, a permutation-based test was used for the duration analysis.

### 5. Causal Interpretation

The dataset is observational. Therefore, statistically significant associations
are not interpreted as proof that coaching or another variable causes improved
performance.

Important variables include:

- `Performance`
- `Gender`
- `Caste`
- `coaching`
- `time`
- `Class_ten_education`
- `twelve_education`
- `medium`
- `Class_X_Percentage`
- `Class_XII_Percentage`
- `Father_occupation`
- `Mother_occupation`

The target variable is:

```text
Performance






