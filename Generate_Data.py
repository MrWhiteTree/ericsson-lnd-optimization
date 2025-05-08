import pandas as pd
import numpy as np

# Define the fields and data types
data = {
    'Employee_ID': range(1, 6001),  # 6000 employees
    'Age': np.random.randint(18, 60, 6000),  # Random ages between 18 and 60
    'Career_Stage': np.random.choice(['Entry-Level', 'Mid-Career', 'Senior'], 6000),
    'Skills': np.random.choice(['5G', 'AI/ML', 'Cybersecurity', 'Leadership'], 6000),
    'Training_Participation': np.random.randint(0, 600, 6000),  # Random training participation
    'Certifications': np.random.randint(0, 5, 6000),  # Random certifications
    'Performance_Metrics': np.random.uniform(0, 1, 6000),  # Random performance scores
    'Skill_Gaps': np.random.choice(['5G', 'AI/ML', 'Cybersecurity', 'Leadership'], 6000)
}

# Debug: Print the length of each array
for key, value in data.items():
    print(f"{key}: {len(value)}")
    
# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('ericsson_engineers.csv', index=False)

print("Dataset created successfully!")

df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)
