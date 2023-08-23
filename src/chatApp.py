from flask import Flask, redirect, url_for, request, render_template
import csv
server = Flask(__name__ , template_folder="templates")

@server.route("/", methods=['GET', 'POST'])
def toHomePage():
    return redirect("/register")
@server.route("/register", methods=['GET', 'POST'])
def homePage():
    if request.method == 'POST':
        name = request.form["username"]
        password = request.form["password"]
        exist = saveInCsv(name, password)
        return redirect('/login')
    return render_template('register.html')


@server.route("/login", methods=['GET', 'POST'])
@server.route("/logout", methods=['GET', 'POST'])
def loginPage():
    if request.method == 'POST':
        name = request.form["username"]
        password = request.form["password"]
        exist = checkIfExist(name, password)
        if exist:
            return redirect('/lobby')
    return render_template('login.html')
    
@server.route("/chat", methods=['GET', 'POST'])
def chatPage():
    return render_template('chat.html')

@server.route("/lobby", methods=['GET', 'POST'])
def lobbyPage():
    return render_template('lobby.html')


def saveInCsv(name, password):
    with open('users.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=',') 
        for row in reader:
            if name == row[0]:
                f.close()
                return True
    with open('users.csv', 'a') as f:
        writer = csv.writer(f)
        encPassword = password.encode()
        writer.writerow([name,encPassword])
        f.close()
        return False

def checkIfExist(name, password):
    with open('users.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=',') 
        for row in reader:
            if name == row[0]:
                if password.encode() == row[1]:
                    f.close()
                    return True
        return False


if __name__ == "__main__":
    server.run(host='0.0.0.0')