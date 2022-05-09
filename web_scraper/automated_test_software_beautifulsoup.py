"""
Method 2: Parsing with BeautifulSoup
"""

# **************requests module************************** 

# import requests
# import os
# from dotenv import load_dotenv

# load_dotenv()
# URL = os.environ.get("URL")
# URL_HTML_TEST_FILE = r"/Users/justinelim/financials.morningstar.com/ratios/r.html?t=fb.html"
HEADER = {
        "From": "Justine Lim <wenjeix@gmail.com>"
    }

# with open(URL_HTML_TEST_FILE, encoding="utf-8") as f:
#         html = f.read()

# response = requests.get(url_input, headers=HEADER)
# if response.status_code != 200:
#     print("Failed to get HTML:",
#             response.status_code, response.reason)
#     exit()

# html = response.text
# print(html)

# **************urllib module************************** 

import urllib.request
import os
from dotenv import load_dotenv

load_dotenv()
URL = os.environ.get("URL")

request = urllib.request.Request(URL)
response = urllib.request.urlopen(request)
html = response.read()
print(html)