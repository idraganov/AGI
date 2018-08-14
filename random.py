
### Training workshop (Git) - 15 min ###

git clone "link" # clones to local
start notepad++ "filename"
git add "filename" # adds a file to staging
git commit -m "some message" # save a version

git commit -am # in one step add and commit

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

git checkout # switch to the new branch
git merge <branch name> # merges a branch to the master branch (be careful of merge conflicts).



