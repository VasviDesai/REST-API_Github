# REST-API_Github
Basic interaction with Github's REST API using a python code.

## LIBRARIES
Two libraries used - requests and json. <br/>
requests library can be installed by using the command, on the command prompt: `pip install requests` <br/>
json library is generally present in all minimal versions of python, if not present it can be installed in a similar manner <br/>
Both the libraries are imported in the code in *lines 5 and 6*.


## HEADERS
Before getting to the tasks for the homework, there were mainly three headers that were defined in *lines 11, 13 and 15* of the code: head_auth, accept_header and accept_header2. <br/><br/>
**_head_auth_** header was defined for authentication purposes which is needed for performing certain tasks of the homework. The authentication is done using a github token. <br/>
**Token** string is used for authentication, and it can be very easily generated using the github interface. <br/>
To generate the token, Login to your account -> Click on Settings -> Click on Developer Settings -> Click on Personal Access Tokens -> Click on Generate a new token -> Give a description to the token -> Define the scopes and permissions (do select user and repo) -> Click on Generate Token. A string is generated and this token string can be used in the code for authentication. In line 8 of the code, replace '<my_token>' by the actual token string for example '123456789abcdefg' for execution. <br/> <br/>
**_accept_header1_** is the custom media type accept header along with authentication needed for Tasks 1.3 and 1.4 <br/> <br/>
**_accept_header2_** is the custom media type accept header along with authentication needed for Task 1.6


## TASKS

### Task 1.1 List All Branches - 
*Lines 18 to 23* in the code refer to this task and the function that corresponds to this task is **_T1_ListAllBranches(user,repo)_** <br/>
This function is called and defined using the github username and repository name as parameters for listing all the branches of that particular repository of that user. <br/>
The function is defined is defined from *lines 18 to 21* and the function is called on *line 23*. <br/>
The function call is written as: `T1_ListAllBranches('<user_name>', '<repository_name>')` 
So, the defined function for Task 1.1 can executed by just replacing <user_name> and <repository_name> with appropriate values. <br/>
For example, `T1_ListAllBranches('User1', 'Repo1')`


### Task 1.2 Create A New Repo - 
*Lines 26 to 32* in the code refer to this task and the function that corresponds to this task is **_T2_CreateANewRepo(repo_name, repo_description)_** <br/>
This function is called and defined using the github repository name and descriptions for the new repository to be created as parameters. <br/>
The function is defined is defined from *lines 26 to 30* and the function is called on *line 32*. <br/>
The function call is written as: `T2_CreateANewRepo('<repository_name>', '<repository_description>')` 
So, the defined function for Task 1.2 can executed by just replacing <repository_name> and <repository_description> with appropriate values. <br/>
For example, `T2_CreateANewRepo('NewRepo', 'This is the new repository!')`


### Task 1.3 Create An Issue - 
*Lines 35 to 41* in the code refer to this task and the function that corresponds to this task is **_T3_CreateAnIssue(user, repo, issue_title, issue_body)_** <br/>
This function is called and defined using the github username, repository name, issue title and body for the new issue to be created for that repository as parameters. <br/>
The function is defined is defined from *lines 35 to 39* and the function is called on *line 41*. <br/>
The function call is written as: `T3_CreateAnIssue('<user_name>', '<repository_name>', '<issues_title>', '<issues_body>')` 
So, the defined function for Task 1.3 can executed by just replacing <user_name>, <repository_name>, <issues_title> and <issues_body> with appropriate values. <br/>
For example, `T3_CreateAnIssue('User1', 'NewRepo', 'NewIssue - Bug Found', 'Cannot execute this!')`


### Task 1.4 Add An Assignee - 
*Lines 44 to 50* in the code refer to this task and the function that corresponds to this task is **_T4_AddAnAssignee(user, repo, issue_number, assignee_name)_** <br/>
This function is called and defined using the github username, repository name, issue number and name of the assignee to be added for the particular issue to be created for that repository as parameters. <br/>
The function is defined is defined from *lines 44 to 48* and the function is called on *line 50*. <br/>
The function call is written as: `T4_AddAnAssignee('<user_name>', '<repository_name>', '<issues_number>', '<assignees_name>')` 
So, the defined function for Task 1.4 can executed by just replacing <user_name>, <repository_name>, <issues_number> and <assignees_name> with appropriate values. You can either add yourself as an assignee or it has to be one of the collaborators. <br/>
For example, `T4_AddAnAssignee('User1', 'NewRepo', '1', 'User2')`


### Task 1.5 Edit A Repo - 
*Lines 53 to 59* in the code refer to this task and the function that corresponds to this task is **_T5_EditARepo(user, repo, repo_name, repo_description)_** <br/>
This function is called and defined using the github username, repository name, edited repository name and description for that repository as parameters. <br/>
The function is defined is defined from *lines 53 to 57* and the function is called on *line 59*. <br/>
The function call is written as: `T5_EditARepo('<user_name>', '<repository_name>', '<editedrepository_name>', '<editedrepository_description>')` 
We also disable issues in this task, by setting has_issues to false, in *line 54* of the code, i.e. `new_data = {'name': repo_name, 'description': repo_description, 'has_issues': 'false'}` 
So, the defined function for Task 1.5 can executed by just replacing <user_name>, <repository_name>, <editedrepository_name> and <editedrepository_description> with appropriate values. <br/>
For example, `T5_EditARepo('User1', 'NewRepo', 'EditedRepo', 'Repository has been edited!')`


### Task 1.6 List Reactions - 
*Lines 62 to 67* in the code refer to this task and the function that corresponds to this task is **_T6_ListReactions(user, repo, issue_number)_** <br/>
This function is called and defined using the github username, repository name and issue number for the particular issue for which the reactions have to be printed for that repository as parameters. <br/>
The function is defined is defined from *lines 62 to 65* and the function is called on *line 67*. <br/>
The function call is written as: `T6_ListReactions('<user_name>', '<repository_name>', '<issues_number>')` 
So, the defined function for Task 1.6 can executed by just replacing <user_name>, <repository_name> and <issues_number> with appropriate values. <br/>
For example, `T6_ListReactions('User1', 'EditedRepo', '1')`



