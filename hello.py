from flask import Flask, render_template, redirect, url_for, request
from flask_rq import RQ, get_worker
from database import db_session, init_db
from tasks import count_words_at_url
from models import CountRequest
import time

app = Flask(__name__)
rq = RQ(app)

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        instance = CountRequest(url = url)
        task = count_words_at_url.delay(url)
        while task.status != 'finished' and task.status != 'failed':
            time.sleep(1)
        
        if task.status == 'failed':
            return "Failed to get the word count"
        instance.count = task.result
        db_session.add(instance)
        db_session.commit()

    entries = CountRequest.query.all()
    results = [(entry.url,entry.count) for entry in entries]
    return render_template("index.html", results = results)

@app.route("/test_url")
def test_url():
    num_words = 1234
    test_string = ''
    for _ in range(num_words):
        test_string += "aaaaa "
    return test_string

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

