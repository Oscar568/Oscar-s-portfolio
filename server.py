#import os
#os.environ['Flask_APP'] = 'server.py' #not sure what this does


from flask import Flask, render_template, request, url_for, redirect
import csv
app = Flask(__name__)






@app.route('/')  # the code inside the parenthesis returns you when you click on the menu buttons instead of 404 error code
def home():
    return render_template('index.html')  #this whole code creates my own server

@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/works.html')
def works():
    return render_template('works.html')

@app.route('/about.html')
def about_me():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

# def write_to_file(data):
#     with open('C:/Users/oalex/Desktop/pythonFlaskProject/templates/database.txt',mode = 'a') as database:
#         email = data.get('email')
#         subject = data.get('subject')
#         message = data.get('message')
#         database.write(f'\n{email},{subject},{message}')


#the code below is to write information to a csv file
def write_to_csv(data):
    try:
        with open('database.csv',mode = 'a', newline = '') as database2:
            email = data.get('email')
            subject = data.get('subject')
            message = data.get('message')
            csv_writer = csv.writer(database2, delimiter= ',', quotechar= '"', quoting= csv.QUOTE_MINIMAL)
            csv_writer.writerow([email,subject,message])
    except Exception as e:
        print(f'An error occurred while writing to the file {e} ')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return render_template('thankyou.html')
    else:
        return 'Something went wrong. Try again!'



if __name__ == '__main__':
    app.run(debug=True)