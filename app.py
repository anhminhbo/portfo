import csv
from flask import Flask, render_template, request, redirect # render_template will send the html file
app = Flask(__name__) # create an instance of class Flask with name app
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>') # This is a shortcut to access all the html file instead of create one by one
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database: #a mean append to the file
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},({subject}),\'{message}\'')

def write_to_csv(data):
    with open('database.csv',mewline = '',mode='a') as database2: #a mean append to the file
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimeter= ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET']) # Get means the browser want us to send info, Post mean the browser want us to save the info
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict() # grab the datas and get everything as a dict
        write_to_file(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong. Try again!'

