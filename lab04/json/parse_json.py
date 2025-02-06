import json

with open('sample-data.json', 'r') as file:
    json_data = json.load(file)
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<6} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for item in json_data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    print("{:<50} {:<20} {:<6} {:<6}".format(
        attributes["dn"],
        attributes["fecMode"],
        attributes["speed"],
        attributes["mtu"]
    ))
