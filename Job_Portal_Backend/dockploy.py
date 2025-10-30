# pip install requests 
 
import requests 
 
API_URL = "http://http://13.60.29.125:3000//api/project.all" 
api_key = "ygpQYncqgPbSnoOlGmUcEMDMReokjgEymaOtpaXuSsLbNXqTjgbxoaaDGkJNwMhX" 
app_name = "jobportal-backend-9pgu1a" 
 
def get_application_id(): 
   """Fetch Application ID""" 
   headers = { 
       "accept": "application/json", 
       "x-api-key": api_key, 
   } 
   req = requests.get(API_URL, headers=headers, timeout=30) 
   req.raise_for_status() 
   data = req.json() 
   # Safely iterate and find the requested application by name 
   for project in data or []: 
       environments = project.get("environments", []) 
       for env in environments: 
           applications = env.get("applications", []) 
           for app in applications: 
               if app.get("appName") == app_name: 
                   print(app.get("applicationId")) 
   return req.content 
 
get_application_id()