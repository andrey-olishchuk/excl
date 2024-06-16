import click
import gemini
import qdrant
from langchain_community.document_loaders import DirectoryLoader


@click.group()
def cli():
    pass 

@click.command()
@click.argument('folder')
@click.option('--collection', help='Alternative collection name')
def index(folder, collection):
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
        
        qdrant.add_index(i,vector,link,alldata[0], collection)
        i += 1


@click.command()
@click.option('--question', help='Question to answer')
def ask(question):
    vector = gemini.embed_content(question)
    documents = qdrant.search(vector)
    links = gemini.extract_links(documents)
    answer = gemini.prompt(question, documents)
    click.echo(click.style(answer,fg="green"))
    click.echo(click.style(links,fg="yellow"))

@click.command()
@click.argument('collection')
def kickoff(collection):
    qdrant.kickoff(collection)
    click.echo(f'Kickoff attempt on the collection: {collection}')

cli.add_command(index)
cli.add_command(ask)
cli.add_command(kickoff)

if __name__ == '__main__':
    cli()
