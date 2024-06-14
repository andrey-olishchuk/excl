import click
import gemini
import qdrant
from langchain_community.document_loaders import DirectoryLoader


@click.group()
def cli():
    pass 

@click.command()
@click.argument('folder')
def index(folder):
    loader = DirectoryLoader(folder, glob="**/*.txt", show_progress=True)
    docs = loader.load()
    i = 1
    for d in docs:
        alldata = d.page_content.split("<<<***")
        vector = gemini.embed_content(alldata[0])

        if (len(alldata) > 0):
            link = alldata[1]
        else:
            link = ""

        click.echo(click.style(alldata[0][:20],fg="green"))
        click.echo(click.style(vector[:5],fg="blue"))
        click.echo(click.style(link,fg="yellow"))
        
        qdrant.add_index(i,vector,link,alldata[0])
        i += 1


@click.command()
def ask():
    click.echo('Searching index')

cli.add_command(index)
cli.add_command(ask)

if __name__ == '__main__':
    cli()
