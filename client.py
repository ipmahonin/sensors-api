import requests

sensor = {
    "name": "Temp1",
    "value": 60
}

def command_post():
    data = requests.post(
        "http://127.0.0.1:5000/sensors/",
        json=sensor
        
    ) 
    print(data.status_code)
    print(data.json())

def command_get_all():
    data = requests.get(
        "http://127.0.0.1:5000/sensors/"  
    )
    print(data.status_code)
    print(data.json())
    
def command_get_alarm():
    data= requests.get(
       "http://127.0.0.1:5000/sensors/alarm"  
    )
    print(data.status_code)
    print(data.json())

def delete_sensor():
    data=requests.delete(
        "http://127.0.0.1:5000/sensors/Temp2",
    )
    print(data.status_code)
    print(data.json())

def status():
    data=requests.get(
        "http://127.0.0.1:5000/system/stats",
    )
    print(data.status_code)
    print(data.json())   

def health():
    data=requests.get(
        "http://127.0.0.1:5000/system/health",
    )
    print(data.status_code)
    print(data.json())

command='2'

if command == '1':
    command_post()
elif command == '2':
    command_get_all()
elif command == '3':
    command_get_alarm()
elif command == '4':
    delete_sensor()
elif command == '5':
    status() 
elif command == '6':
    health()   

# конец файла client.py он нужен для проверки
