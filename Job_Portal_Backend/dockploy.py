# ...existing code...
# pip install requests 

import requests

API_URL = "http://51.20.183.232:3000//api/project.all"
api_key = "ygpQYncqgPbSnoOlGmUcEMDMReokjgEymaOtpaXuSsLbNXqTjgbxoaaDGkJNwMhX"
app_name = "jobportal-backend-9pgu1a"

def get_application_id():
    """Fetch Application ID"""
    headers = {
        "accept": "application/json",
        "x-api-key": api_key,
    }
    try:
        req = requests.get(API_URL, headers=headers, timeout=30)
        req.raise_for_status()
        data = req.json()
    except requests.RequestException as e:
        print("Request failed:", e)
        return None

    # Safely iterate and find the requested application by name
    for project in data or []:
        environments = project.get("environments", [])
        for env in environments:
            applications = env.get("applications", [])
            for app in applications:
                if app.get("appName") == app_name:
                    app_id = app.get("applicationId")
                    print("Found application id:", app_id)
                    return app_id

    print("Application not found")
    return None

if __name__ == "__main__":
    get_application_id()
# ...existing code...