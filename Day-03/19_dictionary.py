# Dictionary A dictionary stores data as key-value pairs.

server = {
    "name": "web-01",
    "ip": "192.168.1.10",
    "port": 8080
}

print(server)
print(server["ip"])
print(server["port"])


for k in server:
    print(k, server[k])