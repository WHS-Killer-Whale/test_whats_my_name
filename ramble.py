import requests
from bs4 import BeautifulSoup

user = "wahaha"

url = (
    "http://rambleeeqrhty6s5jgefdfdtc6tfgg4jj6svr4jpgk4wjtg3qshwbaad.onion/user/"
    + user
)
proxies = {
    "http": "socks5h://localhost:9050",
    "https": "socks5h://localhost:9050",
}


response = requests.get(url, proxies=proxies)
soup = BeautifulSoup(response.text, "html.parser")

print(response.status_code)

if response.status_code == 200:
	print(user," exists")
else :
	print(user," doesn't exist")


