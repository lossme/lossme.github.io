# Chrome Flash插件已被拦截.md

在浏览某些网站的时候，会在地址栏里出现“插件已被拦截”提示，具体提示是：“该网页已屏蔽以下插件Adobe Flash Player”，选择运行所有插件，问题依旧。

解决办法
点击管理插件或打开`chrome://settings/content/flash`

在允许列表中添加`[*.]xxx.com:80`其中`xxx.com`是被拦截的网站网址

如果是https类型的，则添加`[*.]xxx.com:443`其中`xxx.com`是被拦截的网站网址

添加完之后，刷新刚才被拦截的网页就可以了
