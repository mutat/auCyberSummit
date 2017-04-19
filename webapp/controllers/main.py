from flask import (render_template, Blueprint)
from ..forms import SpeakerForm, EventForm
from webapp.models import db, Speaker

main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='../templates/main',
    url_prefix="/"
)


@main_blueprint.route('/')
def home():
    form = SpeakerForm()
    event_form = EventForm()
    event_form.speaker.choices = [(g.id, g.f_name + ' ' + g.l_name) for g in Speaker.query.order_by(Speaker.id)]
    speakers = Speaker.query.order_by(Speaker.id).all()
    return render_template('home.html', form=form, speakers=speakers, event_form=event_form)

