

from app import app


@app.route('/')
@app.route('/index')
def serve():
    return 'Hello from backend'



from app.wiki.controller import *