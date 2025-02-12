### **Flask Web Development - Quick Guide**  

#### **What is Flask?**  
Flask is a lightweight **web framework** for Python, providing essential tools like routing, templates, and database integration for web development.  

---

## **Getting Started**  

### **Install Flask**  
```sh
pip install flask
```

### **Create a Basic Flask App**  
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

---

## **Routing in Flask**  
### **What is a Route?**  
A **route** defines a URL path that maps to a function.  

```python
@app.route('/about')
def about():
    return "About Page"
```

### **Handling Variables in Routes**  
```python
@app.route('/user/<name>')
def greet_user(name):
    return f"Hello, {name}!"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Post ID: {post_id}"
```

---

## **Templates with Jinja2**  
Templates use **Jinja2** to render dynamic content in HTML.

### **Create a Template (`templates/index.html`)**  
```html
<!DOCTYPE html>
<html>
<head><title>Flask App</title></head>
<body>
    <h1>Welcome, {{ name }}!</h1>
</body>
</html>
```

### **Render the Template in Flask**  
```python
from flask import render_template

@app.route('/hello/<name>')
def hello(name):
    return render_template('index.html', name=name)
```

---

## **Dynamic Templates (Loops & Conditions)**  
### **Loop Example**  
```html
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>
```

### **Condition Example**  
```html
{% if user.is_admin %}
    <p>Welcome, Admin!</p>
{% else %}
    <p>Welcome, User!</p>
{% endif %}
```

---

## **Displaying MySQL Data in HTML**  
### **Install MySQL Connector**  
```sh
pip install flask-mysql-connector
```

### **Connect Flask to MySQL**  
```python
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="mydatabase"
)

@app.route('/users')
def users():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template('users.html', users=users)
```

### **Display Data in HTML (`templates/users.html`)**  
```html
<ul>
{% for user in users %}
    <li>{{ user.name }} - {{ user.email }}</li>
{% endfor %}
</ul>
```

---

## **Next Steps**  
- Add **Flask-WTF** for forms  
- Use **Flask-Login** for authentication  
- Integrate **SQLAlchemy** for ORM  
- Deploy using **Gunicorn & Nginx**  
