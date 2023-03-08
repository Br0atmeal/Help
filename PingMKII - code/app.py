from flask import Flask, render_template, url_for, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/addrec', methods = ['POST', 'GET'])
def addrec():
    if request.method == 'GET': 
        return render_template('add.html')
    
    elif request.method == 'POST': 
        with sqlite3.connect('students.db') as con: 
            con.execute("INSERT INTO students (name, id, city) VALUES (?, ?, ?)", (request.form["s-name"], request.form["s-id"], request.form["s-city"]))
            con.commit
            msg = "Student record successfuly added"
            return render_template("add.html", msg = msg)
        
@app.route('/searchrec', methods = ['POST', 'GET'])
def searchrec():
    if request.method == 'GET': 
        return render_template('search.html')
    
    elif request.method == 'POST': 
        try: 
            name = request.form["s-name"]

            with sqlite3.connect('students.db') as con: 
                cur = con.cursor()
                found = cur.execute("SELECT * FROM students WHERE (name) LIKE (?)",(name) ).fetchall()
                print(found) 
        
        except Exception as e: 
            con.rollback()
            print(e)

        finally: 
            con.close()
            return render_template('found.html', found = found)
        


if '__main__' == __name__: 
    app.run(debug = True)