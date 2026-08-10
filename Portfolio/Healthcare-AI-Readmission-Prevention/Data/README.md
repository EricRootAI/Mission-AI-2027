# Prototype Data

## Overview

The Healthcare AI Readmission Prevention prototype uses synthetic patient data to demonstrate an end-to-end AI consulting workflow for predicting 30-day hospital readmission risk.

No real patient information is used in this project.

## Dataset Purpose

The dataset is designed to simulate information that could reasonably be available during or near the time of a patient's hospital discharge.

The intended machine learning task is binary classification:

> Predict whether a patient will experience an unplanned hospital readmission within 30 days of discharge.

## Target Variable

The target variable is:

`readmitted_30_days`

Values:

- `0` = No readmission within 30 days
- `1` = Readmission within 30 days

## Dataset Characteristics

The prototype dataset includes synthetic variables representing:

- Patient demographics
- Hospitalization characteristics
- Previous healthcare utilization
- Clinical complexity
- Medication burden
- Care-management factors
- Follow-up planning

## Data Generation

The dataset will be generated programmatically using Python.

This approach provides:

- Reproducibility
- Transparency
- Privacy protection
- Consistent development data
- The ability to test different scenarios

## Responsible AI

The dataset is synthetic and is not representative of any specific hospital, patient population, or healthcare system.

Synthetic relationships between variables and outcomes are created for demonstration purposes and should not be interpreted as clinical evidence.

## Intended Use

This dataset is intended for:

- AI consulting portfolio demonstration
- Machine learning development
- Explainable AI experimentation
- Responsible AI analysis
- Workflow design
- Business case development

It is not intended for clinical use.
