Want to investigate what oppertunities exist for workflow in digital marketing project lifecycles.
The end "deliverable" is a pack/ collection of images, movies, gifs and other documents.
A google sheet is created as a "quick-ref" for client but also serves as basis for ad performance tracking.

- set up git repo
- clone to local
- start writing notes and ideas
- Add files to mini-project folder and write brief steps for reference
- start new mini-project Google API Hello World
- made branch on github - googleAPI-hello
- tried to switch to branch without pulling, did not match files
- pulled and switched, checked with git branch, also bottom lefthand of vscode
- create env file
- read the docs - [quickstart](https://developers.google.com/drive/api/quickstart/python)
- what packages and libraries off the top of my head?
  - dotenv
  - google client library
- steps

  - check Prerequisites
    - Python 3.10.7 or greater [x]
    - The pip package management tool [x]
    - A Google Cloud project. [x] ----> NAME:test-creation , ID:test-creation
    - A Google account with Google Drive enabled. [x]
  - Set up your environment
    - Enable the API
  - Configure the OAuth consent screen
    - pipenv
    - app name is docs-workflow
    - have no idea about some of the OAuth details - see screenshot
    - also no idea for scopes
    - _also no idea for test users_
    - BUT added g-mail account
    - review summary, is there a way to come back to this? surely?
      messing around with a logo
  - Authorize credentials for a desktop application
  - in ? has OAuth 2.0 Client IDs and API keys
  - have chosen OAuth as per instructions
  - before saving credentials.json add to .env and push
  - created ENV folder to organise credentials

  ```bash
  pipenv install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
  ```

error of pipenv.vendor.requirementslib.exceptions.RequirementError: Failed parsing requirement from '--upgrade'

made quickstart.py
copied and pasted text from:
https://github.com/googleworkspace/python-samples/tree/main/drive/quickstart

tried running, couldnt find credentials:

FileNotFoundError: [Errno 2] No such file or directory: 'credentials.json'
-moved creds back to top level
-check for personal info
-push
-merge branches

- articles of use cases
- talk to contact where can be used

Steps:
pipenv
.env file to ignore env
set up env in file
what packages to install
hello world tutorial for google python SDK

naming conventions? how do these affect things
why have they chosen this set up, are there any other alternatives

# Mini Projects

## doclist-parser

- Interested in collecting finished products, they are nested within folders
- In google docs, search for extensions of .png
- brings back list of docs
- want the share>copylink address for all files
- dev tools copy all html
- files.py finds names of files and unique id, then can generate the link
- outputs to csv, could copy and paste.
