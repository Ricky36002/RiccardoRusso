import json
import jsonschema
import sys

data = {}

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"},
        "scores": {
            "type": "array",
            "items": {"type": "number"},
        }
    },
    "required": ["name"],
    "additionalProperties": False
}

def  JsonSerialize(data, sfile):
    with open(sfile, "w") as write_file:
        json.dump(data, write_file)
def JsonDeserialize(sfile):
    with open(sfile, "r") as read_file:
        return json.load(read_file)
def print_directory(dData, sRoot):
    for key, value in dData.items():
        if sRoot != "":
            print("trovata chiave" + sRoot + "." + key)
        else:
            print("trovata chiave" + key)
        #print(value)
        #print(type(dData[key]))
        if type(dData[key]) is dict:
            if sRoot != "":
                print_directory(dData[key], sRoot + "." +  key)
            else:
                print_directory(dData[key], key)



MyFile = "./example_2.jsom"
data = JsonDeserialize(MyFile)
try:
    validate(instance, schema)
    print("L'istanza è coerente con lo schema")
except jsonschema.exceptions.ValidationError:
    print("L'istanza non è valida")

print_directory(data)
sys.exit()

print(type(data['quiz']))
if type(data('quiz')) is dict:
    print_directory(data['quiz'])


