

import subprocess # 导入子模块



""" def 网址替换(url):
    url= 'https://github.com/tankywoo/simiki.git'
    list_url = list(url)                          # 将字符串替换为列表
    list_url.insert(18,'.cnpmjs.org')             # 在指定位置插入对应字符串
    cn_url = "".join(list_url) 
    

网址替换() """
""" # url= 'https://github.com/tankywoo/simiki.git' # 演示下载
url = input('您好,输入一个github原始下载地址:') # 写入用户输入地址
list_url = list(url)                          # 将字符串替换为列表
list_url.insert(18,'.cnpmjs.org')             # 在指定位置插入对应字符串
cn_url = "".join(list_url)                    # 将列表转换为新的字符串
print('现在开始下载')
#print(git('clone',cn_url))

subprocess.call(['git', 'clone',cn_url])      # 子模块开始下载
#print(cn_url)
print(f'已经完成下载,耗时:') """

def 网址替换(url):
    
    list_url = list(url)                          # 将字符串替换为列表
    list_url.insert(18,'.cnpmjs.org')             # 在指定位置插入对应字符串
    cn_url = "".join(list_url) 
    print(f'您好,{cn_url}是替换后的网址,\n正在为您下载')
    return cn_url

def clone(cn_url):
    cn_url = 网址替换(url)
    subprocess.call(['git', 'clone',cn_url])    
 
def main():

    cn_url = 网址替换(url =input('请输入您的网址:\n'))
    clone(cn_url)
#print (download)
if __name__ == '__main__':
    main()



    

    
