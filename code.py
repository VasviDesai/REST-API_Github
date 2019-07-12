# CSC 510

import requests 
import json

git_token = '<my-token>' # The user needs to add his/her token (generated through github here for authentication)
# List of all headers used in the code: 
# head_auth is a basic authentication header which uses the token
head_auth = {'Authorization': 'token {}'.format(git_token)}
# accept_header1 is the accept header along with authentication needed for Tasks 1.3 and 1.4
accept_header1 = {'Accept': 'application/vnd.github.symmetra-preview+json', 'Authorization': 'token {}'.format(git_token)}
# accept_header2 is the accept header along with authentication needed for Task 1.6
accept_header2 = {'Accept': 'application/vnd.github.squirrel-girl-preview+json', 'Authorization': 'token {}'.format(git_token)}

# Task 1.1 List All Branches - 
def T1_ListAllBranches(user, repo):
    r = requests.get('https://api.github.com/repos/' +user+ '/' +repo+ '/branches', headers = head_auth) 
    for branches in r.json():
        print(branches['name'])
# Function call for Task 1.1 - During function call must put in github username and repository name
T1_ListAllBranches('<user_name>', '<repository_name>')

# Task 1.2 Create A New Repo - 
def T2_CreateANewRepo(repo_name, repo_description): 
    new_data = {'name': repo_name, 'description': repo_description, 'homepage': 'https://github.com'}
    json_data = json.dumps(new_data)
    r = requests.post('https://api.github.com/user/repos', data = json_data, headers = head_auth)
    print(r.json())
# Function call for Task 1.2 - During function call must put in github repository name and description for the new repository
T2_CreateANewRepo('<repository_name>', '<repository_description>')

# Task 1.3 Create An Issue - 
def T3_CreateAnIssue(user, repo, issue_title, issue_body):
    new_data = {'title': issue_title, 'body': issue_body}
    json_data = json.dumps(new_data)
    r = requests.post('https://api.github.com/repos/' +user+ '/' +repo+ '/issues', data = json_data, headers = accept_header1)
    print(r.json())
# Function call for Task 1.3 - During function call must put in github username, repository name, issue title and body for the new issue
T3_CreateAnIssue('<user_name>', '<repository_name>', '<issues_title>', '<issues_body>')

# Task 1.4 Add An Assignee - 
def T4_AddAnAssignee(user, repo, issue_number, assignee_name):
    new_data = {'assignees': assignee_name}
    json_data = json.dumps(new_data)
    r = requests.post('https://api.github.com/repos/' +user+ '/' +repo+ '/issues/' +issue_number+ '/assignees', data = json_data, headers = accept_header1)
    print(r.json())
# Function call for Task 1.4 - During function call must put in github username, repository name, issue number and the name of the assignee added 
T4_AddAnAssignee('<user_name>', '<repository_name>', '<issues_number>', '<assignees_name>')

# Task 1.5 Edit A Repo - 
def T5_EditARepo(user, repo, repo_name, repo_description):
    new_data = {'name': repo_name, 'description': repo_description, 'has_issues': 'false'} # has_issues has been disabled by setting it to false
    json_data = json.dumps(new_data)
    r = requests.patch('https://api.github.com/repos/' +user+ '/' +repo, data = json_data, headers = head_auth)
    print(r.json())
# Function call for Task 1.5 - During function call must put in github username, repository name, edited reposiroty name and description 
T5_EditARepo('<user_name>', '<repository_name>', '<editedrepository_name>', '<editedrepository_description>')

# Task 1.6 List Reactions - 
def T6_ListReactions(user, repo, issue_number):
    r = requests.get('https://api.github.com/repos/' +user+ '/' +repo+ '/issues/' +issue_number+ '/reactions', headers = accept_header2)
    for reaction in r.json():
        print(reaction['content'])
# Function call for Task 1.6 - During function call must put in github username, repository name and the issue for which we want the reactions displayed
T6_ListReactions('<user_name>', '<repository_name>', '<issues_number>')

