import click


@click.group()
@click.pass_context
def link_gopher(self):
    pass


@link_gopher.command()
def command():
    print('OK')


cli = click.CommandCollection(sources=[link_gopher])


if __name__ == '__main__':
    link_gopher()
