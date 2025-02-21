import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
import os

# Load the Titanic dataset
df = pd.read_csv("data/titanic.csv")

# Handle missing values in 'age' and 'Fare' columns
    df['Age'].fillna(df['Age'].median(), inplace=True)
    df['Fare'].fillna(df['Fare'].median(), inplace=True)

def analyze_data(question: str):
    
    if not os.path.exists("images"):
        os.makedirs("images")

    # Question 1: What percentage of passengers were male?
    if "percentage of passengers were male" in question.lower():
        male_percentage = (df['Sex'].value_counts(normalize=True)['male'] * 100)
        return f"{male_percentage:.2f}% of passengers were male."

    # Question 2: Show a histogram of passenger ages
    if "histogram of passenger ages" in question.lower():
        plt.figure(figsize=(8, 6))
        plt.hist(df['Age'], bins=20, color='blue', edgecolor='black')
        plt.title('Passenger Age Distribution')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        image_path = "images/histogram_age.png"
        plt.savefig(image_path)
        plt.close()
        return image_path  # Return the path to the saved image

    # Question 3: What was the average ticket Fare?
    elif "average ticket fare" in question.lower():
        avg_fare = df['Fare'].mean()
        return f"The average ticket Fare was ${avg_fare:.2f}."

    # Question 4: How many passengers embarked from each port?
    elif "passengers embarked from each port" in question.lower():
        embark_counts = df['Embarked'].value_counts()
        return embark_counts.to_string()


    # Question 5: How many passengers are from each Pclass?
    elif "passengers are from each pclass" in question.lower():
        pclass_counts = df['Pclass'].value_counts().sort_index()
        return f"Passengers by class:\nPclass 1: {pclass_counts[1]}\nPclass 2: {pclass_counts[2]}\nPclass 3: {pclass_counts[3]}"

    # Question 6: What is the survival rate for each passenger class?
    elif "survival rate for each passenger class" in question.lower():
        survival_rate = df.groupby('Pclass')['Survived'].mean() * 100
        return f"Survival rate by class:\nPclass 1: {survival_rate[1]:.2f}%\nPclass 2: {survival_rate[2]:.2f}%\nPclass 3: {survival_rate[3]:.2f}%"

    # Question 7: What is the distribution of passengers by gender?
    elif "distribution of passengers by gender" in question.lower():
        gender_distribution = df['Sex'].value_counts()
        return gender_distribution.to_string()

    # Question 8: What is the average age of passengers?
    elif "average age of passengers" in question.lower():
        avg_age = df['Age'].mean()
        return f"The average age of passengers was {avg_age:.2f} years."

    # Question 9: How many passengers Survived vs. did not survive?
    elif "passengers survived vs. did not survive" in question.lower():
        survival_counts = df['Survived'].value_counts()
        return f"Survival counts:\nSurvived: {survival_counts[1]}\nDid not survive: {survival_counts[0]}"

    # Question 10: What is the highest fare paid by a passenger?
    elif "highest fare paid by a passenger" in question.lower():
        max_fare = df['Fare'].max()
        return f"The highest fare paid by a passenger was ${max_fare:.2f}."

    # Question 11: What is the survival rate by gender?
    elif "survival rate by gender" in question.lower():
        survival_rate_gender = df.groupby('Sex')['Survived'].mean() * 100
        return f"Survival rate by gender:\nMale: {survival_rate_gender['male']:.2f}%\nFemale: {survival_rate_gender['female']:.2f}%"

    # Question 12: How many passengers traveled alone?
    elif "passengers traveled alone" in question.lower():
        alone_passengers = df[(df['SibSp'] == 0) & (df['Parch'] == 0)].shape[0]
        return f"{alone_passengers} passengers traveled alone."

    # Question 13: What is the age distribution of survivors vs. non-survivors?
    elif "age distribution of survivors vs. non-survivors" in question.lower():
        plt.figure(figsize=(8, 6))
        plt.hist(df[df['Survived'] == 1]['Age'], bins=20, alpha=0.5, label='Survived')
        plt.hist(df[df['Survived'] == 0]['Age'], bins=20, alpha=0.5, label='Did not survive')
        plt.title('Age Distribution of Survivors vs. Non-Survivors')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.legend()
        image_path = "images/histogram_survival_age.png"
        plt.savefig(image_path)
        plt.close()
        return image_path  # Return the path to the saved image

    # Question 14: What is the average fare for each passenger class?
    elif "average fare for each passenger class" in question.lower():
        avg_Fare_class = df.groupby('Pclass')['Fare'].mean()
        return f"Average fare by class:\nPclass 1: ${avg_Fare_class[1]:.2f}\nPclass 2: ${avg_Fare_class[2]:.2f}\nPclass 3: ${avg_Fare_class[3]:.2f}"

    # Question 15: How many children (age < 18) were on board?
    elif "children were on board" in question.lower():
        children_count = df[df['Age'] < 18].shape[0]
        return f"There were {children_count} children (age < 18) on board."

    # Question 16: What is the survival rate of children?
    elif "survival rate of children" in question.lower():
        children_survival_rate = df[df['Age'] < 18]['Survived'].mean() * 100
        return f"The survival rate of children (Age < 18) was {children_survival_rate:.2f}%."

    # Question 17: How many passengers had siblings/spouses on board?
    elif "passengers had siblings/spouses on board" in question.lower():
        SibSp_count = df[df['SibSp'] > 0].shape[0]
        return f"{SibSp_count} passengers had siblings/spouses on board."

    # Question 18: How many passengers had parents/children on board?
    elif "passengers had parents/children on board" in question.lower():
        Parch_count = df[df['Parch'] > 0].shape[0]
        return f"{Parch_count} passengers had parents/children on board."

    # Question 19: What is the survival rate of passengers with siblings/spouses?
    elif "survival rate of passengers with siblings/spouses" in question.lower():
        SibSp_survival_rate = df[df['SibSp'] > 0]['Survived'].mean() * 100
        return f"The survival rate of passengers with siblings/spouses was {SibSp_survival_rate:.2f}%."

    # Question 20: What is the survival rate of passengers with parents/children?
    elif "survival rate of passengers with parents/children" in question.lower():
        Parch_survival_rate = df[df['Parch'] > 0]['Survived'].mean() * 100
        return f"The survival rate of passengers with parents/children was {Parch_survival_rate:.2f}%."

    # Question 21: What is the median age of passengers?
    elif "median age of passengers" in question.lower():
        median_age = df['Age'].median()
        return f"The median age of passengers was {median_age:.2f} years."

    # Question 22: What is the survival rate of passengers in each age group?
    elif "survival rate of passengers in each age group" in question.lower():
        df['age_group'] = pd.cut(df['Age'], bins=[0, 18, 30, 50, 100], labels=['Child', 'Young Adult', 'Adult', 'Senior'])
        age_group_survival = df.groupby('age_group')['Survived'].mean() * 100
        return age_group_survival.to_string()

    # Question 23: How many passengers were in each age group?
    elif "passengers were in each age group" in question.lower():
        df['age_group'] = pd.cut(df['Age'], bins=[0, 18, 30, 50, 100], labels=['Child', 'Young Adult', 'Adult', 'Senior'])
        age_group_counts = df['age_group'].value_counts()
        return f"Passengers in each age group:\n{age_group_counts}"

    # Question 24: What is the survival rate of passengers by embarkation port?
    elif "survival rate of passengers by embarkation port" in question.lower():
        embark_survival = df.groupby('Embarked')['Survived'].mean() * 100
        return embark_survival.to_string()

    # Question 25: How many passengers had a cabin assigned?
    elif "passengers had a cabin assigned" in question.lower():
        cabin_assigned = df['Cabin'].notna().sum()
        return f"{cabin_assigned} passengers had a cabin assigned."

    # Default response if the question is not recognized
    else:
        return "Sorry, I couldn't understand your question. Please try asking something else."
