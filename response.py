from dotenv import dotenv_values
import requests
class Command:
    
    def request_command(self, prompt: str):
        env_vars = dotenv_values(".env")
        Backend_URL = env_vars.get("BACKEND_URL")
        print(Backend_URL)
        url = Backend_URL+"/generate"
        payload = {"input": prompt}
        headers = {"Content-Type": "application/json"}

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            result = response.json()
            print(f"Result from FastAPI: {result}")
            return result
        else:
            print(f"Error: {response.status_code} - {response.text}")
        return response