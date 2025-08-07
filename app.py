from dotenv import load_dotenv
from flask import Flask
from api.controllers.ngram_controller import ngram_blueprint
from waitress import serve

load_dotenv()

app = Flask(__name__)
app.register_blueprint(ngram_blueprint)

print("Starting NGram API Service")

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)    
    app.run(debug=True)
