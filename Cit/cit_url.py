""" 
这个模块用来解决地址链接转换问题
"""
url_test = 'https://github.com/cheat/cheat/archive/4.2.0.zip'
url_fastgit = 'https://download.fastgit.org/cheat/cheat/archive/4.2.0.zip'
url_wuyan = 'https://github.wuyanzheshui.workers.dev/cheat/cheat/archive/4.2.0.zip'
git_clone = 'https://gitclone.com/github.com/tendermint/tendermint.git'
url_91chifun = 'https://github.91chifun.workers.dev//https://github.com/cheat/cheat/archive/4.2.0.zip'
url_ghcon = 'https://gh.con.sh/https://github.com/cheat/cheat/archive/4.2.0.zip'
url_999 = 'https://gh.api.99988866.xyz/https://github.com/cheat/cheat/archive/4.2.0.zip'
url_xiu = 'https://github.xiu2.xyz/https://github.com/cheat/cheat/archive/4.2.0.zip'
url_ghproxy = 'https://ghproxy.com/https://github.com/cheat/cheat/archive/4.2.0.zip'
url_365 = 'https://pd.zwc365.com/seturl/https://github.com/cheat/cheat/archive/4.2.0.zip'

""" def 网址替换(url):
    url = url_test
    fastgit = url.replace('github.com','download.fastgit.org')
    wuyan = url.replace('com','wuyanzheshui.workers.dev')
    print(fastgit)
    return fastgit,wuyan """



def change(url):
    #url = url_test
    list_url = list(url)                          # 将字符串替换为列表
    list_url.insert(18,'.cnpmjs.org')             # 在指定位置插入对应字符串
    cn_url = "".join(list_url) 
    fastgit = url.replace('github.com','download.fastgit.org')
    wuyan = url.replace('com','wuyanzheshui.workers.dev')
    chifun = 'https://github.91chifun.workers.dev//'+ url
    ghcon = 'https://gh.con.sh/'+ url
    api_999 = 'https://gh.api.99988866.xyz/' + url 
    xiu = 'https://github.xiu2.xyz/' + url  
    ghproxy = 'https://ghproxy.com/' + url 
    zwc365 = 'https://pd.zwc365.com/seturl/' + url

    url_list = (cn_url,fastgit,wuyan,chifun,ghcon,api_999,xiu,ghproxy,zwc365)
    #for index,item in enumerate(url_list):
     #   print(index,item)
    return url_list


if __name__ == '__main__':        
    url_list = change(url = url_test)
    for index,item in enumerate(url_list):
        print(index,item)
    print(url_list[int(input('您好,请输入您要下载的链接序号:'))])   

    
    