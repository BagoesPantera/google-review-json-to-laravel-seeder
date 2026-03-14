import json

# Fungsi untuk escape single quotes dalam string
def escape_quotes(text):
    return str(text).replace("'", "\\'")

# Fungsi konversi JSON ke Laravel Seeder
def convert_to_laravel_seeder(json_array):
    output = "array (\n"
    
    for index, item in enumerate(json_array):
        output += f"{index} =>\n"
        output += "array (\n"
        output += f"'id' => {index + 1},\n"
        output += f"'name' => '{escape_quotes(item.get('name', ''))}',\n"
        output += f"'message' => '{escape_quotes(item.get('text', ''))}',\n"
        output += f"'rating' => {item.get('stars', 0)},\n"
        output += f"'review_url' => '{escape_quotes(item.get('reviewUrl', ''))}',\n"
        output += "),\n"
    
    output += ")"
    return output

# Baca file JSON
try:
    with open('reviews.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    
    # Generate hasil konversi
    result = convert_to_laravel_seeder(json_data)
    
    # Simpan ke file output
    with open('seeder_output.php', 'w', encoding='utf-8') as file:
        file.write(result)
    
    print("✓ Seeder berhasil dibuat!")
    print("File output: seeder_output.php\n")
    print(result)

except FileNotFoundError:
    print("✗ Error: File 'reviews.json' tidak ditemukan!")
except json.JSONDecodeError:
    print("✗ Error: Format JSON tidak valid!")
except Exception as e:
    print(f"✗ Error: {str(e)}")
