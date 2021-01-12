import typer
import subprocess # 导入子模块

app = typer.Typer()
@app.command()
def change(url:str):
    
    list_url = list(url)                          # 将字符串替换为列表
    list_url.insert(18,'.cnpmjs.org')             # 在指定位置插入对应字符串
    cn_url = "".join(list_url) 
    typer.echo(f'{cn_url}是替换后的网址,')
    return cn_url
    
    

@app.command()
def clone(url:str):

    cn_url = change(url)
    git_start = subprocess.call(['git', 'clone',cn_url]) 
    typer.echo(f'现在开始为您下载:{git_start}')


@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")


