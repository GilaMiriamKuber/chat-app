from flask import Flask, redirect, request, render_template, session
import csv
import os
# from dotenv import load_dotenv
# load_dotenv()
app = Flask(__name__)
app.secret_key = "tamar_gilamiriam_!_@_?_chat_app"
app.config["SECRET_KEY"]="tamar_gilamiriam_!_@_?_chat_app"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


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
def loginPage():
    if request.method == 'POST':
        name = request.form["username"]
        password = request.form["password"]
        exist = checkIfExist(name, password)
        if exist:
            session['username'] = name
            return redirect('/lobby')
    return render_template('login.html')


@server.route("/logout", methods=['GET', 'POST'])
def logOut():
    session.pop('username', None)
    return redirect("/login")
    
@server.route("/chat", methods=['GET', 'POST'])
def chatPage():
    return render_template('chat.html')

@server.route("/lobby", methods=['GET', 'POST'])
def lobby():
    if session.get('usernme') == True:
            if request.method == 'POST':
                new_room = request.form['new_room']
                # path = os.getenv('ROOMS_PATH') + new_room + ".txt"
                path = './src/rooms' + new_room + ".txt"
                open(path , 'w')
                rooms=  os.listdir('./src/rooms')
                new_rooms = [x[:-4] for x in rooms]
                return render_template('lobby.html',room_names=new_rooms)
    else:
        return render_template('login.html') 


@server.route("/chat/<int:room> ", methods=['GET', 'POST'])
def chatRoom():
    return render_template('chat.html')

def saveInCsv(name, password):
    with open('users.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=',') 
        for row in reader:
            if name == row[0]:
                f.close()
                return True
    with open('users.csv', 'a') as f:
        writer = csv.writer(f)
        #encPassword = password.encode()
        writer.writerow([name,password])
        f.close()
        return False

def checkIfExist(name, password):
    with open('users.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=',') 
        for row in reader:
            if name == row[0]:
                if password == row[1]:
                    f.close()
                    return True
        return False


if __name__ == "__main__":
    server.run(host='0.0.0.0')
