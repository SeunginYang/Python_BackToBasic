from requests import get

websites = [
    "naver.com",
    "google.com",
    "https://yahoo.com",
    "tving.com",
    "https://airbnb.com"
]

# for web in websites:
#     if web.startswith("https://"):
#         print("Good to go")
#     else:
#         print("Need to fix it")


results = {}


for web in websites:
    if not web.startswith("https://"):
        # print("Have to go")
        web = f"https://{web}"        
    response = get(web)
    # print(response.status_code)
    if response.status_code == 200:
        # print(f"{web} is OK")
        results[web] = "OK"
    else:
        # print(f"{web} is not OK")
        results[web] = "FAILED"

print(results)