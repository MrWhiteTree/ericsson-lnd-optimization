import sqlite3
import pandas as pd

# Step 1: Connect to the SQLite database
conn = sqlite3.connect('ericsson.db')
cursor = conn.cursor()

# Step 2: Create the Engineers table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Engineers (
        Employee_ID INTEGER PRIMARY KEY,
        Age INTEGER,
        Career_Stage TEXT,
        Skills TEXT,
        Training_Participation INTEGER,
        Certifications INTEGER,
        Performance_Metrics REAL,
        Skill_Gaps TEXT
    )
''')
conn.commit()

# Step 3: Import data from CSV
df = pd.read_csv('ericsson_engineers.csv')
df.to_sql('Engineers', conn, if_exists='replace', index=False)

# Step 4: Run queries
query = '''
    SELECT 
        CASE 
            WHEN Age BETWEEN 25 AND 34 THEN '25-34'
            WHEN Age BETWEEN 35 AND 44 THEN '35-44'
            ELSE '45+'
        END AS Age_Group,
        AVG(Training_Participation) AS Avg_Training
    FROM Engineers
    GROUP BY Age_Group
'''
result = pd.read_sql(query, conn)
print(result)

# Step 5: Close the connection
conn.close()