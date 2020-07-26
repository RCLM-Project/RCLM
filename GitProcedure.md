# ***DO NOT USE THIS DOCUMENTATION YET.***
Procedural documentation for using Git and GitHub by the RCLM. Written by Caitlin Postal.

More information and instructions available in GitHub Guides: https://guides.github.com/activities/hello-world/ 

# (IN PROGRESS)
github desktop directions
vsc/command line directions

## User Interface
Be prepared to use the "GitHub Desktop" app or the command line. *Do not upload any materials through the browser-based GUI.*

Git is complex. This guide will document a step-by-step procedure for RCLM team members to follow. If you run into an issue while using Git and GitHub, please contact the technical team (Kelly Mahaffy and Caitlin Postal).

Caitlin recommends using Visual Studio Code or another integrated development environment (IDE) as you can implement commits directly from the IDE.

# Work Sessions

## Fetch
At the beginning of every work session, use "Fetch origin" to clone the most up to date repository.

It is important to fetch the most recent files and to update your files in the main repository in every working session.

## Branch
Team members will use branches for version control. It is imperative that each team member work on a branch not on the main repo itself.  You will work on a branch during your working session, then merge back at the end of your session. In the next working session, you will pull changes from the main repo ("master") into your branch, then merge back at the end. This process should prevent commit conflicts, which is helpful when we are working in multi-thousand line files. Using this method will offer an intentional merge of any changes rather than a conflict or error. 

When you create a new branch, label it with your editor identifier and the date.

#### Working on branches
All team members should do collaborative work on their designated dev branch (for example, the Wynken 1509 collaborators will commit their work to the dev_wynken1509 branch). You can create a subbranch from the dev branch to do individual work and practice branching but ***please do not commit work to the main repository until you have practiced committing to branches.***

pull request to commit to main


##### Create a branch in Visual Studio Code (or another IDE):
1. Navigate to Source Control tab (ctrl+shift+g in VSC).
2. Click the meatballs menu (three horizontal dots which offer a dropdown menu) to the right of "Source Control" (above the "Staged Changes" and "Changes" dropdown menus).
3. Select "Checkout to" in order to create a new branch with your name in the file extension.

##### Create a branch in GitHub Desktop:
1. Navigate to the Current Branch button in the middle of the top row of buttons and ensure that you are in the correct branch (within a named folder if working on a witness).
2. Click on Current Branch and then select the New Branch button. 
3. Name your branch with your editor tag and the date. It will give you the option to base the branch in the Master branch or your current branch, be sure to select your current branch.
4. You will automatically be moved to working in the newly created branch, which you can check by looking at the Current Branch button. 

## Local Commit 
Save and commit changes locally as frequently as possible. Recommended: save frequently, commit locally at least once per hour and at the end of every work session. ***Do not use the GitHub browser GUI to commit any changes.***

#### Local commit in Visual Studio Code (or another IDE):
1. Navigate to Source Control in your text editor (ctrl+shift+g in Visual Studio Code).
2. Using the file name under the "Changes" dropdown, click the plus sign next to the file name to "Stage Changes." The file name will now be under the "Staged Changes" dropdown. 
3. To commit locally, click the check mark to the right of "Source Control" (above the "Staged Changes" and "Changes" dropdown menus).

At the end of every work session, save and commit your changes.

## Merge Branch

## Push to Repo

When ready to commit to the main repository ("master"), there are two methods.

#### To push from Visual Studio Code
After you have staged and committed changes locally, it's time to push them to the remote repository. 
1. Navigate to Source Control in your text editor (ctrl+shift+g in Visual Studio Code).
2. Click the meatballs menu (three horizontal dots which offer a dropdown menu) to the right of "Source Control" (above the "Staged Changes" and "Changes" dropdown menus) and select "Push to."
3. Choose the intended branch to push your changes to (usually either a dev branch or the main repo "master").
4. Type a brief summary to note what the changes are (date and 2-3 word recap: for example, 7/24 procedure update).

#### To push/commit from GitHub Desktop
After you have staged and committed local changes, the Desktop client will load a light blue box that says "Push commits to origin remote" with text identifying how many local commits are waiting to be pushed to GitHub. You can either:
- Use the dark blue "Push origin" button in the light blue "Push commits to the origin remote" box.
or
- Click the "Push origin" section on the top navigation bar (it will either say "push origin" or "fetch origin").


Within GitHub Desktop, "Push origin" in the top navigation bar and "Commit to master" in the lower left corner serve the same function of sending your updated files to the main repository on GitHub.
