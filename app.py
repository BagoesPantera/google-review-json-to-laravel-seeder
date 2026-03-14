import json

# Data JSON kamu
json_data = [
    {
        "title": "title",
        "url": "url",
        "stars": 5,
        "name": "Tracy James",
        "reviewUrl": "url",
        "text": "the review"
    }
]

# Konversi ke format Laravel Seeder
def convert_to_laravel_seeder(json_array):
    output = "array (\n"
    
    for index, item in enumerate(json_array):
        output += f"{index} =>\n"
        output += "array (\n"
        output += f"'id' => {index + 1},\n"
        output += f"'name' => '{item.get('name', '')}',\n"
        output += f"'message' => '{item.get('text', '')}',\n"
        output += f"'rating' => {item.get('stars', 0)},\n"
        output += f"'review_url' => '{item.get('reviewUrl', '')}',\n"
        output += "),\n"
    
    output += ")"
    return output

# Generate hasil konversi
result = convert_to_laravel_seeder(json_data)
print(result)
