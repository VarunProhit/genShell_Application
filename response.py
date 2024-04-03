from dotenv import dotenv_values
import requests
class Command:
    
    def request_command(self, prompt: str):
        env_vars = dotenv_values(".env")
        Backend_URL = env_vars.get("BACKEND_URL")
        # print("bac",Backend_URL)
        url = Backend_URL+"/generate"
        payload = {"input": prompt}
        headers = {"Content-Type": "application/json"}

        response = requests.post(url, json=payload, headers=headers)
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            result = response.json()
            print(f"Result from FastAPI: {result}")
            print("res", result["data"])
            return result["data"]
        except Exception as e:
            print (e)
            raise e
        # if response.status_code == 200:
        #     result = response.json()
        #     # print(f"Result from FastAPI: {result}")
        #     return result
        # else:
        #     print(f"Error: {response.status_code} - {response.text}")
        # return response