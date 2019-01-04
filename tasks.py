from flask_rq import job
from models import CountRequest
from database import db_session
import requests

@job
def count_words_at_url(url):
    resp = requests.get(url)
    count =  len(resp.text.split())
    return count