import pandas as pd

# Sample accident data with required columns
sample_data = pd.DataFrame({
    'State': ['CA', 'CA', 'TX', 'TX', 'NY'],
    'Severity': [2.5, 3.0, 2.0, 1.5, 2.0],
    'Start_Time': [
        '2023-06-01 08:00:00',
        '2023-06-01 14:30:00',
        '2023-06-02 07:15:00',
        '2023-06-02 21:00:00',
        '2023-06-03 10:45:00'
    ],
    'Weather_Condition': ['Clear', 'Rain', 'Cloudy', 'Clear', 'Fog']
})

# Save it to disk
sample_data.to_csv('data/sample_accidents.csv', index=False)
