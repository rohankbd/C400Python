import requests

url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"
response = requests.get(url)

csv_file = "/tmp/taxi_zone_lookup.csv"
with open(csv_file, "wb") as file:
    file.write(response.content)

data = []
with open(csv_file, "r") as file:
    lines = file.readlines()[1:]
    for line in lines:
        data.append(line.strip().split(','))

data_sorted = sorted(data, key=lambda x: x[0])
total_records = len(data_sorted)

boroughs = []
for row in data_sorted:
    borough = row[1]
    if borough not in boroughs:
        boroughs.append(borough)

brooklyn_count = 0
for row in data_sorted:
    if row[1] == '"Brooklyn"':
        brooklyn_count += 1

output = f"""
Total Records (sorted ascending): {total_records}
Unique Boroughs: {', '.join(boroughs)}
Number of records for Brooklyn: {brooklyn_count}
"""

with open("/root/taxi_zone_output.txt", "w") as output_file:
    output_file.write(output)

print("Output saved to /root/taxi_zone_output.txt")
