

import pandas as pd

# Load dataset
df = pd.read_csv("/home/codingcops/Downloads/titanic.csv")


# ------------------------------------------------------
# 1. Survival counts and percentages
# ------------------------------------------------------
print("Survival Counts and Percentages")

counts = df["Survived"].value_counts()
percentages = df["Survived"].value_counts(normalize=True) * 100

print("Counts:\n", counts)
print("\nPercentages:\n", percentages.round(2), "%\n")


# ------------------------------------------------------
# 2. Survival rate by passenger class
# ------------------------------------------------------
print("Survival Rate by Passenger Class")

class_survival = df.groupby("Pclass")["Survived"].mean() * 100
print(class_survival.round(2), "%\n")


# ------------------------------------------------------
# 3. Average age of survivors vs non-survivors
# ------------------------------------------------------
print("Average Age (Survived vs Not)")

avg_age = df.groupby("Survived")["Age"].mean()
print(avg_age.round(2), "\n")


# ------------------------------------------------------
# 4. Embarkation port with highest survival rate
# ------------------------------------------------------
print("Survival Rate by Embarkation Port")

port_survival = df.groupby("Embarked")["Survived"].mean() * 100
print(port_survival.round(2))

best_port = port_survival.idxmax()
print(f"Highest Survival Port: {best_port}\n")


# ------------------------------------------------------
# 5. Missing ages + fill with median by class
# ------------------------------------------------------
print("Missing Age Handling")

missing_age = df["Age"].isnull().sum()
print("Missing Age Values:", missing_age)

# Fill missing age with median of each class
df["Age"] = df.groupby("Pclass")["Age"].transform(
    lambda x: x.fillna(x.median())
)

print("Missing Age After Filling:", df["Age"].isnull().sum(), "\n")


# ------------------------------------------------------
# 6. Oldest surviving passenger
# ------------------------------------------------------
print("Oldest Surviving Passenger")

survivors = df[df["Survived"] == 1]
oldest = survivors.loc[survivors["Age"].idxmax()]

print("Name:", oldest["Name"])
print("Age:", oldest["Age"])
print("Class:", oldest["Pclass"], "\n")


# ------------------------------------------------------
# 7. Survival % of women vs men
# ------------------------------------------------------
print("Survival % by Gender")

gender_survival = df.groupby("Sex")["Survived"].mean() * 100
print(gender_survival.round(2), "%\n")


# ------------------------------------------------------
# 8. Age Group + survival rate
# ------------------------------------------------------
print("Survival Rate by Age Group")

def get_age_group(age):
    if age < 18:
        return "Child"
    elif age <= 60:
        return "Adult"
    else:
        return "Senior"

df["AgeGroup"] = df["Age"].apply(get_age_group)

age_group_survival = df.groupby("AgeGroup")["Survived"].mean() * 100
print(age_group_survival.round(2), "%\n")


# ------------------------------------------------------
# 9. 3rd class survival (men vs women)
# ------------------------------------------------------
print("3rd Class Survival (Men vs Women)")

third_class = df[df["Pclass"] == 3]
third_survival = third_class.groupby("Sex")["Survived"].mean() * 100

print(third_survival.round(2), "%\n")


# ------------------------------------------------------
# 10. Drop missing Cabin rows
# ------------------------------------------------------
print("Cabin Data Cleaning")

original_rows = len(df)

df_no_cabin = df.dropna(subset=["Cabin"])
remaining_rows = len(df_no_cabin)

percentage_kept = (remaining_rows / original_rows) * 100

print("Remaining Rows:", remaining_rows)
print("Percentage Kept:", round(percentage_kept, 2), "%\n")


