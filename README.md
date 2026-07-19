# diabetes-readmission-prediction
Machine learning pipeline to predict 30-day hospital readmission risk among patients with diabetes using clinical and healthcare utilization data.
https://diabetes-readmission-prediction-x7rqhrfmcyz3r2t88rkhzz.streamlit.app/

# Diabetes 30-Day Readmission Risk Prediction

## Project Overview

This project develops a machine learning model to predict the risk of 30-day hospital readmission among patients with diabetes using clinical and hospital utilization data.

The goal is to identify patient characteristics associated with increased readmission risk and develop an interpretable prediction tool that can support clinical decision-making.

## Research Question

Can machine learning models predict the likelihood of 30-day hospital readmission among patients with diabetes using clinical and utilization-related features?

## Dataset

Dataset:
UCI Diabetes 130-US Hospitals for Years 1999-2008

The dataset contains hospital encounters for patients with diabetes and includes demographic information, laboratory results, medications, and utilization variables.

The prediction target was:

- 1: Readmitted within 30 days
- 0: Not readmitted within 30 days

## Clinical Cohort Definition

The analysis focused on emergency admissions involving patients with diabetes.

Patients were identified using ICD-9 diabetes diagnosis codes beginning with "250%" and admission characteristics relevant to acute care utilization.

## Machine Learning Workflow

1. Data extraction and cleaning
2. Missing value and data quality assessment
3. Exploratory data analysis
4. Feature engineering
5. Train/test split
6. Model development
7. Model evaluation
8. Clinical interpretation
9. Streamlit deployment
