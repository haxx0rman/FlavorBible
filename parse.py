import csv
import json
import unidecode

data = list(csv.reader(open("bible.csv")))
#print(data)
#print(json.dumps(data, sort_keys=True, indent=4))

def clean_main(initialString):
    #print("Fixing: " + str(initialString))
    parts = initialString.split(" (")
    final = str(parts[0])
    if "in general" in final:
        print(final)
        final = final.replace("in general", "")
        #print(final[:4])
        final = final[:len(final) - 3]
        print(final)

    if ", " in parts[0]:
        #print(final)
        stuff = final.split(", ")

        final = stuff [1] + " " + stuff[0]
        #print(final)
    return final

def clean_sub(initialString):
    print("Fixing: " + str(initialString))
    parts = initialString.split(" (")
    final = parts[0]
    if ", " in parts[0]:
        stuff = final.split(", ")

        final = stuff [1] + " " + stuff[0]

    return final

dick = {}
for thing in data:
    thing[0] = thing[0].lower()
    thing[1] = thing[1].lower()
    thing[0] = clean_main(thing[0])
    thing[0] = unidecode.unidecode(thing[0])
    thing[1] = unidecode.unidecode(thing[1])
    if thing[0] not in dick:
        dick[thing[0]] = [thing[1]]
        #print(thing)
    else:
        dick[thing[0]].append(thing[1])
        #print(str(thing) + " Is working")
#print(json.dumps(dick, sort_keys=True, indent=4))
with open('data.json', 'w') as outfile:
    json.dump(dick, outfile, indent=4, sort_keys=True)
