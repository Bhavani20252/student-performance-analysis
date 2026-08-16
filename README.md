# Student Entrance Examination Performance Analysis
## 🌐 Live Dashboard

[Open the Student Performance Analysis Dashboard](https://student-performance-analysis-hdjuft5wq7bvwa2cftuqfp.streamlit.app/)

## 📌 Project Overview

This project analyzes student performance in an entrance examination using data related to students' academic background, coaching participation, coaching duration, education medium, and family background.

The main objective is to identify meaningful relationships between student characteristics and entrance-examination performance using:

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Statistical analysis
- Data visualization
- Interactive Streamlit dashboard
- Executive summary

The project follows a complete data-science workflow from raw data to insights and an interactive application.

---

## 🎯 Objectives

The main objectives of this project are to:

1. Understand the overall distribution of student entrance-examination performance.
2. Investigate whether coaching participation is associated with performance.
3. Investigate the relationship between Class XII academic performance and entrance-examination performance.
4. Analyze whether reported coaching duration is associated with performance.
5. Use statistical tests to determine whether observed relationships are statistically significant.
6. Present the findings through clear visualizations and an interactive dashboard.
7. Provide actionable recommendations while considering limitations and possible bias.

---

## 📊 Dataset

The project uses the **Student Performance on an Entrance Examination** dataset.

The dataset contains **666 student records** and includes academic, demographic, coaching, and family-background attributes.

### Important Attributes

| Attribute | Description |
|---|---|
| `Performance` | Entrance-examination performance |
| `Gender` | Student gender |
| `Caste` | Student caste category |
| `coaching` | Coaching participation |
| `time` | Reported coaching-duration category |
| `Class_ten_education` | Class X education board |
| `twelve_education` | Class XII education board |
| `medium` | Medium of education |
| `Class_X_Percentage` | Class X performance category |
| `Class_XII_Percentage` | Class XII performance category |
| `Father_occupation` | Father's occupation |
| `Mother_occupation` | Mother's occupation |

### Target Variable

The target variable is **Performance**.

The four performance categories are:

- **Excellent**
- **Vg**
- **Good**
- **Average**

### Dataset Source

The dataset is from the UCI Machine Learning Repository:

**Student Performance on an Entrance Examination**

[UCI Machine Learning Repository – Student Performance on an Entrance Examination](https://archive.ics.uci.edu/dataset/582/student%2Bp)

---

# 🔎 Research Questions

The analysis focuses on three main research questions.

## RQ1 — Coaching and Performance

**Is participation in coaching associated with entrance-examination performance?**

This compares the performance distribution of students across different coaching categories.

---

## RQ2 — Class XII Performance and Entrance Performance

**How is Class XII academic performance associated with entrance-examination performance?**

This examines whether students with different Class XII performance levels show different entrance-examination performance patterns.

---

## RQ3 — Coaching Duration and Performance

**Does reported coaching duration show different entrance-examination performance patterns?**

This compares performance across the available coaching-duration categories.

---

# 🧹 Data Cleaning

The raw dataset was inspected before analysis.

The following checks were performed:

- Dataset dimensions
- Missing values
- Data types
- Categorical values
- Duplicate rows
- Target-variable distribution

### Missing Values

The dataset contains no missing values.

### Duplicate Rows

The dataset contains exact duplicate feature rows.

These rows were **not automatically removed** because the dataset does not provide a unique student identifier. Therefore, identical feature values do not prove that the records belong to the same student.

This decision prevents potentially valid observations from being incorrectly deleted.

The cleaned dataset is stored in:

```text
data/processed/cleaned_student_data.csv
