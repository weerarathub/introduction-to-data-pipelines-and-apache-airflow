import json

from airflow import DAG
from airflow.utils import timezone
from airflow.operators.python import PythonOperator

import requests


def _get_dog_images():
    # Get data from Dog API
    # โค้ดส่วนนี้จะเป็นการเชื่อมต่อกับ Dog API โดยเราจะใส่ URL Endpoint
    url = "https://dog.ceo/api/breeds/image/random"
    # เสร็จแล้วจะยิง Request ไปดึงข้อมูลมาเก็บใส่ Response
    response = requests.get(url)
    data = response.json()
    print(data)

    # Write data to file
    with open("dogs.json", "w") as f:
        json.dump(data, f)

    # โค้ดส่วนนี้จะเป็นการเตรียมเรื่อง Credentials และ Configuration ต่าง ๆ เพื่อใช้ในการเชื่อมต่อกับ Dog API
    api_url = "https://api.jsonbin.io/v3/b"
    headers = {
        "Content-Type": "application/json",
        "X-Master-Key": "$2a$10$uPYcGTovrmZ3/84/Q6g8SuABaVLHU0lcG7nuqJHlniDFrEJB5hX8K",
        "X-Collection-Id": "65ab44791f5677401f218262",
    }

    # Read data from file
    with open("dogs.json", "r") as f:
        data = json.load(f)

    # โค้ดส่วนนี้จะเป็นการยิง Request ไปเพื่ออัพโหลดข้อมูลไปยังเซิฟเวอร์ของ JSONBin
    response = requests.post(api_url, json=data, headers=headers)
    print(response.json())


with DAG(
    "dog_api_pipeline",
    start_date=timezone.datetime(2024, 1, 15),
    schedule=None,
):

    get_dog_images = PythonOperator(
        task_id="get_dog_images",
        python_callable=_get_dog_images,
    )