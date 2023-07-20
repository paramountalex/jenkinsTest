import requests

print("This means I can use docker and jenkins!")

req = requests.get('https://www.google.com')

if req.status_code == 200:
    print("and my image can access google!")
else:
    print("but my image can't access google):")
