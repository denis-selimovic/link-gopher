import click

from link_gopher.cli.validations import validate_input, validate_output
from link_gopher.scraper.base import Scraper


@click.group()
@click.pass_context
def link_gopher(self):
    pass


@link_gopher.command()
@click.option('--browser', '-b', required=True)
@click.option('--src', '-s', required=True)
@click.option('--dst', '-d', required=True)
@click.option('--in', '-i')
@click.option('--out', '-o')
def run(**kwargs):
    print(kwargs)
    try:
        validate_input(kwargs['src'], kwargs.get('in'))
        validate_output(kwargs['dst'], kwargs.get('out'))
    except Exception as e:
        print(e)
        return

    scraper = Scraper(kwargs['browser'], kwargs['src'], kwargs['dst'])
    scraper.load(kwargs.get('in'), kwargs.get('out'))


cli = click.CommandCollection(sources=[link_gopher])


if __name__ == '__main__':
    link_gopher()
