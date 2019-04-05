# Python script to transfer Projects

This project helps in transferring task from one project to another. 
This works when transferring from one workspace to another.

#### How to use :

1. Before you start, you may need to set up a few things that the tool can't do on its own though the API.

1. Add your new user account (for your destination workspace) to your old workspace, if not already using the same email address
1. Log in to Asana with your new account
1. Add any user accounts you want to keep task assignments for to the new workspace
1. Add any custom fields you want to keep to the new workspace (pro workspaces)

#### Use of this project :

1. Download the project
1. Install packages in requirement.txt `pip install -r requirements.txt`
1. In `transferProject.py` file add your personal api key, old and new project ID
1. Then run the script

NOTE : Some of the information is not transferred


Feel free to report bugs and features in github!!
