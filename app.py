

from flask import Flask, render_template, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'




class MyForm(Form):
    num = IntegerField('Insert an Number')



@app.route("/", methods=['GET', 'POST'])
def index():
    context = {
        'title': "Мама",
    }
    print(request.method)
    form = MyForm()
    if request.method == 'POST':  # Now this will work correctly
        form = MyForm(request.form)
        if form.validate():
            num = form.num.data
            context["num"] = num
        else:
            print("error")

    context ["form"] = form

    print(context)
    return render_template('index.html', **context)