# Ubuntu开启cron日志

1、 修改文件
```sh
sudo nano /etc/rsyslog.d/50-default.conf
```
将前面的#删掉
```sh
cron.*                          /var/log/cron.log
```

2、重启rsyslog
```sh
sudo service rsyslog restart
```

3、查看crontab日志
```sh
tail /var/log/cron.log
```
