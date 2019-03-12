# Python解析unicode转义

```python
a = b"\u7f8a\u7531\u5927\u4e95\u592b\u5927\u4eba\u738b\u4e2d\u5de5"
a.decode("unicode-escape")
# '羊由大井夫大人王中工'
```
