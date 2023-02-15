from asyncio import Task

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Task, User, Prize
from . import db
import json

views = Blueprint('views', __name__)


@views.route('', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        task = request.form.get('task')
        title = request.form.get('title')

        if len(task) < 1:
            flash('Task is too short!', category='error')
        else:
            new_task = Task(data=task, title=title, user_id=current_user.id)
            db.session.add(new_task)
            db.session.commit()
            flash('Task added!', category='success')

    return render_template("home.html", user=current_user)


@views.route("/about")
def about():
    return render_template("about.html", user=current_user)


@views.route("/loyalty", methods=['GET', 'POST'])
@login_required
def loyalty():
    return render_template("loyalty.html", user=current_user, prize=Prize)


@views.route('/delete-task', methods=['POST'])
def delete_task():
    task = json.loads(request.data)
    taskId = task['taskId']
    task = Task.query.get(taskId)
    if task:
        if task.user_id == current_user.id:
            db.session.delete(task)
            db.session.commit()
            flash('Task deleted!', category='message')

    return jsonify({})


@views.route('/done-task', methods=['GET', 'POST'])
def done_task():
    task = json.loads(request.data)
    taskId = task['taskId']
    task = Task.query.get(taskId)
    if task:
        if task.user_id == current_user.id:
            db.session.delete(task)
            current_user.points = current_user.points + 10
            db.session.commit()
    flash('Points added !', category='message')

    return jsonify({})


@views.route('/done-prize', methods=['GET', 'POST'])
def done_prize():
    prize = json.loads(request.data)
    prizeId = prize['prizeId']
    prize = Prize.query.get(prizeId)
    if prize:
        if prize.user_id == current_user.id:
            db.session.delete(prize)
            current_user.points = current_user.points - 20
            db.session.commit()
    flash('Points deducted !', category='message')

    return jsonify({})
