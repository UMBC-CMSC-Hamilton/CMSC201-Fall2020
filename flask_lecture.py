from flask import Flask, render_template, send_file, request

app = Flask(__name__)


@app.route('/')
def main_page():
    print('hello there')
    return render_template('index.html')
    # return '<html><title>This is the title.</title><body>This is the body</body></html>'


@app.route('/images')
def load_image_site():
    return render_template('pic_select.html')


@app.route('/imagechoices')
def image_choice_page():
    return render_template('imagechoices.html')


@app.route('/<image_name>.jpg')
def get_image(image_name):
    print('the image pid is', image_name)
    return send_file('static/' + image_name + '.jpg', mimetype='image/gif')


@app.route('/united_states')
def united_states_page():
    states = []
    with open('united_states.txt') as f:
        states = [x.strip() for x in f.readlines()]
    return render_template('for_page.html', states=states)


@app.route('/create_example')
def create_page():
    return render_template('create_element_example.html')


answers = []


@app.route('/form_example', methods=['GET', 'POST'])
def form_example_page():
    if request.method == 'POST':
        the_name = request.form.get('name')
        the_quest = request.form.get('quest')
        the_color = request.form.get('color')
        answers.append([the_name, the_quest, the_color])
        print(answers[-1])
    return render_template('form_example.html', answers=answers)


if __name__ == '__main__':
    app.run(port=81)
