import click

from link_gopher.output.factory import OutputFactory
from link_gopher.source.factory import SourceFactory


def validate_output(value, out):
    output = OutputFactory.get(value, None)

    if not output.is_valid(out):
        raise click.BadParameter(
            f'Unknown destination for output type {value}')

    return value


def validate_input(value, inpt):
    input = SourceFactory.get(value)

    if not input.is_valid(inpt):
        raise click.BadParameter(
            f'Unknown source for input type {value}')

    return value
