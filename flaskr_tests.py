import os
import hello
import unittest
import tempfile
import random
from tasks import count_words_at_url
from bs4 import BeautifulSoup
from flask_testing import LiveServerTestCase

class HelloTestCase(LiveServerTestCase):

    # def setUp(self):
    #     self.db_fd, hello.app.config['DATABASE'] = tempfile.mkstemp()
    #     hello.app.testing = True
    #     self.app = hello.app.test_client()
    #     with hello.app.app_context():
    #         hello.init_db()

    # def tearDown(self):
    #     os.close(self.db_fd)
    #     os.unlink(hello.app.config['DATABASE'])
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"
    TESTING = True

    def create_app(self):
        return hello.app

    def 

    def checkWordCount(self):
        #creating random string of random number of words
        result =  count_words_at_url("http://localhost:5000")
        assert result == 1234
    
    def test_product(self):
        #this for check if POST method is working
        url = "https://youtube.com"
        rv = self.app.post("/", data = {"url":url})
        flag = False
        soup = BeautifulSoup(rv.data)
        table = soup.find("table")
        print(table)
        for row in table.findAll("tr"):
            cols = row.findAll("td")
            if url in [col.text for col in cols]:
                flag = True
        assert flag

    
        

if __name__ == '__main__':
    unittest.main()