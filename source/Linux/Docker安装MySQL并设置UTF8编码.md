# Docker安装MySQL并设置UTF8编码

这么理解吧

docker中所说的image（镜像）相当于创建虚拟机时使用的iso文件

docker中所说的container（容器）相当于你创建的虚拟机


### 创建容器

```sh
# 拉取镜像
sudo docker pull mysql/mysql-server:5.7
# 从镜像中创建容器
sudo docker run \
    -v /数据文件保存目录:/var/lib/mysql \
    -v /配置文件目录/mysqld_charset.cnf:/etc/mysql/my.cnf \
    --name=mydb \
    -p 3306:3306 \
    -e MYSQL_ROOT_PASSWORD=root \
    -d mysql/mysql-server:5.7
```

配置文件mysqld_charset.cnf，内容如下:
```
[mysqld]
character_set_server=utf8
character_set_filesystem=utf8
collation-server=utf8_general_ci
init-connect='SET NAMES utf8'
init_connect='SET collation_connection = utf8_general_ci'
skip-character-set-client-handshake
```

**注意**: mysqld_charset.cnf文件权限不能过大，拥有者有读写权限即可，这里我设置为644

若启动时没有设置密码，会生一个随机密码。登陆后需要重新设置

```sh
# 查看密码
sudo docker logs mydb
# 进入容器
sudo docker exec -it mydb mysql -uroot -p
# 修改密码
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'passwd123';
```

### 设置root用户允许外部访问

```sh
# 进入容器
sudo docker exec -it mydb mysql -uroot -p
# 设置root用户允许外部访问
mysql> use mysql;
mysql> UPDATE user SET host = '%' WHERE user = 'root';
```


### 查看字符集

```sh
mysql> SHOW VARIABLES LIKE '%char%';
mysql> SHOW VARIABLES LIKE 'collation_%';
```


### 设置导入文件大限制

```sh
mysql> SET GLOBAL max_allowed_packet=1024*1024*1024;
```

### 进入容器

```sh
sudo docker exec -it mydb /bin/bash
```

### 启动容器

```sh
sudo docker start mydb
```

### 删除容器

```sh
sudo docker rm mydb
```
