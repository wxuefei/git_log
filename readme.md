## git log reader


Read the commit logs of git repository, just for studying git data structure.
```
python git.py <repository path>
```
output:
```
commit 212tree 6fc0b789d3240db347b1482f957d7e4b03837cc1
parent 367094c19c1d28b2d12dbba9aba7071c9dca3c57
author test <test@github.com> 1713937962 +0800
committer test <test@github.com> 1713937962 +0800

commit 2

commit 164tree 945a75091dea971311b3ad4b20dc88644bc3a3e6
author test <test@github.com> 1713936154 +0800
committer test <test@github.com> 1713936154 +0800

commit 1
```
## related git commands
command:
```
git hash-object readme.md
```
output:
```
b1eed291c8b5791339d3f0bf23a9ac8649275c1c
```
command:
```
git cat-file -p 8faa95c68edc8441ae31e5c59db64afbe7115ae4
```
output:
```
tree a009dac30318419af8559536b04bf5bfa0be39bf
author wuxuefei <wuxuefei@hotmail.com> 1713947683 +0800
committer wuxuefei <wuxuefei@hotmail.com> 1713947683 +0800

init
```
command:
```
git verify-pack -v .git\objects\pack\pack-a8593672eb6667432ed8ab42190e7756418852c6.idx
```
output:
```
8faa95c68edc8441ae31e5c59db64afbe7115ae4 commit 167 115 12
7ef8b7b43ac375b5d615d91b0385e4a76b0dc176 blob   3111 910 127
b1eed291c8b5791339d3f0bf23a9ac8649275c1c blob   548 288 1037
a009dac30318419af8559536b04bf5bfa0be39bf tree   71 79 1325
non delta: 4 objects
.git\objects\pack\pack-a8593672eb6667432ed8ab42190e7756418852c6.pack: ok
```

