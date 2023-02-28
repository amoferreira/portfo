from flask import Flask, render_template, request, redirect 
import csv, os, smtplib


app = Flask(__name__)
if(__name__=="__main__"):
    app.run(debug=True)

@app.route("/")
def main():
    return render_template('index.html')


@app.route("/<string:page_name>")
def page_html(page_name):
    return render_template(page_name)
    
"""def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        name = data["name"]
        message = data["message"]
        file = database.write(f'\n{email},{name},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        name = data["name"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,name,message])

def sendemail(data):
    email = data["email"]
    name = data["name"]
    message = data["message"]
    answer = "Oki"
    server = smtplib.SMTP("smtp.office365.com", 587)
    server.starttls()
    server.login("", "")
    server.sendmail("", email, answer)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():

    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        sendemail(data)
        return 'ok'
"""      
    

