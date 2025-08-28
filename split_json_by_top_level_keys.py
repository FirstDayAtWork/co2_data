import json, os

def split_json_by_top_level_keys(input_json_path, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with open(input_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for key, value in data.items():
        output_data = {key: value}
        output_filename = os.path.join(output_directory, f"{key}.json")

        with open(output_filename, 'w', encoding='utf-8') as outfile:
            json.dump(output_data, outfile, separators=(',', ':'))

input_file = "owid-co2-data.json"
output_dir = "countries"
split_json_by_top_level_keys(input_file, output_dir)