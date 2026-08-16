import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Student Performance Analytics",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Entrance Examination Performance Analytics")

st.write(
    """
    This dashboard analyzes how academic preparation and
    coaching-related factors are associated with entrance
    examination performance.
    """
)

df = pd.read_csv("data/processed/cleaned_student_data.csv")

st.subheader("Dataset Preview")

st.dataframe(df)
st.header("📌 Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Students",
    len(df)
)

col2.metric(
    "Performance Categories",
    df["Performance"].nunique()
)

col3.metric(
    "Coaching Groups",
    df["coaching"].nunique()
)

col4.metric(
    "Missing Values",
    int(df.isnull().sum().sum())
)

st.sidebar.title("🔎 Filters")
gender_filter = st.sidebar.multiselect(
    "Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

coaching_filter = st.sidebar.multiselect(
    "Coaching",
    options=df["coaching"].unique(),
    default=df["coaching"].unique()
)

medium_filter = st.sidebar.multiselect(
    "Medium",
    options=df["medium"].unique(),
    default=df["medium"].unique()
)
filtered_df = df[
    df["Gender"].isin(gender_filter)
    & df["coaching"].isin(coaching_filter)
    & df["medium"].isin(medium_filter)
]


st.header("📊 Overall Performance")
performance_counts = (
    filtered_df["Performance"]
    .value_counts()
    .reset_index()
)

performance_counts.columns = [
    "Performance",
    "Students"
]

st.bar_chart(
    performance_counts.set_index("Performance")
)


st.header("🔍 Question 1")

st.write(
    "1)Is participation in coaching associated with entrance-examination performance❓"
)
q1 = pd.crosstab(
    filtered_df["coaching"],
    filtered_df["Performance"],
    normalize="index"
) * 100

st.bar_chart(q1)
st.info(
    """
    This visualization compares the percentage distribution
    of performance categories across coaching groups.
    Differences indicate observed associations and should
    not be interpreted as proof that coaching causes better
    performance.
    """
)
st.subheader("Performance Distribution (%)")

st.dataframe(
    q1.round(2),
    use_container_width=True
)
from scipy.stats import chi2_contingency

q1_counts = pd.crosstab(
    filtered_df["coaching"],
    filtered_df["Performance"]
)

chi2, p_value, dof, expected = chi2_contingency(
    q1_counts
)

st.subheader("Statistical Evidence")

st.write(f"Chi-square statistic: **{chi2:.2f}**")
st.write(f"P-value: **{p_value:.4f}**")
if p_value < 0.05:
    st.success(
        "The test provides statistical evidence of an association "
        "between coaching and performance."
    )
else:
    st.warning(
        "The test does not provide sufficient statistical evidence "
        "of an association between coaching and performance."
    )


st.header("🔍 Question 2")

st.write(
    "2)How is Class XII academic performance associated with entrance-examination performance❓"
)

q2 = pd.crosstab(
    filtered_df["Class_XII_Percentage"],
    filtered_df["Performance"],
    normalize="index"
) * 100
st.bar_chart(q2)
st.subheader("Class XII vs Entrance Performance (%)")

st.dataframe(
    q2.round(2),
    use_container_width=True
)
st.info(
    """
    The table and chart show how entrance-examination
    performance is distributed across Class XII performance
    categories.
    """
)
q2_counts = pd.crosstab(
        filtered_df["Class_XII_Percentage"],
        filtered_df["Performance"]
    )
chi2, p_value, dof, expected = chi2_contingency(
    q2_counts
)
st.header("Statistical Evidence")
st.write(f"Chi-square statistic: **{chi2:.2f}**")
st.write(f"P-value: **{p_value:.4f}**")

if p_value < 0.05:
    st.success(
        "The test provides statistical evidence of an association "
        "between Class XII performance and entrance-examination performance."
    )
else:
    st.warning(
        "The test does not provide sufficient statistical evidence "
        "of an association between Class XII performance and entrance-examination performance."
    )


st.header("🔍 Question 3")

st.write(
    "3)Does reported coaching duration show different performance patterns❓"
)

q3 = pd.crosstab(
    filtered_df["time"],
    filtered_df["Performance"],
    normalize="index"
) * 100

st.bar_chart(q3)
st.subheader("Coaching Duration vs Performance (%)")

st.dataframe(
    q3.round(2),
    use_container_width=True
)

chi2, p_value, dof, expected = chi2_contingency(
    pd.crosstab(
        filtered_df["time"],
        filtered_df["Performance"]
    )
)
st.header("Statistical Evidence")
st.write(f"Chi-square statistic: **{chi2:.2f}**")
st.write(f"P-value: **{p_value:.4f}**")
if p_value < 0.05:
    st.success(
        "The test provides statistical evidence of an association "
        "between coaching duration and entrance-examination performance."
    )
else:
    st.warning(
        "The test does not provide sufficient statistical evidence "
        "of an association between coaching duration and entrance-examination performance."
    )

st.header("⚠️ Limitations")

st.markdown(
    """
    - The dataset is observational, so associations cannot
      establish causation.
    - Other variables may influence both preparation choices
      and examination performance.
    - The dataset represents a specific student population,
      so results may not generalize to all students.
    - Categorical performance measures may simplify differences
      between individual students.
    """
)

with st.expander("⭐ About this dataset"):

    st.write(
        """
        This project analyzes student performance data from
        an entrance-examination context.

        The analysis focuses on the relationship between
        coaching, academic preparation, coaching duration,
        and entrance-examination performance.
        """
    )


csv = filtered_df.to_csv(index=False)

st.download_button(
    label="⬇️ Download Filtered Data",
    data=csv,
    file_name="filtered_student_data.csv",
    mime="text/csv"
)