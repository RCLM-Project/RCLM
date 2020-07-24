Procedural documentation for using Git and GitHub by the RCLM. Written by Caitlin Postal.

More information and instructions available in GitHub Guides: https://guides.github.com/activities/hello-world/ 

# (IN PROGRESS)
github desktop directions
vsc/command line directions

## User Interface
Be prepared to use the "GitHub Desktop" app or the command line. Please do not upload any materials through the browser-based GUI.

Git is complex. This guide will document a step-by-step procedure for RCLM team members to follow. If you run into an issue while using Git and GitHub, please contact the technical team (Kelly Mahaffy and Caitlin Postal).

Caitlin Postal recommends using Visual Studio Code.

## Work Sessions

### Fetch
At the beginning of every work session, use "Fetch origin" to clone the most up to date repository.

It is important to fetch the most recent files and to update your files in the main repository in every working session.

### Branch
Team members will use branches for version control. It is imperative that each team member work on a branch not on the main repo itself.  You will work on a branch during your working session, then merge back at the end of your session. In the next working session, you will pull changes from the main repo ("master") into your branch, then merge back at the end. This process should prevent commit conflicts, which is helpful when we are working in multi-thousand line files. Using this method will offer an intentional merge of any changes rather than a conflict or error. 

In Visual Studio Code (or another IDE), 

### Local Commit 
Save changes locally as frequently as possible.

Commit changes locally as necessary after saving. To do this in Visual Studio Code (or another IDE), first navigate to Source Control in your text editor (ctrl+shift+g in Visual Studio Code). Using the file name under the "Changes" dropdown, click the plus to "Stage Changes." The file name will now be under the "Staged Changes" dropdown. To commit locally, click the check mark to the right of "Source Control" (above the "Staged Changes" and "Changes" dropdown menus).

At the end of every work session, save and commit your changes.

### Merge Branch

### Commit/Push to Repo

When ready to commit to the main repository ("master"), there are two methods.

To commit from Visual Studio Code

To commit from GitHubDesktop, 


Within GitHub Desktop, "Push origin" in the top navigation bar and "Commit to master" in the lower left corner serve the same function of sending your updated files to the main repository on GitHub.