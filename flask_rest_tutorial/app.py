from flask import render_template
from models import Person
from build_database import init_db
from pathlib import Path

import config

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")


@app.route("/")
def home():
    people = Person.query.all()
    return render_template("home.html", people=people)


if __name__ == "__main__":
    if not Path(config.basedir / "people.db").is_file():
        init_db()

    app.run(host="0.0.0.0", port=8000, debug=True)
