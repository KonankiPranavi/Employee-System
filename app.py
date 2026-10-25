from flask import Flask, request, render_template_string

app = Flask(__name__)

# In-memory database to store employee records
employees = []

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Employee System - v1</title>
</head>
<body>
    <h2>Employee System (Version 1 - Add Employee)</h2>
    <form action="/add" method="POST">
        <label>Employee ID:</label><br>
        <input type="text" name="id" required><br><br>
        <label>Employee Name:</label><br>
        <input type="text" name="name" required><br><br>
        <label>Designation:</label><br>
        <input type="text" name="designation" required><br><br>
        <button type="submit">Add Employee</button>
    </form>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/add', methods=['POST'])
def add_employee():
    emp_id = request.form.get('id')
    name = request.form.get('name')
    designation = request.form.get('designation')
    
    new_employee = {"id": emp_id, "name": name, "designation": designation}
    employees.append(new_employee)
    
    return f"<h3>Employee {name} added successfully!</h3> <a href='/'>Go Back</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
