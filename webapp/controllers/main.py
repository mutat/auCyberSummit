from flask import render_template, Blueprint, flash, redirect, url_for, request
from ..forms import SpeakerForm, EventForm, LoginForm, RegisterForm
from webapp.models import db, Speaker, User, EventSession
from flask_login import login_user, logout_user, current_user, login_required
from sqlalchemy import text

main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='../templates/main',
    url_prefix="/"

)


@main_blueprint.route('/')
def home():
    events = EventSession.query.join(Speaker).add_columns(Speaker.f_name, Speaker.l_name, Speaker.employer, Speaker.image).order_by(
        EventSession.time).all()
    return render_template('home.html', events=events)


@main_blueprint.route('login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash("You have been logged in.", category="success")
            return redirect(request.args.get('next') or url_for('.home'))
        flash("Invalid username or password", category="danger")

    return render_template('main/login.html', form=form)


@main_blueprint.route('logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash("You have been logged out.", category="success")
    return redirect(url_for('.home'))


@main_blueprint.route('__geek', methods=['GET', 'POST'])
#@login_required
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        new_user = User()
        new_user.name = form.name.data
        new_user.username = form.username.data
        new_user.set_password(form.password.data)

        db.session.add(new_user)
        db.session.commit()

        flash(new_user.name + " has been created, please login.", category="success")
        return redirect(url_for('.login'))

    return render_template('main/register.html', form=form)


@main_blueprint.route('thingamajig')
def thingamajig():
    sql = text('SELECT event_session.id, event_session.speaker_id, event_session.description, event_session.title, speaker.f_name FROM public.event_session INNER JOIN speaker ON event_session.speaker_id=speaker.id;')
    events = "[" + '\n'
    result = db.engine.execute(sql)
    for row in result:
        id = '"id":'+str(row[0])
        speaker_id = '"speaker_id":'+str(row[1])
        description = '"description":'+'"'+row[2]+'"'
        title = '"title":'+'"'+row[3]+'"'
        f_name = '"f_name":'+'"'+row[4]+'"'
        ans = id+'\n'+speaker_id+'\n'+description+'\n'+title+'\n'+f_name+'\n'
        events += ans

    events += "]"
    return events



