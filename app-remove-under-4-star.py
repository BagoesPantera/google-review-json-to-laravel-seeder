import json

# Fungsi untuk escape single quotes dalam string
def escape_quotes(text):
    return str(text).replace("'", "\\'")

# Fungsi untuk validasi rating (hanya accept 1-5, sisanya NULL)
def validate_rating(stars):
    try:
        rating = int(stars)
        if 1 <= rating <= 5:
            return rating
        else:
            return "NULL"
    except (ValueError, TypeError):
        return "NULL"

# Fungsi konversi JSON ke Laravel Seeder
def convert_to_laravel_seeder(json_array):
    output = "array (\n"
    id_counter = 1

    for item in json_array:
        rating = validate_rating(item.get('stars'))

        # Filter: hanya masukkan yang rating 4 atau 5
        if rating == "NULL" or rating < 4:
            continue

        # Filter: skip jika text kosong atau "None"
        text = item.get('text', '')
        if not text or str(text).strip().lower() == 'none':
            continue

        output += f"{id_counter - 1} =>\n"
        output += "array (\n"
        output += f"'id' => {id_counter},\n"
        output += f"'name' => '{escape_quotes(item.get('name', ''))}',\n"
        output += f"'message' => '{escape_quotes(text)}',\n"
        output += f"'rating' => {rating},\n"
        output += f"'review_url' => '{escape_quotes(item.get('reviewUrl', ''))}',\n"
        output += f"'created_at' => ($date = Carbon::now()->subDays(rand(0, 365))),\n"
        output += f"'updated_at' => $date,\n"
        output += "),\n"

        id_counter += 1

    output += ")"
    return output

# Baca file JSON
try:
    with open('review.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    # Generate hasil konversi
    result = convert_to_laravel_seeder(json_data)

    # Simpan ke file output
    with open('seeder_output.php', 'w', encoding='utf-8') as file:
        file.write(result)

    print("✓ Seeder berhasil dibuat!")
    print("File output: seeder_output.php")
    print("Filter: Hanya stars 4 dan 5\n")
    print(result)

except FileNotFoundError:
    print("✗ Error: File 'review.json' tidak ditemukan!")
except json.JSONDecodeError:
    print("✗ Error: Format JSON tidak valid!")
except Exception as e:
    print(f"✗ Error: {str(e)}")