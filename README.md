# iot_home

Sistema Smart Home IoT
======================

Questo progetto consente la gestione di sensori domestici tramite MQTT e database locale. Include moduli per sensori di gas e temperatura, un client MQTT e un database per la registrazione dei dati.

## Struttura del progetto

- `app.py`: Entry point dell'applicazione principale.
- `database.py`: Gestione del database locale per la memorizzazione dei dati dei sensori.
- `mqtt_client.py`: Client MQTT per la comunicazione con i sensori.
- `sensors.py/`: Moduli dei sensori.
  - `gaz_sensor.py`: Gestione sensore di gas.
  - `temp_sensor.py`: Gestione sensore di temperatura.

## Installazione

1. Clona il repository:
	```bash
	git clone https://github.com/Ednajm/iot_home.git
	cd iot_home
	```
2. Installa le dipendenze Python (se necessario):
	```bash
	pip install -r requirements.txt
	```

## Utilizzo

Avvia l'applicazione principale:
```bash
python app.py
```

## Requisiti

- Python 3.8+
- Broker MQTT (es. Mosquitto)

## Autore

Ednajm
