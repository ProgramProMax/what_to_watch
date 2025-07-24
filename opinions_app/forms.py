from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, URLField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

REQUIRED_MSG = 'Обязательное поле'


class OpinionForm(FlaskForm):
    title = StringField(
        'Введите название фильма',
        validators=(
            DataRequired(message=REQUIRED_MSG),
            Length(1, 128)
        )
    )
    text = TextAreaField(
        'Напишите мнение',
        validators=(
            DataRequired(message=REQUIRED_MSG),
        )
    )
    source = URLField(
        'Добавьте ссылку на подробный обзор фильма',
        validators=(
            Length(1, 126), Optional()
        )
    )
    submit = SubmitField('Добавить')
