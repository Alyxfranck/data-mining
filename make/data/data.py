# this script acts as a data prcessing unit 
import json
import pandas as pd
import re

# Step 1: Load data from 'contact_data.json'
with open('contact_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Initialize a list to hold parsed data
parsed_data = []

for entry in data:
    url = entry.get('url', '')
    business_name = entry.get('business_name', '')
    contact_info = entry.get('contact', '')

    # Step 2: Parse the contact information
    # Replace multiple spaces and tabs with a single tab
    contact_info = re.sub(r'[\t ]+', '\t', contact_info.strip())
    contact_fields = contact_info.split('\t')

    contact_dict = {}
    key = None
    for field in contact_fields:
        field = field.strip()
        # If the field is a key, set it as the current key
        if field in ['Adresse', 'Telefon', 'Mobiltelefon', 'Fax', 'Email', 'Website', 'Postfach',]:
            key = field
            # Initialize the key in contact_dict if not already present
            if key not in contact_dict:
                contact_dict[key] = ''
        elif key:
            # Append the value to the current key
            if contact_dict[key]:
                contact_dict[key] += ' ' + field
            else:
                contact_dict[key] = field

    # Step 3: Organize data into a dictionary
    data_dict = {
        'URL': url,
        'Business Name': business_name,
        'Address': contact_dict.get('Adresse', ''),
        'Telephone': contact_dict.get('Telefon', ''),
        'Mobile Phone': contact_dict.get('Mobiltelefon', ''),
        'Fax': contact_dict.get('Fax', ''),
        'Email': contact_dict.get('Email', ''),
        'Website': contact_dict.get('Website', ''),
        
    }

    # Handle special cases where the contact info is missing
    if not contact_info or 'No contact available' in contact_info:
        data_dict['Other Info'] = 'No contact information available'

    # For entries with special keys like 'Zu Favoriten hinzufügen', 'Teilen', etc.
    if 'Zu Favoriten hinzufügen' in contact_dict:
        data_dict['Other Info'] = 'Entry contains special instructions or missing contact info'

    parsed_data.append(data_dict)

# Step 4: Create a DataFrame
df = pd.DataFrame(parsed_data)

# Step 5: Sort the DataFrame by Business Name
df.sort_values(by='Business Name', inplace=True)

# Step 6: Export to Excel
df.to_excel('sorted_business_data.xlsx', index=False)

print("Data has been parsed, sorted, and exported to 'data.xlsx'.")
