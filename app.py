from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'


@app.route('/')
def show_form():
    ''' Show for to ask for words '''
    prompts = story.prompts

    return render_template('form.html', prompts=prompts)

@app.route('/story')
def show_story():
    ''' Generate story '''
    text = story.generate(request.args)

    return render_template('story.html', text=text)