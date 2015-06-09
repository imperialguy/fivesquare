from flask import Flask
from app001.web.views.business import businessbp
from app001.utils.settings import DEBUG, USE_RELOADER


app = Flask(__name__)
app.register_blueprint(businessbp)

if __name__ == '__main__':
    app.run(debug=DEBUG, use_reloader=USE_RELOADER)
