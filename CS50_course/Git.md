# Git

### Git config

设置用户名，邮箱

```shell
git config --global user.name "runoob"
git config --global user.email test@runoob.com
```

查看配置信息

```shell
git config --list
```


生成ssh密钥

```shell
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"
```

此时将在主文件夹生成公钥和私钥，如需要配置Github，可将后缀为.pub的公钥文件填入Github账户设置中。


使用vscode打开文件

```shell
`code<filename>` 
```

### Git Repository


初始化仓库

```shell
git init
```



克隆仓库

```shell
git clone <url>
```



读取目录

```shell
cd <filename>
```



回退目录到上一级

```shell
cd ..
```



提交到暂存区

```shell
git add <filename>
```



提交暂存区到本地仓库

```shell
git commit -m  "message" 
git commit -am "message" 提交所有更改
```




告知当前状态

```shell
git status
```



添加注释

```shell
git notes
```



上传远程代码并合并

```shell
git push
```


下载最新版本仓库

```shell
git full
```



查找更改日志

```shell
git log
```



恢复旧版本

```shell
git reset --hard<commit>
git reset --hard origin/master
```



### Git branch

查看分支

```shell
git branch
```


创建新分支

```shell
git checkout -b <branchname>
```


切换分支

```shell
git checkout <branchname>
```


合并分支（先转到主分支）

```shell
git checkout main
git merge <branchname>
```


合并冲突(Merge Conflicts)


当多人针对同一行代码进行修改后，可能会面临合并冲突，需要解决该种冲突之后才能再次git push



推送合并后的分支

```shell
git push origin main
```



删除分支

```shell
git branch -d <branchname>
```


### Git tags

为快照打标签

```shell
git tag  -a v1.0
```



推送标签

```shell
git push origin <tagname>
git push origin --tags 推送所有标签
```



删除标签

```shell
git tag -d <tagname> 本地删除
git push origin --delete <tagname>
```

