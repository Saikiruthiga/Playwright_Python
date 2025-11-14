import json

def generate_report():
    dt = {
        "name" : "Peter",
        "Age" : 25,
    }

    with open("report.json", "w") as file:
        json.dump(dt,file) # takes the dt data and write/dump as json in a file
        print("File generated")

generate_report()
