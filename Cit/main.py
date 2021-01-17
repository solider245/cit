#!/usr/bin/python
import typer
import subprocess # 导入子模块
#from download import download
#import wget
# from cit_url import change
import requests
from tqdm.auto import tqdm

app = typer.Typer(help="从github的下载速度提高一万倍")
#@app.command()
def 地址序号():
    try :
        num = int(input('请输入一个数字(默认为0):') )
    except ValueError :
        num = 0
    return num


def change(url:str):
    #url = 'https://github.com/cheat/cheat/archive/4.2.0.zip'
    list_url = list(url)                          # 将字符串替换为列表
    list_url.insert(18,'.cnpmjs.org')             # 在指定位置插入对应字符串 
    list_url_02 = list(url)
    list_url_02.insert(8,'gitclone.com/')
    cn_url = "".join(list_url)
    git_clone_url = "".join(list_url_02)
    fastgit = url.replace('github.com','download.fastgit.org')
    wuyan = url.replace('com','wuyanzheshui.workers.dev')
    raw_fastgit = url.replace('githubusercontent.com','fastgit.org')
    raw_sevencdn = url.replace('githubusercontent.com','sevencdn')
    
    chifun = 'https://github.91chifun.workers.dev//'+ url
    ghcon = 'https://gh.con.sh/'+ url
    api_999 = 'https://gh.api.99988866.xyz/' + url 
    xiu = 'https://github.xiu2.xyz/' + url  
    ghproxy = 'https://ghproxy.com/' + url 
    zwc365 = 'https://pd.zwc365.com/seturl/' + url
    
    assect_url = [chifun,ghcon,ghproxy,api_999,xiu,zwc365]
    raw_list =[raw_fastgit,raw_sevencdn]+ assect_url
    url_list = [cn_url,fastgit,wuyan,git_clone_url]+ assect_url
    url_all =(raw_list,url_list)
    #for index,item in enumerate(url_all):
        #print(index,item,end='\n')
    return url_list,raw_list    

    

@app.command()
def clone(url:str ):
    """
    示例:cit clone https://github.com/solider245/cit.git
    """
    cn_url = change(url)[0]
    for index,item in enumerate(cn_url):
        print(index,item)
    
    print(f'为您找到{len(cn_url)}个地址,')
    
    try :
        num =int(input('请输入一个数字（默认为0）: '))
    except ValueError :
        num = 0
        
    
    最终地址 = cn_url[num]    
    git_start = subprocess.call(['git', 'clone',最终地址]) 
    typer.echo(f'下载完毕{git_start}')

@app.command()
def sub(url:str):
    """
    示例:cit sub https://github.com/solider245/cit.git
    """
    cn_url = change(url)[0]
    for index,item in enumerate(cn_url):
        print(index,item)
    
    print(f'为您找到{len(cn_url)}个地址,')
    n = 地址序号()
    git_sub = subprocess.call(['git', 'submodule','add' , cn_url[n]]) 
    typer.echo(f'现在开始为您下载:{git_sub}') 

@app.command()
def get(url:str):
    """ 
    示例:cit get https://github.com/cheat/cheat/archive/4.2.0.zip
    """
    cn_url = change(url)[0]
    for index,item in enumerate(cn_url):
        print(index,item)
    
    print(f'为您找到{len(cn_url)}个地址,')
    n = 地址序号()
    下载地址 = cn_url[n]
    print('下载地址是:',下载地址)
    #下载命令 = subprocess.call(['wget',下载地址])
    file_name = 下载地址.split('/')[-1]
    typer.echo(f"开始下载文件:{file_name}")
    r = requests.get(下载地址,stream=True)
    with tqdm.wrapattr(open(file_name, "wb"), "write", miniters=1,
                total=int(r.headers.get('content-length', 0)),
                desc=file_name) as fout:
        for chunk in r.iter_content(chunk_size=4096):
            fout.write(chunk)
"""     with open(file_name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk) """
if __name__ == "__main__":
    app()




        
    #typer.echo(f'正在执行下载命令:{下载命令}') 

@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")


