import logging
import click

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)
# logging.warning('This is a warning message')

#### decoretor
# def logit(func):
#     def weapper():
#         logging.warning('funcation start')
#         func()
#         logging.warning('funcation end')
#     return weapper

# @logit
# def hello():
#     print("I am a hello funcation")


@click.group()
@click.option('--debug/--no-debug', default=False, help='Run command on debug mode')
def cli(debug):
    if debug:
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.WARNING)

    logging.debug('Debug mode is set')

# def logit(func):
#     def weapper():
#         logging.warning('funcation start')
#         func()
#         logging.debug('This is just a debug message')
#         logging.warning('funcation end')
#     return weapper

@cli.command()
def hello():
    logging.warning('funcation start')
    print("I am a hello funcation")
    logging.debug('Debug just for fun')
    logging.warning('funcation end')

if __name__ == '__main__':
    # hello()
    cli()