import click


@click.group()
@click.option('--debug/--no-debug', default=False, help='Run command on debug mode')
@click.pass_context
def kancli(ctx, debug):
    # click.echo('Debug mode is %s' % ('on' if debug else 'off'))
    ctx.obj['DEBUG'] = debug

@kancli.command()
@click.pass_context
def get_instances(ctx):
    click.echo('get instances')
    click.echo('Debug mode is %s' % ('on' if ctx.obj['DEBUG'] else 'off'))

@kancli.command()
@click.pass_context
def stop_instances(ctx):
    if click.confirm('Are you sure you want to stop instanes?'):
        click.echo('Bye bye instance')

if __name__ == '__main__':
    kancli(obj={})