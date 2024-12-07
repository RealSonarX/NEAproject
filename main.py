from flask import *
from pymongo import *


# from random import *
# from datetime import *


def get_database():
    key1 = f"mongodb+srv://p10090:P4THF1ND3R@cluster0.kvmfm3w.mongodb.net/?appName=Cluster0"
    client2 = MongoClient(key1)
    return client2['Test']


def roll_attack():
    pass


def update_score():
    pass


def challenge():
    pass


class Player:
    pass


key = f"mongodb+srv://p10090:P4THF1ND3R@cluster0.kvmfm3w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient()
dbname = client['Test']
print(dbname.list_collection_names())
for i in dbname.list_collection_names():
    if i != "user_data":
        dbname.drop_collection(str(i))
app = Flask(__name__)

print(dbname.list_collection_names())
# print(dbname.list_collection_names())
user_data_mongo = dbname["user_data"]
print(user_data_mongo.find_one('user_data'))
# print(collection_name)
cursor = user_data_mongo.find({})
admindata = {"username": "Admin", "password": "P4TH4DM1N", "path": "Blaze"}
adminPresent = False
for document in cursor:
    print(document)
    if document['username'] == "Admin":
        adminPresent = True

if not adminPresent:
    user_data_mongo.insert_one(admindata)
for document in cursor:
    print(f"Username : {document['username']}")


@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)

    if request.method == 'POST':
        if request.form.get('Login') == 'Login':
            print("Pressed")
            return redirect("/login")
        else:
            return render_template("login.html")
    return render_template("intro.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    global logged_in_user
    if request.method == 'POST':
        if request.form.get('Login') == 'Login':
            username = request.form.get("username")
            password = request.form.get("password")
            print(username)
            print("Pressed")

            # valid = False
            for documentee in user_data_mongo.find({}):
                print(documentee['username'], username)
                if documentee['username'] == username:
                    if documentee['password'] == password:
                        print('Valid')
                        # valid = True

                        logged_in_user = username
                        return redirect('/game')
                    else:
                        return redirect('/login')

        # else:
        #    return render_template("game.html")
    return render_template("login.html")


@app.route('/register', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        if request.form.get('Register') == 'Register':
            password = request.form.get("pass")
            username = request.form.get('user')
            path = request.form.get('path')
            print(username)
            print(path)
            print(password)
            userdata = {"username": username, "password": password, "path": path, "lives" : 3, "Rank" : 0}
            print(userdata)
            # valid = True
            for documente in user_data_mongo.find({}):
                print(documente['username'], username)
                if documente['username'] == username:
                    print(documente['username'], 'a')
                    print('username taken')
                    return redirect("/register")
                else:
                    user_data_mongo.insert_one(userdata)
                    print('registered')
                    return redirect('/login')
    # else:
    #    return render_template("game.html")
    return render_template("register.html")


# @app.route('/character_creation', methods=['GET', 'POST'])
# def create():
#    return render_template("game.html")
#

# username = 'Jerry'
@app.route('/game')
def game():
    # dbname = get_database()
    for documents in user_data_mongo.find({}):
        if documents['username'] == logged_in_user:
            print(documents)
    return render_template("game.html", user=logged_in_user, path='Blaze')


if __name__ == '__main__':
    # print(get_database())
    app.run(host='0.0.0.0', port=5000, debug=True)
