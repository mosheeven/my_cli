#!/usr/bin/env python3
import click

@click.command()
@click.option('--name', prompt='Your name',help='The person to greet.')
@click.option
def hello(name):
    click.echo('Hello ' + name)

if __name__ == '__main__':
    hello()