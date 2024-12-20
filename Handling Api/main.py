import requests

def fetch_random_user():
    
    # Free api url
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    
    headers = {"accept": "application/json"}
    
    # Make a request to the API through its method
    response = requests.get(url, headers=headers)
    
    # Convert the response in json
    # Check "https://jsonformatter.org/" for tree object structure
    data_object = response.json()
    
    if data_object["success"] and data_object["data"]:
        user_data = data_object["data"]
        
        # data->login->username
        username = user_data["login"]["username"]
        
        # data-> location -> country
        country = user_data["location"]["country"]
        
        return username, country
    else:
        raise Exception("Failed to Fetch Data")
    
    

def fetch_random_quote():
    
    url= "https://api.freeapi.app/api/v1/public/quotes/quote/random"
    
    response = requests.get(url=url)
    
    data_obj=response.json()
    
    if data_obj["success"] and data_obj["data"]:
        user_data= data_obj["data"]
        
        author = user_data["author"]
        quote= user_data["content"]
        
        return author,quote
    else:
        raise Exception("Unable to Fetch")


def main():
    try:
        
        # username, country = fetch_random_user() #this functions returns 2 things
        # print(f"Username:{username}\n Country:{country}")
        
        author, quote = fetch_random_quote()
        print(f"Author:{author}\n Quote:{quote}")
        
        
    except Exception as e:
        print(str(e)) #exception may be anytype that will break the system thus convert it to string


if __name__ == "__main__":
    main()
        
    
    