from flask import Flask
from flask.sessions import SecureCookieSession as SCS

app = Flask(__name__)
session = SCS()

@app.route('/')
def index():
    session['joao'] = SCS()
    print(session)
    return str(session)

app.run(host='0.0.0.0', port=5500) if __name__=='__main__' else print()
