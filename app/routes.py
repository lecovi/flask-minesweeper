"""
    minesweeper.routes
    ~~~~~~~~~~~~~~~~~~~~~~~
    
    Description
    
    :copyright: (c) 2017 by LeCoVi.
    :author: Leandro E. Colombo Viña <colomboleandro at bitson.com.ar>.
    :license: AGPL, see LICENSE for more details.
"""
# Standard lib imports
# Third-party imports
from flask import Blueprint, render_template
# LeCoVi imports

mines = Blueprint('mines', __name__)


@mines.route('/')
def index():
    return render_template('index.html')


@mines.route('/new')
def new_game():
    return render_template('new_game.html')