import requests

def main_fun():    
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    if response.status_code == 200:
        print("Response JSON:", response.json())
    else:
        print("Failed to fetch data. Status Code:", response.status_code)
