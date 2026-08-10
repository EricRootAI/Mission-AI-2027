# Healthcare AI Readmission Prevention
## Prototype Data Dictionary

### Purpose

This data dictionary defines the variables used by the Healthcare AI Readmission Prevention prototype.

The prototype is designed to estimate the likelihood that a hospitalized patient will experience an unplanned hospital readmission within 30 days of discharge.

All prototype data will be synthetic and is intended solely for educational, demonstration, and portfolio purposes.

---

## Target Variable

| Variable | Type | Description |
|---|---|---|
| readmitted_30_days | Binary | Indicates whether the patient was readmitted within 30 days of discharge. `0 = No`, `1 = Yes` |

---

## Patient Demographics

| Variable | Type | Description |
|---|---|---|
| patient_id | Integer | Synthetic identifier assigned to each patient |
| age | Integer | Patient age in years |
| gender | Categorical | Patient gender category |

---

## Hospitalization Information

| Variable | Type | Description |
|---|---|---|
| admission_type | Categorical | Type of hospital admission |
| length_of_stay | Integer | Number of days the patient remained hospitalized |
| discharge_disposition | Categorical | Patient disposition at discharge |

---

## Prior Healthcare Utilization

| Variable | Type | Description |
|---|---|---|
| prior_admissions | Integer | Number of hospital admissions during the previous 12 months |
| emergency_visits | Integer | Number of emergency department visits during the previous 12 months |
| outpatient_visits | Integer | Number of outpatient visits during the previous 12 months |

---

## Clinical Complexity Indicators

| Variable | Type | Description |
|---|---|---|
| number_of_diagnoses | Integer | Number of documented diagnoses associated with the hospitalization |
| chronic_condition_count | Integer | Number of chronic-condition indicators represented in the patient's synthetic record |
| medication_count | Integer | Number of medications documented at discharge |
| prior_readmission | Binary | Indicates whether the patient experienced a prior readmission |

---

## Social and Care Factors

| Variable | Type | Description |
|---|---|---|
| follow_up_scheduled | Binary | Indicates whether a follow-up appointment was scheduled before discharge |
| care_management_enrolled | Binary | Indicates whether the patient was enrolled in a care-management program |

---

## Responsible AI Considerations

The prototype intentionally uses synthetic data and does not contain real patient information.

Demographic variables may be included for analytical and fairness evaluation purposes. They should not automatically be treated as predictive features without appropriate responsible AI review.

Model development will include consideration of:

- Bias
- Fairness
- Explainability
- Data quality
- Feature appropriateness
- Privacy
- Human oversight

---

## Important Disclaimer

This dataset and prototype are not intended for clinical decision-making, diagnosis, treatment recommendations, or deployment in a healthcare environment.

The system is a portfolio demonstration of an AI consulting methodology.
