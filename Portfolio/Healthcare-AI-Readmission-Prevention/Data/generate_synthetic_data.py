import numpy as np
import pandas as pd

# Reproducibility
np.random.seed(42)

# Number of synthetic patients
N_PATIENTS = 2000

# ---------------------------------------------------------
# Generate synthetic patient characteristics
# ---------------------------------------------------------

patient_id = np.arange(100001, 100001 + N_PATIENTS)

age = np.random.randint(18, 91, N_PATIENTS)

gender = np.random.choice(
    ["Female", "Male"],
    size=N_PATIENTS
)

admission_type = np.random.choice(
    ["Emergency", "Urgent", "Elective"],
    size=N_PATIENTS,
    p=[0.55, 0.25, 0.20]
)

length_of_stay = np.random.poisson(
    lam=4,
    size=N_PATIENTS
) + 1

prior_admissions = np.random.poisson(
    lam=0.8,
    size=N_PATIENTS
)

emergency_visits = np.random.poisson(
    lam=1.2,
    size=N_PATIENTS
)

outpatient_visits = np.random.poisson(
    lam=3.0,
    size=N_PATIENTS
)

number_of_diagnoses = np.random.randint(
    1,
    9,
    N_PATIENTS
)

chronic_condition_count = np.random.randint(
    0,
    6,
    N_PATIENTS
)

medication_count = np.random.randint(
    1,
    16,
    N_PATIENTS
)

prior_readmission = np.random.binomial(
    1,
    0.20,
    N_PATIENTS
)

follow_up_scheduled = np.random.binomial(
    1,
    0.75,
    N_PATIENTS
)

care_management_enrolled = np.random.binomial(
    1,
    0.35,
    N_PATIENTS
)

discharge_disposition = np.random.choice(
    [
        "Home",
        "Home Health",
        "Skilled Nursing Facility",
        "Rehabilitation"
    ],
    size=N_PATIENTS,
    p=[0.65, 0.15, 0.12, 0.08]
)

# ---------------------------------------------------------
# Generate synthetic readmission risk
# ---------------------------------------------------------

risk_score = (
    -3.0
    + (age * 0.015)
    + (length_of_stay * 0.12)
    + (prior_admissions * 0.45)
    + (emergency_visits * 0.25)
    + (number_of_diagnoses * 0.12)
    + (chronic_condition_count * 0.20)
    + (medication_count * 0.04)
    + (prior_readmission * 0.90)
    - (follow_up_scheduled * 0.35)
    - (care_management_enrolled * 0.25)
)

# Convert risk score into probability
readmission_probability = 1 / (
    1 + np.exp(-risk_score)
)

# Generate binary outcome
readmitted_30_days = np.random.binomial(
    1,
    readmission_probability
)

# ---------------------------------------------------------
# Build dataset
# ---------------------------------------------------------

df = pd.DataFrame({
    "patient_id": patient_id,
    "age": age,
    "gender": gender,
    "admission_type": admission_type,
    "length_of_stay": length_of_stay,
    "prior_admissions": prior_admissions,
    "emergency_visits": emergency_visits,
    "outpatient_visits": outpatient_visits,
    "number_of_diagnoses": number_of_diagnoses,
    "chronic_condition_count": chronic_condition_count,
    "medication_count": medication_count,
    "prior_readmission": prior_readmission,
    "follow_up_scheduled": follow_up_scheduled,
    "care_management_enrolled": care_management_enrolled,
    "discharge_disposition": discharge_disposition,
    "readmitted_30_days": readmitted_30_days
})

# ---------------------------------------------------------
# Save dataset
# ---------------------------------------------------------

output_file = "sample_patient_data.csv"

df.to_csv(
    output_file,
    index=False
)

print("Synthetic dataset created successfully.")
print(f"Patients generated: {len(df)}")
print(f"Dataset saved to: {output_file}")

print("\nReadmission distribution:")
print(df["readmitted_30_days"].value_counts())

print("\nReadmission percentage:")
print(df["readmitted_30_days"].mean() * 100)
