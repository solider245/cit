url01 = 'https://github.com/cheat/cheat/archive/4.2.0.zip'
url02 = 'https://raw.githubusercontent.com/solider245/cit/master/poetry.lock'
url_list = [url01,url02]
参数_raw = 'raw.githubusercontent.com'
参数_github = 'https://github.com'
全部参数 = [参数_raw,参数_github]
def change(url):
    if 参数_raw in url :
        print('这是一个raw文件地址')
        raw_fastgit = url.replace('githubusercontent.com','fastgit.org')
        raw_sevencdn = url.replace('githubusercontent.com','sevencdn')
        raw_list = [raw_fastgit,raw_sevencdn]
        return raw_list
    elif 参数_github in url:
        print('这是一个github文件地址')
        list_url = list(url)                          # 将字符串替换为列表
        list_url.insert(18,'.cnpmjs.org')             # 在指定位置插入对应字符串 
        list_url_02 = list(url)
        list_url_02.insert(8,'gitclone.com/')
        cn_url = "".join(list_url)
        git_clone_url = "".join(list_url_02)
        fastgit = url.replace('github.com','download.fastgit.org')
        wuyan = url.replace('com','wuyanzheshui.workers.dev')
        url_list = [cn_url,git_clone_url,fastgit,wuyan]
        return url_list
    else:
        print( '地址错误,请输入一个合法的github地址')

def assect_url(url):
    chifun = 'https://github.91chifun.workers.dev//'+ url
    ghcon = 'https://gh.con.sh/'+ url
    api_999 = 'https://gh.api.99988866.xyz/' + url 
    xiu = 'https://github.xiu2.xyz/' + url  
    ghproxy = 'https://ghproxy.com/' + url 
    zwc365 = 'https://pd.zwc365.com/seturl/' + url

    assect_url = [chifun,ghcon,ghproxy,api_999,xiu,zwc365]
    return assect_url

def main(url):
    第一部分地址 = change(url)
    公共地址 = assect_url(url)
    所有地址 = 第一部分地址 + 公共地址
    num = len(所有地址)
    print(f'一共为您找到{num}个地址')
    for index,item in enumerate(所有地址):
        
        print(index,item)
    return 所有地址


if __name__ == "__main__":
    main(url02)
