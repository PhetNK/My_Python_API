import requests
import sys

api_url = "https://jsonplaceholder.typicode.com/todos/1"


print (f"[*] Querying API: {api_url}\n")

try:

    response = requests.get(api_url, timeout=5)
    st_code = response.raise_for_status()
    print(f"{st_code}\n")
    data = response.json()
    #print(data)
    print(f"[+] Request successful !")
    print("------------------------")
    print(f"User ID: {data['userId']}")
    print(f"Title: {data['title']}")
    print(f"Completed: {data['completed']}")
    print("------------------------\n")

except requests.exceptions.RequestException as e:
    print(f"\n[ERROR] couuld not connect to The API {e}")
    sys.exit(1)

