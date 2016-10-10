#! /bin/bash

# should be run in place

root=$(pwd)
temp_dir=$root/update-fontawesome
remote_url=https://github.com/FortAwesome/Font-Awesome.git 
remote=fontawesome
desired_dirs=(fonts css)

mkdir $temp_dir
cd $temp_dir

git clone $remote_url $remote

main_repo=$temp_dir/$remote
cd $root
git remote add $remote $main_repo

for name in "${desired_dirs[@]}"
do
    :
    cd ${main_repo}
    echo "Splitting subtree for ${name}..."
    git subtree split --prefix=${name}/ -b ${name} > /dev/null 2>&1
    cd $root
    echo "Fetching new branch..."
    git fetch ${remote}
    echo "Pulling changes for ${name} into index..."
    git merge -X subtree=pelicanfly/static/${name} remotes/${remote}/${name} --no-commit
    changes=$(git status --porcelain 2>/dev/null | grep "^[MA]" | wc -l)
    if [ "${changes}" -gt 0 ]
    then
        echo "Changes detected!"
        git add .
        git commit -m "Auto-merge for subtree of ${name} from ${remote_url}"
    else
        echo "No changes here."
        git merge --abort
    fi
done

echo "Cleaning up..."

git remote rm ${remote}
rm -rf $temp_dir
