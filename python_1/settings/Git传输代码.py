#git init 初始化仓库
cd /E/Git
mkdir Rscript
cd Rscript
git init

#git status 查看仓库状态
git status
touch README.md #新建README文件
#git add 向暂存区添加文件
git add README.md
git add file1 file2 file3
# 添加指定目录下的文件 config目录下所有文件，home目录下所有.php文件
git add config/*
git add home/*.php
# git add . 添加所有文件，或者git add --all 添加所有文件

git
git status

#git commit 保存仓库的历史记录
git commit -m "First commit"

#git log 查看提交日志
git log
git log --pretty=short #只显示一行简述信息
git log README.md #显示指定目录、文件的改动
git log -p #显示改动后的前后差别

#git diff 查看更改前后的差别
git diff
git add README.md
git diff HEAD #查看工作树与最新提交的差别
git commit -m "Add index"

#分支的操作
git branch #显示分支
git checkout -b #创建、切换分支
git checkout -b feature-A
git add README.md
git commit -m "Add feature-A"
git checkout master
git checkout - #切换回上一层分支
# git merge 合并分支
git merge --no-ff feature-A
git log --graph 以图表形式显示分支

#git reset 回溯历史版本
git reset --hard 07d4ca36f6b92c4656b1986757fce27e7780dd1c
#哈希值通过git log获得
git checkout -b fix-B
git add README.md
git commit -m "Fix B"
git reflog #查看当前仓库执行过的操作的日志
git checkout master
git reset --hard 7c704d7
git merge --no-ff fix-B
git add README.md
git commit -m "Fix confilct"

#git commit --amend 修改提交信息
git commit --amend
#vim 文本编辑器，
#i-插入文本，l-当前行的行首，
#a-将新文本追加到光标当前所在位置之后，
#A-将新文本追加到所在行的行尾
#空行插入命令，o-命令将在光标所在行的下面插入一个空行，并将光标置于该行的行首。
#O-命令在光标所在行的上面插入一个空行，并将光标置于该行的行首。
# Esc 退出编辑状态
#：WQ (保存并退出)，或者shift+zz
#正常退出，：q, 不保存退出 ：q! 强制退出 ：！

#git rebase -i——压缩历史
git checkout -b feature-C
git commit -am "Add feature-C"
git diff
git commit -am "Fix typo"
git rebase -i HEAD~2
git checkout master
git mege --no-ff feature-C

#推送至远程仓库
 git remote add origin git@github.com:Christal0922/Rscript.git
 git push -u origin master

 git checkout -b feature-D
 git push -u origin feature-D
报错
git remote rm origin

#其他尝试
cd Rtest
git add --all
git commit -m "Rtest"
git remote rm origin
git remote add origin git@github.com:Christal0922/Rscript.git
git push -u origin feature-D

#从远程仓库获取
git clone https://hub.xn--gzu630h.xn--kpry57d/danielecook/Awesome-Bioinformatics.git
git clone git@github.com:github-book/git-tutorial.git

# 删除暂存区指定文件
git rm --cached readme.txt

# 清空暂存区
rm .git/index





