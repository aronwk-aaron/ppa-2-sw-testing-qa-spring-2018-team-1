import logging
from flask import Flask, render_template, redirect, url_for, request, Blueprint

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def index():
    return render_template('index.html')


@main_blueprint.route('/bmi', methods=['GET', 'POST'])
def bmi():
    if request.method == 'POST':
        return 'Hello, bmi post!'
    else:
        return 'Hello, bmi!'


@main_blueprint.route('/distance', methods=['GET', 'POST'])
def distance():
    if request.method == 'POST':
        return 'Hello, distance post!'
    else:
        return 'Hello, distance!'


@main_blueprint.route('/email', methods=['GET', 'POST'])
def email():
    if request.method == 'POST':
        return 'Hello, email post!'
    else:
        return 'Hello, email!'


@main_blueprint.route('/retirement', methods=['GET', 'POST'])
def retirement():
    if request.method == 'POST':
        return 'Hello, retirement post!'
    else:
        return 'Hello, retirement!'


@main_blueprint.route('/tip', methods=['GET', 'POST'])
def tip():
    if request.method == 'POST':
        return 'Hello, tip post!'
    else:
        return 'Hello, tip!'


@main_blueprint.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))


@main_blueprint.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('Someone tried to do somehting they were not supposed to do!.')
    return render_template('index.html')
