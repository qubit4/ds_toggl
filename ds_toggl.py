import requests
from requests.auth import HTTPBasicAuth
  
token = "cd4c01ad6ede5b9926c2631241a98396"
workspace_id = "5373442"
start_date = "2021-01-01"
end_date = "2022-01-01"
user_agent = "f22@gmx.us"
url = f"https://api.track.toggl.com/reports/api/v2/summary?workspace_id={workspace_id}&since={start_date}&until={end_date}&user_agent={user_agent}"

response = requests.get(url, auth = HTTPBasicAuth(token, "api_token"))

if response.status_code == 200:

    data = response.json()

    total_time = data["total_grand"] / 1000
    print(f"Total time of all projects (in seconds): {total_time} \n")
   
    for i in range(len(data["data"])):

        project = data["data"][i]
        project_title = project["title"]["project"]
        project_time = project["time"] / 1000

        print(f"Time of {project_title} (in seconds): {project_time} \n")
        print(f"Tasks in {project_title}: \n")

        for j in range(len(project["items"])):

            task_title = project["items"][j]["title"]["time_entry"]
            task_time = project["items"][j]["time"] / 1000
            percents_allprojects = round(((task_time / total_time) * 100), 2)
            percents_project = round(((task_time / project_time) * 100), 2)

            print(f"Title: {task_title}")
            print(f"Time (in seconds): {task_time}")
            print(f"Time of {task_title} makes {percents_allprojects}% of total time and {percents_project}% of project time. \n")
           

else:
    print(f"Failed to read data. Status code is: {response.status_code}")

