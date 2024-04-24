# !/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
import sys
import zlib

class Git:
    def __init__(self, repo=None):
        self.repo = '.' if repo is None else repo 
        self.git_dir = self.repo + "/.git/"
        self.head_file = self.git_dir + "HEAD"
        self.branch_file = ''
        self.head_tag = ''
        
    def read_head(self):
        try:
            with open(self.head_file, 'r') as file:
                data = file.read()
            if data[0:4] != 'ref:':
                print("read_head: wrond data: ", data)
                exit(0)
            self.branch_file = data[5:].strip()
            #print(self.branch_file)
            fn = self.git_dir + self.branch_file
            with open(fn, 'r') as file:
                data = file.read()
                self.head_tag = data.strip()
            #print(self.head_tag)
        except Exception as e:
            print('raed head failed', e)
        
    def log(self):
        self.read_head()
        self.read_file(self.head_tag)

    # tree len \x0 mode filename \x0 tag
    # blob len \x0 contents
    # commit len \x0
    def read_file(self, tag):
        try:
            while True:
                fn = self.git_dir + 'objects/' + tag[0:2] + '/' + tag[2:]
                with open(fn, 'rb') as file:
                    data = file.read()
                    bytes = zlib.decompress(data)
                if bytes[0:6] != b'commit':
                    print('unkown date type: ', bytes)
                    return
                commit_bytes = bytes.split(b'\n\n',2)
                header_bytes = commit_bytes[0]
                msg_bytes = commit_bytes[1]
                
                cmmit_headers_bytes = header_bytes.split(b'\x00')
                #cmmit_headers_bytes[0]
                headers_bytes = cmmit_headers_bytes[1].split(b'\n')
                #print(headers_bytes)
                committer = author = parent = tree = None

                for h in headers_bytes:
                    if h[0:5] == b'tree ':
                        tree = h[5:].decode('utf-8')
                    elif h[0:7] == b'parent ':
                        parent = h[7:].decode('utf-8')
                    elif h[0:7] == b'author ':
                        author = h[7:].decode('utf-8')
                    elif h[0:10] == b'committer ':
                        committer = h[10:].decode('utf-8')
                #print('commit', tag)
                #print('Author', author)
                ##print('Date', date)
                #msg = msg_bytes.decode('utf-8')
                #print('')
                #print(msg)
                txt = bytes.decode('utf-8')
                print(txt)

                if parent is None:
                	break
                tag = parent

        except Exception as e:
            print('read_file failed', e)


def main():
    repo = '.'
    if len(sys.argv) > 1:
        repo = sys.argv[1]

    git = Git(repo)
    git.log()

if __name__ == '__main__':
    main()