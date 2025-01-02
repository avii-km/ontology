import json

def filter_and_clean_json(data, necessary_attributes):
    """
    Filters and cleans JSON data to retain only necessary attributes for ontology creation.
    """
    if isinstance(data, dict):
        return {
            key: filter_and_clean_json(value, necessary_attributes)
            for key, value in data.items()
            if key in necessary_attributes or isinstance(value, dict)
        }
    elif isinstance(data, list):
        # Remove duplicates and clean items
        return list({json.dumps(item): item for item in data}.values())
    elif isinstance(data, str):
        return data.strip()  # Clean strings
    else:
        return data

# Necessary attributes for the ontology
necessary_attributes = {
    'Belt',
    'Bottom Type',
    'Category',
    'Chest pad',
    'Closure',
    'Collar',
    'Color',
    'Dresses Length',
    'Dresses Sleeve Length',
    'Fabric',
    'Features',
    'Fit',
    'Fit Type',
    'Gloves Material',
    'Hem Shaped',
    'Imported',
    'Length',
    'Material',
    'Neckline',
    'Occasion',
    'Outerwear Length',
    'Outerwear Sleeve Length',
    'Pants Length',
    'Pattern Type',
    'Placket',
    'Plating',
    'Pockets',
    'Room',
    'Shape',
    'Skirts Length',
    'Skirts Material',
    'Sleeve Length',
    'Sleeve Type',
    'Special Features',
    'Stone Type',
    'Style',
    'Tops Composition',
    'Tops Length',
    'Tops Material',
    'Tops Sleeve Length',
    'Tops Style',
    'Trends',
    'Type',
    'Waist Line',
    'Women Panties Material'
}



# Open the file with the correct encoding
with open('ontology.json', 'r', encoding='utf-8') as file:
    ontology_data = json.load(file)

# Filter and clean the data
filtered_data = filter_and_clean_json(ontology_data, necessary_attributes)

# Save the filtered and cleaned data to a new file
with open("filtered_ontology.json", "w") as file:
    json.dump(filtered_data, file, indent=4)

print("Necessary attributes for ontology creation have been filtered and saved as 'filtered_ontology.json'.")
