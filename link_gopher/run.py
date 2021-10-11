import click

from link_gopher.browser.factory import BrowserFactory
from link_gopher.cli.validations import validate_input, validate_output
from link_gopher.filters.factory import FilterFactory
from link_gopher.output.factory import OutputFactory
from link_gopher.scraper.base import Scraper
from link_gopher.source.factory import SourceFactory


@click.group()
@click.pass_context
def link_gopher(self):
    pass


@link_gopher.command()
@click.option('--browser', '-b', required=True,
              default='firefox',
              type=click.Choice(BrowserFactory.get_keys()))
@click.option('--src', '-s', required=True, default='mem',
              type=click.Choice(SourceFactory.get_keys()))
@click.option('--dst', '-d', required=True, default='mem',
              type=click.Choice(OutputFactory.get_keys()))
@click.option('--in', '-i')
@click.option('--out', '-o')
@click.option('--filter-type', '-ft',
              type=click.Choice(FilterFactory.get_keys()))
@click.option('--filter-values', '-fv')
def run(**kwargs):
    try:
        validate_input(kwargs['src'], kwargs.get('in'))
        validate_output(kwargs['dst'], kwargs.get('out'))
    except Exception as e:
        print(e)
        return

    scraper = Scraper(kwargs['browser'], kwargs['src'], kwargs['dst'],
                      kwargs['filter_type'],
                      kwargs['filter_values'].split(",")
                      if kwargs['filter_type'] else None)
    scraper.load(kwargs.get('in'), kwargs.get('out'))


cli = click.CommandCollection(sources=[link_gopher])


if __name__ == '__main__':
    link_gopher()
