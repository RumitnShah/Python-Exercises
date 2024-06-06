import json

sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

with open("sampleJson.json" , "w") as write_file:
    json.dump(sampleJson, write_file, indent=2, sort_keys=True)

print("Writing JSON data into a file")
