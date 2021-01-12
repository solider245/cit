#!/usr/local/bin/env python
#from sh import git
import subprocess # 导入子模块

def 网址替换(url):
    
    list_url = list(url)                          # 将字符串替换为列表
    list_url.insert(18,'.cnpmjs.org')             # 在指定位置插入对应字符串
    cn_url = "".join(list_url) 
    print(f'您好,{cn_url}是替换后的网址,\n正在为您下载')
    

def clone(cn_url):
    cn_url = 网址替换(url)
    subprocess.call(['git', 'clone',cn_url])    
    
def submodule(cn_url):
    cn_url = 网址替换(url)
    subprocess.call(['git', 'submodule','add' , cn_url])     
 
def main():

    cn_url = 网址替换(url =input('请输入您的网址:\n'))
    clone(cn_url)
#print (download)
if __name__ == '__main__':
    main()