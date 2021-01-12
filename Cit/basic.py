
def 网址替换(url):
    
    list_url = list(url)                          # 将字符串替换为列表
    list_url.insert(18,'.cnpmjs.org')             # 在指定位置插入对应字符串
    cn_url = "".join(list_url) 
    #print(f'您好,{cn_url}是替换后的网址,\n正在为您下载')
    return cn_url
    

""" def clone(cn_url):
    cn_url = 网址替换(url =input('请输入您的网址:\n'))
    subprocess.call(['git', 'clone',cn_url])  """

cn_url = 网址替换('https://github.com/tankywoo/simiki.git')    
print(cn_url)