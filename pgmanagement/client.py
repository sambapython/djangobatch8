import requests
# resp = requests.post("http://127.0.0.1:8000/api/pgmanagers/",
# 	json={"name":"apima nager","cell":"9676622026",
# 	"email":"m4@gmail.com","gender":"M"})
# print resp.json()
# resp = requests.get("http://127.0.0.1:8000/api/pgmanagers/")
# print resp.json()
# resp = requests.post("http://127.0.0.1:8000/api/pgmanagers/")
# print resp.json()
# resp = requests.put("http://127.0.0.1:8000/api/pgmanagers/")
# print resp.json()
# resp = requests.delete("http://127.0.0.1:8000/api/pgmanagers/")
# print resp.json()
# resp = requests.put("http://127.0.0.1:8000/api/pgmanagers/3",
# 	json={"name":"apimanager_modify1","cell":"9676622028"})
# print resp.json()
# resp = requests.delete("http://127.0.0.1:8000/api/pgmanagers/6")
# print resp.json(), resp.status_code
# resp = requests.post("http://127.0.0.1:8000/api/pgmanagers/",
# 	json={"name":"pg4","cell":"9676622029","email":"pg4@gmail.com",
# 	"gender":"F"})
# print resp.json(), resp.status_code
# resp = requests.get("http://127.0.0.1:8000/api/pgmanagers/")
# print resp.json()

# resp = requests.post("http://127.0.0.1:8000/api/pgmanagers/",
# 	json={"name":"pg6","cell":"9676622021","email":"pg6@gmail.com",
# 	"gender":"F"})
# print resp.json(), resp.status_code
# resp = requests.put("http://127.0.0.1:8000/api/pgmanagers/1",
# 	json={"name":"pg62",},auth=("user1","samba1234"))
# print resp.json(), resp.status_code
# resp = requests.get("http://127.0.0.1:8000/api/pgmanagers/",auth=("user1","samba1234"))
# print resp.json(), resp.status_code
# resp = requests.get("http://127.0.0.1:8000/api/pgmanagers/",)
# print resp.json(), resp.status_code
resp = requests.post("http://127.0.0.1:8000/api/pgmanagers/",
	json={"name":"pg9","cell":"9676622024","email":"pg9@gmail.com",
	"gender":"F"})
print resp.json(), resp.status_code