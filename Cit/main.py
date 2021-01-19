#!/usr/bin/python
import typer
import subprocess # 导入子模块
#from download import download
#import wget
from Cit import cit_url
import requests
from tqdm.auto import tqdm
CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])



#app = typer.Typer(add_completion=False)
app = typer.Typer(help="从github的下载速度提高一万倍",add_completion=False)

def main(
    name: str = typer.Argument(
        "Wade Wilson", help="Who to greet", show_default="Deadpoolio the amazing's name"
    )
):
    typer.echo(f"Hello {name}")


#@app.command()
def 地址序号():
    try :
        num = int(input('请输入一个数字(默认为0):') )
    except ValueError :
        num = 0
    return num


""" def change(url:str):
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
    raw_list =[raw_fastgit,raw_sevencdn] + assect_url
    url_list = [cn_url,fastgit,wuyan,git_clone_url]+ assect_url
    url_all =(raw_list,url_list)
    #for index,item in enumerate(url_all):
        #print(index,item,end='\n')
    return url_all    """
@app.command()
def change(url:str):
    """ 
    链接转换:cit change <url>
    """
    s = cit_url.main(url)
    


@app.command()
def clone(url:str ):
    """
    git加速:cit clone <url>
    """
    s = cit_url.main(url)
    
    try :
        num =int(input('请输入一个数字,选择你的下载地址（默认为0）: ')) 
    except ValueError :
        num = 0 
        
    
    最终地址 = s[num]    
    git_start = subprocess.call(['git', 'clone',最终地址]) 
    

@app.command()
def sub(url:str):
    """
    子模块加速:cit sub <url>
    """
    s = cit_url.main(url)
    
    try :
        num =int(input('请输入一个数字,选择你的下载地址（默认为0）: ')) 
    except ValueError :
        num = 0 
        
    
    最终地址 = s[num]    
    git_start = subprocess.call(['git', 'submodule','add', 最终地址]) 

@app.command()
def get(url:str):
    """ 
    文件下载:cit get <url>
    """
    s = cit_url.main(url)
    n = 地址序号()
    下载地址 = s[n]
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

if __name__ == "__main__":
    app()




        
    #typer.echo(f'正在执行下载命令:{下载命令}') 

""" @app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!") """


