from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'mysql_password', 
    'database': 'campus_connect'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    
    event_name = request.form.get('event_name')
    full_name = request.form.get('full_name')
    degree = request.form.get('degree')
    branch = request.form.get('branch')
    email = request.form.get('email')
    phone = request.form.get('phone')

    try:
       
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
       
        query = """INSERT INTO registrations (full_name, degree, branch, email, phone, event_name) 
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        values = (full_name, degree, branch, email, phone, event_name)
        
        cursor.execute(query, values)
        conn.commit()
        
        cursor.close()
        conn.close()
        
        print(f"Success: Registered {full_name} for {event_name}")
        return jsonify({"status": "success"})

    except Exception as e:
        print(f"Database Error: {e}")
        
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)