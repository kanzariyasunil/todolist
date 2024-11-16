from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Initialize an empty to-do list
todo_list = []

# Function to fetch all to-do items
def get_todo():
    return todo_list

# Function to add a new item to the to-do list
def add(value):
    todo_list.append(value)
    return todo_list

# Function to update a to-do item
def update(value, change_value):
    if value in todo_list:
        index = todo_list.index(value)
        todo_list[index] = change_value
    return todo_list

# Function to delete a to-do item
def delete(value):
    if value in todo_list:
        todo_list.remove(value)
    return todo_list

# Home route to display the to-do list
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        action = request.form.get('action')
        value = request.form.get('value')

        if action == "add":
            add(value)
        elif action == "update":
            change_value = request.form.get('change_value')
            update(value, change_value)
        elif action == "delete":
            delete(value)
    # Fetch the latest to-do list to pass to the template
    return render_template("index.html", todos=get_todo())

# API routes for AJAX requests
@app.route("/add", methods=["POST"])
def add_todo():
    value = request.json.get('value')
    add(value)
    return jsonify({"todos": get_todo()})

@app.route("/update", methods=["POST"])
def update_todo():
    value = request.json.get('value')
    change_value = request.json.get('change_value')
    update(value, change_value)
    return jsonify({"todos": get_todo()})

@app.route("/delete", methods=["POST"])
def delete_todo():
    value = request.json.get('value')
    delete(value)
    return jsonify({"todos": get_todo()})

if __name__ == "__main__":
    app.run(debug=True)
