from random import randrange

from flask import render_template, redirect, abort, flash, url_for

from . import app, db
from .models import Opinion
from .forms import OpinionForm


@app.route('/')
def index_view():
    quantity = Opinion.query.count()
    if not quantity:
        return abort(500)
    offset_value = randrange(quantity)
    opinion = Opinion.query.offset(offset_value).first()
    return render_template('opinion.html', opinion=opinion)


@app.route('/opinions/<int:id>')
def opinion_view(id: int):
    opinion = Opinion.query.get_or_404(id)
    return render_template('opinion.html', opinion=opinion)


@app.route('/add', methods=['GET', 'POST'])
def add_opinion_view():
    form = OpinionForm()
    text = form.text.data
    if Opinion.query.filter_by(text=text).first() is not None:
        flash(
            'Такое мнение уже было оставлено ранее!', 'free-message'
        )
        return render_template('add_opinion.html', form=form)
    if form.validate_on_submit():
        opinion = Opinion(
            title=form.title.data,
            text=text,
            source=form.source.data
        )
        db.session.add(opinion)
        db.session.commit()
        return redirect(url_for('opinion_view', id=opinion.id))
    return render_template('add_opinion.html', form=form)
