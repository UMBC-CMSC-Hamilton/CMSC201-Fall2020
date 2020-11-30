"""
NONE OF THIS IS LEGAL IN 201

THIS IS FOR YOUR FUTURE LIFE
"""

from flask import Flask, render_template, send_file, request
# this isn't the default flask package.
from flask_login import FlaskLoginClient

app = Flask(__name__)


# decorators... we are not going to really talk about them at all...
@app.route('/')
def render_main_page():
    print('trying to create the main page')
    return render_template('real_fun.html')


@app.route('/<image_name>.jpg')
def get_image(image_name):
    print(image_name)
    return send_file('static/' + image_name + '.jpg', mimetype='image/gif')


# what is GET == HTML request for the website
# what is POST == HTML request FROM THE WEBSITE with the data
answers = []
@app.route('/quest', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        the_name = request.form.get('name')
        the_quest = request.form.get('quest')
        the_color = request.form.get('color')

        answers.append([the_name, the_quest, the_color])
    return render_template('form_example.html', answers=answers)


@app.route('/list_states.html')
def render_states_page():
    the_states = []
    with open('united_states.txt') as the_states_file:
        for line in the_states_file:
            the_states.append(line.strip())
    print(the_states)
    # render_template changes this thing into a purely html file
    return render_template('list_states.html', states=the_states)


if __name__ == '__main__':
    app.run(port=1729)
