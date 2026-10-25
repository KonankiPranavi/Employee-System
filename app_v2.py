from flask import Flask, request, redirect, url_for
from html import escape

app = Flask(__name__)

# Original employee records from V1
employees = [
    {
        "id": 101,
        "name": "Konanki Pranavi",
        "department": "IT"
    },
    {
        "id": 102,
        "name": "Ramya",
        "department": "CSE"
    },
    {
        "id": 103,
        "name": "Priya",
        "department": "AI"
    }
]


# Home page
@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Employee System V2</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f2f4f8;
                margin: 40px;
            }

            .container {
                background: white;
                padding: 25px;
                border-radius: 10px;
                max-width: 800px;
                margin: auto;
            }

            input, button {
                padding: 10px;
                margin: 5px;
            }

            button {
                cursor: pointer;
            }

            a {
                text-decoration: none;
            }
        </style>
    </head>

    <body>
        <div class="container">

            <h1>Employee Management System</h1>
            <h2>Version 2</h2>

            <h3>Add Employee</h3>

            <form action="/add" method="post">

                <input type="number"
                       name="id"
                       placeholder="Employee ID"
                       required>

                <input type="text"
                       name="name"
                       placeholder="Employee Name"
                       required>

                <input type="text"
                       name="department"
                       placeholder="Department"
                       required>

                <button type="submit">
                    Add Employee
                </button>

            </form>

            <hr>

            <h3>View Employees</h3>

            <p>
                Click the button below to display all employees.
            </p>

            <a href="/employees">
                <button type="button">
                    View Employees
                </button>
            </a>

        </div>
    </body>
    </html>
    """


# V1 feature: Add employee
@app.route("/add", methods=["POST"])
def add_employee():

    employee_id = request.form.get("id", type=int)

    name = request.form.get("name", "").strip()

    department = request.form.get(
        "department", ""
    ).strip()

    if employee_id is None or not name or not department:
        return "Please enter valid employee details.", 400

    # Prevent duplicate employee IDs
    for employee in employees:
        if employee["id"] == employee_id:
            return "Employee ID already exists.", 400

    employees.append({
        "id": employee_id,
        "name": name,
        "department": department
    })

    return redirect(url_for("view_employees"))


# V2 feature: View employees
@app.route("/employees")
def view_employees():

    rows = ""

    for employee in employees:

        rows += f"""
        <tr>
            <td>{employee['id']}</td>
            <td>{escape(employee['name'])}</td>
            <td>{escape(employee['department'])}</td>
        </tr>
        """

    return f"""
    <!DOCTYPE html>
    <html>

    <head>
        <title>Employee List - V2</title>

        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
                background: #f2f4f8;
            }}

            table {{
                border-collapse: collapse;
                width: 100%;
                background: white;
            }}

            th, td {{
                border: 1px solid #ccc;
                padding: 12px;
                text-align: left;
            }}

            th {{
                background: #dce6f1;
            }}

            a {{
                display: inline-block;
                margin-top: 20px;
            }}
        </style>
    </head>

    <body>

        <h1>Employee List - V2</h1>

        <table>

            <tr>
                <th>Employee ID</th>
                <th>Employee Name</th>
                <th>Department</th>
            </tr>

            {rows}

        </table>

        <h3>Total Employees: {len(employees)}</h3>

        <a href="/">Back to Home</a>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5002,
        debug=False
    )