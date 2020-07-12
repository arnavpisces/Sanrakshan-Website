from flask import Flask, render_template, request, redirect

app=Flask(__name__)
@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/contact-us', methods=['GET','POST'])
def contactPage():
    return render_template('contact.html')

@app.route('/privacy')
def privacyPage():
    return render_template('privacy.html')

@app.route('/donate')
def donatePage():
    return render_template('donate.html')

@app.route('/send-message', methods=['GET','POST'])
def getMessage():
    name=request.form['name']
    email=request.form['email']
    message=request.form['message']
    if len(name) == 0 or len(email) == 0 or len(message) == 0:
        return redirect('contact-us')
    details=open('messages.txt','a')
    details.write("Name: "+name)
    details.write("\nEmail: "+email)
    details.write("\nMessage: "+message+"\n")
    details.close()
    return redirect('contact-us')

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)