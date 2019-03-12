# NCR 编码解码

引自维基百科
> 字符值引用 (numeric character reference, NCR)是在标记语言SGML以及派生的如HTML与XML中常见的一种转义序列结构，用来表示Unicode的通用字符集 (UCS)中的单个字符. NCR可以表示在一个特定文档中不能直接编码的字符，而该标记语言阅读器软件把每个NCR当作一个字符来处理。

NCR（Numeric Character Reference）编码是由一个与号(&)跟着一个井号(#), 然后跟着这个字符的Unicode编码值, 最后跟着一个分号组成的。

那怎么将 NCR 字符转换成文字

## 方法一

利用 chr 和 ord 函数解码

- `chr`返回值是当前整数对应的字符。参数可以是10进制也可以是16进制的形式。
- `ord`参数是一个字符，返回值是对应的十进制整数

```python
>>> ord("蛇")
34503
>>> chr(34503)
'蛇'
>>> hex(34503)
'0x86c7'
>>> chr(0x86c7)
'蛇'
```

我们可以用这组函数来解码 NCR 转义的字符了

```python
import re

def ncr_unescape(s):
    return re.sub("&#(\d+)(;|(?=\s))", lambda x: chr(int(x.group(1))), s)

html = r'商品标题：&#22825;&#28982;&#27668;&#34892;&#19994;&#27861;&#24459;&#23454;&#21153;'
print(ncr_unescape(html))
# 商品标题：天然气行业法律实务
```

## 方法二

Python 有内置的标准库来解码，使用起来更为简便
```python
from html.parser import HTMLParser

html = r'商品标题：&#22825;&#28982;&#27668;&#34892;&#19994;&#27861;&#24459;&#23454;&#21153;'

html_parser = HTMLParser()
print(html_parser.unescape(html))
# 商品标题：天然气行业法律实务
```
