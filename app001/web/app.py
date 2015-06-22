from flask import Flask
from app001.web.views.business import businessbp
from app001.utils.settings import DEBUG, USE_RELOADER
import os


app = Flask(__name__)
app.register_blueprint(businessbp)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=DEBUG, use_reloader=USE_RELOADER)
