import json; 
with open("owid-co2-data.json", 'r') as f_in: 
    data = json.load(f_in)
with open('data.json', 'w') as f_out: 
    json.dump(data, f_out, separators=(',', ':'))