from flask import render_template, Blueprint, url_for, redirect, flash
from webapp.models import db, Speaker
from ..forms import SpeakerForm
from flask_login import login_required


speaker_blueprint = Blueprint(
    'speaker',
    __name__,
    template_folder='../templates/speaker',
    url_prefix="/speaker"
)


@speaker_blueprint.route('/')
def home():
    speakers = Speaker.query.order_by(Speaker.id).all()
    return render_template('speaker/home.html', speakers=speakers)


@speaker_blueprint.route('/new', methods=['GET', 'POST'])
@login_required
def new_speaker():
    form = SpeakerForm()

    if form.validate_on_submit():
        speaker = Speaker()
        speaker.f_name = form.f_name.data
        speaker.l_name = form.l_name.data
        speaker.image = form.image.data
        speaker.employer = form.employer.data
        speaker.bio = form.bio.data

        db.session.add(speaker)
        db.session.commit()

        flash("Successfully added " + speaker.f_name + ' ' + speaker.l_name, category="success")

        return redirect(url_for('.new_speaker'))
    return render_template('speaker/new.html', form=form)


@speaker_blueprint.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_speaker(id):
    speaker = Speaker.query.get_or_404(id)
    form = SpeakerForm()

    if form.validate_on_submit():
        speaker.f_name = form.f_name.data
        speaker.l_name = form.l_name.data
        speaker.image = form.image.data
        speaker.employer = form.employer.data
        speaker.bio = form.bio.data

        db.session.add(speaker)
        db.session.commit()

        flash("Updated " + speaker.f_name + ' ' + speaker.l_name, category="success")

        return redirect('speaker/')

    form.f_name.data = speaker.f_name
    form.l_name.data = speaker.l_name
    form.image.data = speaker.image
    form.employer.data = speaker.employer
    form.bio.data = speaker.bio

    return render_template('edit.html', form=form, speaker=speaker)


@speaker_blueprint.route('/info/<int:id>')
def detail_speaker(id):
    speaker = Speaker.query.get_or_404(id)
    return render_template('detail.html', speaker=speaker)





