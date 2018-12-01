import requests
resp = requests.post("http://127.0.0.1:8000/api/pgmanagers/",
	json={"name":"apima nager","cell":"9676622026",
	"email":"m4@gmail.com","gender":"M"})
print resp.json()
resp = requests.get("http://127.0.0.1:8000/api/pgmanagers/")
print resp.json()
# resp = requests.post("http://127.0.0.1:8000/api/pgmanagers/")
# print resp.json()
# resp = requests.put("http://127.0.0.1:8000/api/pgmanagers/")
# print resp.json()
# resp = requests.delete("http://127.0.0.1:8000/api/pgmanagers/")
# print resp.json()