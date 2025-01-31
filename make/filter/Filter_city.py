import json
# Define file paths
input_file = "urls.json"  # Replace with the path to your file containing the URLs
output_file = "biel-bienne.json"  # Replace with your desired output file path

# Load URLs from the JSON file
with open(input_file, "r") as file:
    data = json.load(file)  # Load the JSON content

# Assuming the URLs are in a list, adjust if your structure is different
urls = data if isinstance(data, list) else data.get("urls", [])

# Filter URLs that start with the specified string
filtered_urls = [url for url in urls if url.startswith("https://www.local.ch/de/d/bielbienne")]

# Save the filtered URLs in list format to a JSON file
with open(output_file, "w") as file:
    json.dump(filtered_urls, file, indent=2)

print(f"Filtered URLs saved to {output_file}")
