import pandas as pd

# Replace 'input_file.xlsx' with the path to your Excel file
input_file = 'ParkingViolationCodes_March_2024.xlsx'
# Replace 'output_file.csv' with the desired name for the CSV file
output_file = 'ParkingViolationCodes_March_2024.csv'

# Read Excel file
df = pd.read_excel(input_file)

# Write DataFrame to CSV file
df.to_csv(output_file, index=False)

