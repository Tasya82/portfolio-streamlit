import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def show_project():
    st.header("Calculation average job satisfaction for top 10 and others")

    df_hrd = pd.read_csv('D:\\Data Science\\D40\\HRDataset_v14.csv')

    top_10_salary = df_hrd.nlargest(10, 'Salary')

    top_10_satisfaction = top_10_salary['EmpSatisfaction'].mean()
    others_satisfaction = df_hrd.loc[~df_hrd.index.isin(top_10_salary.index), 'EmpSatisfaction'].mean()

    satisfaction_data = pd.DataFrame({
        'Group': ['Top 10 Salaries', 'Others'],
        'Average Satisfaction': [top_10_satisfaction, others_satisfaction]
    })

    st.bar_chart(satisfaction_data)

    st.write("Average Satisfaction for Top 10 Highest-Paid Employees: 4.2. This indicates that the top 10 highest-paid employees have relatively high job satisfaction on average.")
    st.write("Average Satisfaction for Other Employees: 3.88. This shows that employees outside the top 10 also report moderate satisfaction but at a slightly lower level than the highest-paid group.")

    st.header("Group by Recruitment Source")

    from datetime import datetime

    # Convert 'DateofTermination' and 'DateofHire' columns to datetime
    df_hrd['DateofHire'] = pd.to_datetime(df_hrd['DateofHire'], errors='coerce')  # Convert to datetime
    df_hrd['DateofTermination'] = pd.to_datetime(df_hrd['DateofTermination'], errors='coerce')  # Convert to datetime

    # Calculate Tenure
    current_date = datetime.now()
    df_hrd['Tenure'] = (df_hrd['DateofTermination'].fillna(current_date) - df_hrd['DateofHire']).dt.days / 365.25

    grouped = df_hrd.groupby('RecruitmentSource').agg({
        'Tenure': 'mean',
        'PerformanceScore': lambda x: x.astype(str).replace({'Needs Improvement': '1', 'Fully Meets': '2', 'Exceeds': '3', 'PIP': '1'}).astype(int).mean()
    }).reset_index()

    grouped.rename(columns={'Tenure': 'Avg_Tenure', 'PerformanceScore': 'Avg_Performance'}, inplace=True)

    st.write(grouped)

    long_text = 'Employee Referral stands out as the best recruitment source because it has the highest average tenure (9.52 years) and the highest average performance score (2.13). This source likely brings in employees who are both loyal and effective. CareerBuilder has the lowest performance score (1.91) and relatively moderate tenure (8.13 years). Efforts could focus on improving recruitment strategies for this source, such as refining job descriptions or targeting candidates with better qualifications. Indeed strikes a balance between long tenure (9.22 years) and decent performance (2.03), making it a reliable source for recruiting long-term employees.'

    st.markdown("**Insight**: " + long_text)

    # Tenure Bar Chart
    sns.barplot(data=grouped, x='RecruitmentSource', y='Avg_Tenure', palette='Blues_d')
    plt.title('Average Tenure by Recruitment Source')
    plt.xticks(rotation=90)
    st.pyplot(plt)

    # Performance Bar Chart
    sns.barplot(data=grouped, x='RecruitmentSource', y='Avg_Performance', palette='Greens_d')
    plt.title('Average Performance by Recruitment Source')
    plt.xticks(rotation=90)
    st.pyplot(plt)

    st.header("Does race, ethnicity, or gender affect engagement survey scores, satisfaction, or performance ratings?")

    race_stats = df_hrd.groupby('RaceDesc')[['EngagementSurvey', 'EmpSatisfaction', 'PerformanceScore']].agg({'PerformanceScore': lambda x: x.astype(str).replace({'Needs Improvement': 1, 'Fully Meets': 2, 'Exceeds': 3, 'PIP': 1}).astype(int).mean(),'EngagementSurvey':'mean','EmpSatisfaction':'mean'})
    gender_stats = df_hrd.groupby('Sex')[['EngagementSurvey', 'EmpSatisfaction', 'PerformanceScore']].agg({'PerformanceScore': lambda x: x.astype(str).replace({'Needs Improvement': 1, 'Fully Meets': 2, 'Exceeds': 3, 'PIP': 1}).astype(int).mean(),'EngagementSurvey':'mean','EmpSatisfaction':'mean'})
    ethnicity_stats = df_hrd.groupby('HispanicLatino')[['EngagementSurvey', 'EmpSatisfaction', 'PerformanceScore']].agg({'PerformanceScore': lambda x: x.astype(str).replace({'Needs Improvement': 1, 'Fully Meets': 2, 'Exceeds': 3, 'PIP': 1}).astype(int).mean(),'EngagementSurvey':'mean','EmpSatisfaction':'mean'})

    st.write(race_stats)
    st.write(gender_stats)
    st.write(ethnicity_stats)

    long_text = 'Race-based findings: American Indian or Alaska Native employees have high performance and satisfaction but lower engagement scores. Hispanic employees have high engagement but report the lowest satisfaction, which might indicate they feel engaged but not completely satisfied with the work environment or company culture. Two or more races employees report the lowest performance, engagement, and slightly above average satisfaction, which suggests they may need additional attention or support. Gender-based findings: No major differences between male and female employees in terms of performance or engagement. However, females report slightly higher job satisfaction. Ethnicity-based findings: Hispanic employees have higher engagement and slightly lower satisfaction than their non-Hispanic counterparts. This suggests the need for deeper investigation into factors affecting satisfaction.'

    st.markdown("**Insight**: " + long_text)
