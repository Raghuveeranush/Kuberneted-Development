import requests
proxies = {
    "http": "http://10.24.19.82:8080",
    "https": "http://10.24.19.82:8080"
}

url = f'https://api.github.com/repos/kubernetes/kubernetes/pulls'

response = requests.get(url, proxies=proxies)

if response.status_code == 200:
    complete_details = (response.json())

    #print(len(complete_details))
    pr_req = {}
    for data in (complete_details):
        user = data["login"]
        #user_id = data["user"]["id"]
        #print(f"{user}:{user_id}")
        if user in pr_req:
            pr_req[user] =+1
        else:
            pr_req[user] = 1
    
    print(pr_req)

else:
    print("Authentication error")
