import requests
import os

print(os.getcwd())

# r = requests.get("https://xkcd.com/353/")

# images = requests.get("https://imgs.xkcd.com/comics/python.png")

# print(images.status_code)

# print(images.content)
# print(r.text)

# with open("comic.png", "wb") as f:
#     f.write(images.content)


# payload = {"username": "corey", "password": "testing"}
# r = requests.post("https://httpbin.org/post", data=payload)

# r_dict = r.json()

# print(r_dict["form"])

## adding auth with timeout
# r = requests.get(
#     "https://httpbin.org/basic-auth/corey/testing", auth=("corey", "testing"), timeout=3
# )

r = requests.get("https://httpbin.org/delay/6", timeout=3)

print(r)
