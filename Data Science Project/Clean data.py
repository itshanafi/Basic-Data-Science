import pandas as pd
import numpy as np

# Define the file paths and names
clean_data_file = 'D:\\Lab\\Basic-Data-Science\\Basic-Data-Science\\Data Science Project\\Malaysia Restaurant Review Datasets\\data_cleaned\\GoogleReview_data_cleaned.csv'
raw_data_file = 'D:\\Lab\\Basic-Data-Science\\Basic-Data-Science\\Data Science Project\\Malaysia Restaurant Review Datasets\\data\\restaurant\\Restaurants_Shah Alam.csv'

# Read the clean data CSV file
clean_data = pd.read_csv(clean_data_file)

# Read the raw data CSV file
raw_data = pd.read_csv(raw_data_file)

# Create a new column in clean data to store the URLs (if it doesn't exist)
if 'url' not in clean_data.columns:
    clean_data['url'] = None

# Ensure 'url' column in clean_data is initially set to be of type 'object' (typically string)
clean_data['url'] = clean_data['url'].astype(object)

# Iterate over each row in the 'Restaurant' column of clean data
for index, row in clean_data.iterrows():
    restaurant_name = row['Restaurant'].capitalize().strip()  # Strip extra spaces
    # Check if the restaurant name exists in the 'Restaurant' column of raw data
    matching_rows = raw_data[raw_data['Restaurant'].str.strip().str.capitalize() == restaurant_name]
    if not matching_rows.empty:
        # Get the URL from the matching row in raw data
        url = matching_rows.iloc[0]['url']
        # Update the 'url' column in clean data
        clean_data.at[index, 'url'] = url if pd.notna(url) else None  # Use None instead of np.nan for string columns
    else:
        print(f"No match found for restaurant '{restaurant_name}'")

# Update the clean data CSV file
clean_data.to_csv(clean_data_file, index=False)

print("Clean data updated and saved to", clean_data_file)
