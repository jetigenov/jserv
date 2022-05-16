from datetime import datetime

import requests
import json

from db_home.models import Question, db
from lib.keys import ID, ANSWER, QUESTION, DATE


def import_data(request):
    count = request['questions_num']
    url = f'https://jservice.io/api/random?count={count}'
    data = requests.get(url)
    response = json.loads(data.text)

    for r in response:
        question = db.session.query(Question).filter(Question.id == r[ID]).first()

        if not question:
            q = Question()
            q.id = r[ID]
            q.answer = r[ANSWER]
            q.question = r[QUESTION]
            q.date_create = r[DATE]
        else:
            import_data(request)

    return {'data': response}
