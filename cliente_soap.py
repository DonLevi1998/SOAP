from zeep import Client

client = Client('http://127.0.0.1:8000/?wsdl')
result = client.service.say_hello("Hello World!")
print(result)