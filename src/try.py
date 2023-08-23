import csv
from flask import Flask
server = Flask(__name__ , template_folder="templates")

@server.route("/", methods=['GET', 'POST'])
def hello():
    return csvcheck()

def csvcheck():
    username = "tamar"

    with open('users.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=',') 
        for row in reader:
            if username == row[0]:
                return row[1]




if __name__ == "__main__":
    server.run(host='0.0.0.0')