import requests
url = "https://www.morningstar.com/"
header = {
    "From": "Justine Lim <wenjeix@gmail.com>"
}
response = requests.get(url, headers=header)
if response.status_code != 200:
    print("Failed to get HTML:",
            response.status_code, response.reason)
    exit()

html = response.text
print(html)
