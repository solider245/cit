import sys
url01 = 'https://github.com/cheat/cheat/archive/4.2.0.zip'
url02 = 'https://raw.githubusercontent.com/solider245/cit/master/poetry.lock'
url03 = 'https://mirrors.huaweicloud.com/python/3.9.1/Python-3.9.1.tar.xz'
url04 = '我觉得我是一个地址'
url_list = [url01,url02,url03,url04]
from string_utils import is_string,is_url
参数_raw = 'raw.githubusercontent.com'
参数_github = 'https://github.com'
参数_http = 'http'
全部参数 = [参数_raw,参数_github]

def 地址序号():
    try :
        num = int(input('请输入一个数字(默认为0):') )
    except ValueError :
        num = 0
    return num
def 列表(地址列表):
    print(f'一共找到{len(地址列表)}个地址')
    for index,item in enumerate(地址列表):
        print(index,item)
    

def assect_url(url):
    """
    这个函数负责所有逻辑比较简单的代理 
    """
    
    chifun = 'https://github.91chifun.workers.dev//'+ url
    ghcon = 'https://gh.con.sh/'+ url
    api_999 = 'https://gh.api.99988866.xyz/' + url 
    xiu = 'https://github.xiu2.xyz/' + url  
    ghproxy = 'https://ghproxy.com/' + url 
    zwc365 = 'https://pd.zwc365.com/seturl/' + url

    assect_url = [chifun,ghcon,ghproxy,api_999,xiu,zwc365]
    return assect_url
def change(url):
    if 参数_raw in url :
        print('这是一个raw文件地址')
        raw_fastgit = url.replace('githubusercontent.com','fastgit.org')
        raw_sevencdn = url.replace('githubusercontent.com','sevencdn')
        raw_list = [raw_fastgit,raw_sevencdn]
        公共地址 = assect_url(url)
        所有raw地址 = raw_list + 公共地址
        s = 列表(所有raw地址)
        num = 地址序号()
        你输入的地址 = 所有raw地址[num]
        print(f'你输入的地址是:{你输入的地址}')
        return 你输入的地址
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
        公共地址 = assect_url(url)
        所有url = 公共地址 + url_list
        s = 列表(所有url)
        num = 地址序号()
        你输入的地址 = 所有url[num]
        print(f'你输入的地址:{你输入的地址}')
        return 你输入的地址
    elif 参数_http in url :
        print('这个不是来一个来自github的地址')
        return url
        
    else:
        print( f'{url}:地址错误,请输入一个合法的github地址')
        sys.exit()



def main(url):
    s = change(url)
    return s


if __name__ == "__main__":
    main(url_list[0])
