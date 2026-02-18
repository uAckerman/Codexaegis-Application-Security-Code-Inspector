import requests
from base_check import BaseCheck

class SQLInjectionCheck(BaseCheck):
    name = "Checking SQL Injection"

    def run(self, base_url):
        payload = {
            "username": "' OR '1'='1",  # one of the SQL Injection query
            "password": "' OR '1'='1"
        }

        try:
            response = requests.post(f"{base_url}/login", data=payload)

            if "Login Successful" in response.text:
                return {
                    "check": self.name,
                    "status": "VULNERABLE"
                }
            else:
                return {
                    "check": self.name,
                    "status": "SAFE"
                }

        except Exception as e:
            return {
                "check": self.name,
                "status": "ERROR",
                "detail": str(e)
            }


