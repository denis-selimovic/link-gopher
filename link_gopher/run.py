import click

from link_gopher.scraper.base import Scraper


@click.group()
@click.pass_context
def link_gopher(self):
    pass


@link_gopher.command()
@click.option('--browser', required=True)
@click.option('--input', required=True)
@click.option('--output', required=True)
def run(**kwargs):
    scraper = Scraper(kwargs['browser'], 'txt', 'txt')
    scraper.load(kwargs['input'], kwargs['output'])


cli = click.CommandCollection(sources=[link_gopher])


if __name__ == '__main__':
    link_gopher()
