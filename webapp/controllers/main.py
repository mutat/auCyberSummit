from flask import render_template, Blueprint, flash, redirect, url_for, request
from ..forms import SpeakerForm, EventForm, LoginForm, RegisterForm
from webapp.models import db, Speaker, User
from flask_login import login_user, logout_user, current_user, login_required

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
@login_required
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
    return "Smooth as Tennessee Whiskey"



