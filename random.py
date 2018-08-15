
### Training workshop (Git) - 15 min ###

git config --global user.name "Name"
git config --global user.email "Email"

git --version # git version
git init # initializes a brand new Git repository
git clone "link" # clones to local
start notepad++ "filename"
git add "filename" # adds a file to staging
git add .
git add -A
git add *.py

git commit -m "some message" # save a version

git commit -am "some message" # in one step add and commit

git status # shows the current status of repository
git push # origin master - send changes to the repository
git pull # pull from repository to my PC
git log # log of all commits (history)

git reset --hard <commit hash for the desired version> # go back to a previous changes
git reset --hard origin/master # to use the cloud version


### Merge Conflicts ###
Resolve them

### Branching ###
Each branch has a version of the repository with its own commit history and current version

git branch # all current branches
git branch <branch name>

git checkout <branch name> # switch to the new branch
git merge <branch name> # merges a branch to the master branch (be careful of merge conflicts).

git branch -D <branch name> # delete the branch

### Other ###
touch "filename.txt" # create new file
touch .gitignore # add the file name that you don't want to include
git remote # list the remote repositories
git remote add origin https://... #add remote repository
git push -u origin master

Links:
https://guides.github.com/introduction/git-handbook/
