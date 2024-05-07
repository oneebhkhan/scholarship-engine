from src import app
from src.config.config import SERVICE_PORT

# from waitress import serve

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=SERVICE_PORT, debug=True)

# serve(app, host='0.0.0.0', port=SERVICE_PORT)