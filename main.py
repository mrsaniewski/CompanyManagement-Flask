from flask import Flask, redirect, url_for, request, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

# app = Flask(__name__)
#
# @app.route("/")
# def home():
#     return "Hello! this is the main page <h1>HELLO<h1>"
#
# @app.route("/<name>")
# def user(name):
#     return f"Hello {name}!"
#
# @app.route("/admin")
# def admin():
#     return redirect(url_for("home"))
#
# if __name__ =="__main__":
#     app.run()
from website import create_app, db
from website.models import User, Task, Prize


app = create_app()

admin = Admin(app)
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Task, db.session))
admin.add_view(ModelView(Prize, db.session))


if __name__ == '__main__':

    app.run(debug=True)

