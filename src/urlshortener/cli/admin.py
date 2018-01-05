import click

import urlshortener.application


@click.group()
def cli():
    pass


@cli.group()
def db():
    pass


@db.command()
def create():
    with urlshortener.application.session_scope() as session:
        session.create_all()
    # urlshortener.application.db.create_all()


@db.command()
def drop():
    with urlshortener.application.session_scope() as session:
        session.drop_all()
    # urlshortener.application.db.drop_all()
