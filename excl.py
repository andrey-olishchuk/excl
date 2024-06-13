import click
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader

@click.group()
def cli():
    pass 

@click.command()
@click.argument('folder')
def index(folder):
    loader = DirectoryLoader('./documents', glob="**/*.txt", show_progress=True)
    docs = loader.load()
    for d in docs:
        alldata = d.page_content.split("<<<***")
        click.echo(alldata[0][:20])
        if (len(alldata) > 0):
            click.echo(alldata[1])

@click.command()
def ask():
    click.echo('Searching index')

cli.add_command(index)
cli.add_command(ask)

if __name__ == '__main__':
    cli()
