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

    
    最终地址 =   cit_url.main(url)
    git_start = subprocess.call(['git', 'clone',最终地址]) 
    

@app.command()
def sub(url:str):
    """
    子模块加速:cit sub <url>
    """
    最终地址 = cit_url.main(url)   
    git_start = subprocess.call(['git', 'submodule','add', 最终地址]) 

@app.command()
def get(url:str):
    """ 
    文件下载:cit get <url>
    """
   
    下载地址 = cit_url.main(url)
    print(f'下载地址是:{下载地址}')
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


