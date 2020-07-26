# ***DO NOT USE THIS DOCUMENTATION YET.***
Procedural documentation for using Git and GitHub in the command line by the RCLM. Written by Kelly Mahaffy.

More information and instructions available in GitHub Guides: https://guides.github.com/activities/hello-world/

# (IN PROGRESS)
github desktop directions
vsc/command line directions

## User Interface
Be prepared to use the "GitHub Desktop" app or the command line. *Do not upload any materials through the browser-based GUI.*

Git is complex. This guide will document a step-by-step procedure for RCLM team members to follow. If you run into an issue while using Git and GitHub, please contact the technical team (Kelly Mahaffy and Caitlin Postal).

Caitlin recommends using Visual Studio Code or another integrated development environment (IDE) as you can implement commits directly from the IDE.

#Cloning the Repository to Your Computer
1. Copy the URL of the repository from the browser.
2. $ cd into where you would like to place this directory, or use $ mkdir to make a GitHub folder.
3. Once in the correct position for the directory, use git clone and the URL previously copied to clone the repo to your local device.
4. $ cd RCLM

# Work Sessions
All command assume that you are already in the correct directory

## Fetch
At the beginning of every work session, you should fetch new changes or updates to the repo in one of a few ways

1. $ git fetch RCLM to fetch the entire repo or $ git fetch RCLM <branch name> to fetch changes made in a specific branch. After fetching you will need to use $git merge origin/master to merge the changes. This is a bit clunky, but it always behaves the same way which is helpful.

2. $ git pull origin master can be used to pull new changes from the master branch, or you can use $git pull origin <branch-name> to pull changes in a branch. This is an easy and efficient way but sometimes does not behave as expected, so it is recommended for those experienced in the command line only.


It is important to fetch the most recent files and to update your files in the main repository in every working session.

## Branch
Team members will use branches for version control. It is imperative that each team member work on a branch not on the main repo itself.  You will work on a branch during your working session, then merge back at the end of your session. In the next working session, you will pull changes from the main repo ("master") into your branch, then merge back at the end. This process should prevent commit conflicts, which is helpful when we are working in multi-thousand line files. Using this method will offer an intentional merge of any changes rather than a conflict or error.

When you create a new branch, label it with your editor identifier and the date.

#### Working on branches
All team members should do collaborative work on their designated dev branch (for example, the Wynken 1509 collaborators will commit their work to the dev_wynken1509 branch). You can create a subbranch from the dev branch to do individual work and practice branching but ***please do not commit work to the main repository until you have practiced committing to branches.***

pull request to commit to main


##### Create a branch from the master
1. Use $ git branch <new-branch> while in the master branches

##### Create a branch within a branch
1. Use $ git branch <new-branch> <base-branch>

#### See all branches in a project
1. Use $ git branch

#### To switch between branches
1. Use $ git checkout <branch-name>. You can add a -b flag to create a new branch while your at it, for example $ git checkout -b <new-branch-name>

## Local Commit
Save and commit changes locally as frequently as possible. Recommended: save frequently, commit locally at least once per hour and at the end of every work session. ***Do not use the GitHub browser GUI to commit any changes.***


#### Local commit in another txt editor (Atom or similar):
1. To open a file, use $ texteditor <filename.extension> or similar, for example $ atom myfile.text
2. Make any edits and save locally.
3. Use $ git add <filename> to stage the changes. As a reminder, you will need to do this to stage all changes, so use this frequently.
4. Use $ git commit <filename> to commit those changes to your current branch. As a reminder, you can add a -m flag to add a short commit message directly on the command line.

#### To check for uncommitted changes
1. Use $ git status to see all of the uncommited changes within your current branch. It is recommended that you use git status to be sure that all files you expected to stage were staged properly.

## Push to the Branch (for in process work)
1. Use $ git push origin <branch-name>.

## Merge the branch
1. Use $ git merge origin/<branch-name>.

## Push to Repo

When ready to commit to the main repository ("master"), there are two methods.

#### To push to Master
1. Use $ git push origin master to push to the Master branch of the repo.
