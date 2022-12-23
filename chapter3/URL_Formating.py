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


for web in websites:
    if not web.startswith("https://"):
        # print("Have to go")
        web = f"https://{web}"
        print("Fixed now" + web)
    print(web)

