import asana

# credentials
API_KEY = 'YOUR_API_KEY HERE'
OLD_PROJECT_ID = 123
NEW_PROJECT_ID = 1234

# connecting to API
client = asana.Client.access_token(API_KEY)

# check if user is connected
me = client.users.me()
print("Hello " + me['name'])

# get new workspace id
new_workspace_id = client.projects.find_by_id(NEW_PROJECT_ID)['workspace']['id']

# get all tasks from old project
tasks = client.tasks.find_all({'project': OLD_PROJECT_ID})


# Method to update old task data for new task
def update_old_task(task_data):
    # necessary deletions
    del task_data['workspace']
    del task_data['hearted']
    del task_data['resource_type']
    del task_data['created_at']
    del task_data['modified_at']
    del task_data['completed_at']
    del task_data['memberships']
    del task_data['hearts']
    del task_data['num_hearts']
    del task_data['likes']
    del task_data['num_likes']
    del task_data['assignee_status']

    # update task to new project
    task_data['projects'] = [NEW_PROJECT_ID]

    return task_data


# loop through task
for task in tasks:
    # get detailed task information
    task_obj = client.tasks.find_by_id(task['id'])

    # remove unwanted items
    task_obj = update_old_task(task_obj)
    print(task_obj)

    # create new task
    client.tasks.create_in_workspace(new_workspace_id, task_obj)
