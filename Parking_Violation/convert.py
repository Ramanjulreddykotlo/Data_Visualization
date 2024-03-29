# covert file xlsx to csv file
import pandas as pd
# xlsx file 
input_file = 'ParkingViolationCodes_March_2024.xlsx'
# csv file
output_file = 'ParkingViolationCodes_March_2024.csv'

# Read Excel file
df = pd.read_excel(input_file)

# Write DataFrame to CSV file
df.to_csv(output_file, index=False)

