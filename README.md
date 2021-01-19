## 序言
github上有很多好项目,但是国内用户连github却非常的慢.每次都要用插件或者其他工具来解决.
这次自己做一个小工具,输入github原地址后,就可以自动替换为代理地址,方便大家更快速的下载.

<!-- more -->
## 安装
```shell
pip install cit
```
## 主要功能与用法

### 主要功能
* change 将目标地址转换为加速后的地址
* clone 常见的git加速,最快10M/s,有时候慢一点
* sub git子模块加速,等同于git submodule add
* get 就是单纯的下载功能


### 示例用法

1. `clone`功能:等效于 `git clone <url>`
```shell
cit clone <url>
# 示例
cit clone https://github.com/solider245/cit.git
```

![20210117184201_a0bb88c0f05074e9936d59be10ee1f7f.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20210117184201_a0bb88c0f05074e9936d59be10ee1f7f.png)

如上图所示,输入一个数字,选择一个链接即可开始下载.默认使用0.

2. `sub`功能:  等效于`git submodule add <url>`
```shell 
cit sub <url>
# 案例
cit sub https://github.com/solider245/cit.git
```
逻辑和git clone一样,这里就不放图了.

3. `get`功能:  等效于 `wget`下载
get功能会根据你的输入,智能判定下载raw文件或者release文件
使用示例:
```shell
cit get <url>
# 案例
cit get https://github.com/cheat/cheat/archive/4.2.0.zip   
```

* 下载raw文件
![20210117195105_c1631ea82365332e2fa165f347a9bf96.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20210117195105_c1631ea82365332e2fa165f347a9bf96.png)



![20210117194012_574bf5e906eb1b18b3b9615d7e8b295d.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20210117194012_574bf5e906eb1b18b3b9615d7e8b295d.png)

下载安装包.
![20210119184535_9e6b84fa7e79b955d6b2c8928a50ee1e.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20210119184535_9e6b84fa7e79b955d6b2c8928a50ee1e.png)

如上图所示,因为是使用https下载,所以速度快点惊人,如果下载速度太慢可以选择别的地址.我目前测试下来,基本都能用.

## 其他功能

- [x ] 常用软件下载,类似python,go等下载
- [x ] 常用系统加速,类似ubuntu或者centos等加速
- [] 其他常用功能

欢迎询问或者给我[邮箱](mailto:solider245@gmail.com)发邮件.
