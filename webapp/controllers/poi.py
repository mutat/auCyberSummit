from flask import render_template, Blueprint, url_for, redirect, flash
from webapp.models import db, Poi
from ..forms import PoiForm
from flask_login import login_required


poi_blueprint = Blueprint(
    'poi',
    __name__,
    template_folder='../templates/poi',
    url_prefix='/poi'
)


@poi_blueprint.route('/')
def poi_home():
    points = Poi.query.all()
    return render_template('poi/home.html', points=points)


@poi_blueprint.route('/new', methods=['GET', 'POST'])
@login_required
def poi_new():
    form = PoiForm()

    if form.validate_on_submit():
        point = Poi()
        point.name = form.name.data
        point.addr1 = form.addr1.data
        point.city = form.city.data
        point.state = form.state.data
        point.zip = form.zip.data
        point.description = form.description.data

        db.session.add(point)
        db.session.commit()

        flash(point.name + "added to Points of Interest", category="success")

        return redirect(url_for('.poi_new'))
    return render_template('poi/new.html',form=form)


@poi_blueprint.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def poi_edit(id):
    form = PoiForm()
    point = Poi.query.get_or_404(id)

    if form.validate_on_submit():
        point.name = form.name.data
        point.addr1 = form.addr1.data
        point.city = form.city.data
        point.state = form.state.data
        point.zip = form.zip.data
        point.description = form.description.data

        db.session.add(point)
        db.session.commit()

        flash('Updated ' + point.name, category="success")

        return redirect(url_for('poi.poi_home'))

    #set the form data
    form.name.data = point.name
    form.addr1.data = point.addr1
    form.city.data = point.city
    form.state.data = point.state
    form.zip.data = point.zip
    form.description.data = point.description

    return render_template('poi/edit.html', form=form)
