import csv

import click

from . import app, db
from .models import Opinion


@app.cli.command('load_opnions')
def load_opnions_command():
    with open('opinions.csv', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        counter = 0
        for row in reader:
            opinion = Opinion(**row)
            db.session.add(opinion)
            db.session.commit()
            counter += 1
    click.echo(f'Загружено: {counter}')
