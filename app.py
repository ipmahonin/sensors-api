from flask import Flask
from repository.sensor_repository import init_db
from routes import sensors, system
import logging
import gunicorn


logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logger = logging.getLogger(__name__)

app=Flask(__name__)
app.register_blueprint(sensors.sensor_bp)
app.register_blueprint(system.system_bp)

@app.errorhandler(500)
def hanle_500(error):
    logger.error("app error 500")
    return{
        'status': 'error',
        "message": "internal server error"
    },500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# конец файла app.py

#docker build -t sensors-api .
#docker run -p 5000:5000 sensors-api
#docker-compose up --build

#docker exec -it sensors-db bash
#psql -U user -d sensors -f /migrations/001_create_sensors.sql
#psql -U user -d sensors