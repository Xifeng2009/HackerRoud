# coding=UTF-8
# time: 17-12-27: 下午3:48 
# Author: Xifeng2009

import zipfile, argparse
from threading import Thread


def extractFile(zFile, password):

    try:
        zFile.extractall(pwd=password)
        print("[+] Found Password " + password + "\n")
        # return password
    except:
        return

def main():

    '''参数解析'''
    parser = argparse.ArgumentParser("usage%prog -f <zipfile> -d <dictionary>")
    parser.add_argument('-f', dest='zname', type=str, help='specify zip file')
    parser.add_argument('-d', dest='dname', type=str, help='specify dictionary file')
    args = parser.parse_args()
    if (args.zname == None) | (args.dname == None):
        print(parser.usage)
        exit(0)
    else:
        zname = args.zname
        dname = args.dname

    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    for line in passFile.readlines():
        password = line.strip('\n')
        '''多线程'''
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()
        # guess = extractFile(zFile, password)
        # if guess:
        #     print("[+] Password = " + password + "\n")
        #     exit(0)

if __name__ == '__main__':
    main()

# 原始代码
# zFile = zipfile.ZipFile("evil.zip")
# passFile = open('dictionary.txt')
# for line in passFile.readlines():
#     password = line.strip('\n')
#     try:
#         zFile.extractall(pwd=password)
#         print("[+] Password Found: " + password + '\n')
#         exit(0)
#     except Exception as e:
#         pass