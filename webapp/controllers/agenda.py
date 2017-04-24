from flask import render_template, Blueprint, url_for, redirect, flash
from webapp.models import db, EventSession, Speaker
from ..forms import EventForm
from flask_login import login_required


event_blueprint = Blueprint(
    'event',
    __name__,
    template_folder='../templates/event',
    url_prefix='/event'
)

@event_blueprint.route('/')
def event_home():
    events = EventSession.query.join(Speaker).add_columns(Speaker.f_name, Speaker.l_name).order_by(EventSession.time).all()
    return render_template('event/home.html', events=events)


@event_blueprint.route('/new', methods=['GET', 'POST'])
@login_required
def new_event():
    form = EventForm()
    form.speaker.choices = [(g.id, g.f_name + ' ' + g.l_name) for g in Speaker.query.order_by(Speaker.id)]

    if form.validate_on_submit():
        event = EventSession()
        event.title = form.title.data
        event.time = form.time.data
        event.speaker_id = form.speaker.data
        event.description = form.description.data

        db.session.add(event)
        db.session.commit()

        flash("Successfully add " + event.title, category="success")

        return redirect(url_for('.new_event'))

    return render_template('event/new.html', form=form)


@event_blueprint.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_event(id):
    form = EventForm()
    event = EventSession.query.get_or_404(id)
    form.speaker.choices = [(g.id, g.f_name + ' ' + g.l_name) for g in Speaker.query.order_by(Speaker.id)]

    if form.validate_on_submit():
        event.title = form.title.data
        event.time = form.time.data
        event.speaker_id = form.speaker.data
        event.description = form.description.data

        db.session.add(event)
        db.session.commit()

        flash('Updated' + event.title, category="success")

        return redirect(url_for('event.event_home'))

    form.title.data = event.title
    form.time.data = event.time
    form.speaker.data = event.speaker_id
    form.description.data = event.description

    return render_template('event/edit.html', form=form)

@event_blueprint.route('/info/<int:id>')
def detail_event(id):
    event = EventSession.query.get_or_404(id)
    speaker = Speaker.query.get_or_404(event.speaker_id)

    return render_template('event/detail.html', event=event, speaker=speaker)