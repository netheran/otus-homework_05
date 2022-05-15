from flask import (
    Blueprint,
    render_template,
)
from homework_05.views.endpoints import ENDPOINTS

webapp = Blueprint("webapp", __name__)


@webapp.get("/", endpoint=ENDPOINTS.get("Index"))
def index_view():
    return render_template("app/index.html", endpoints=ENDPOINTS)


@webapp.get("/about/", endpoint=ENDPOINTS.get("About"))
def show_about():
    return render_template("app/about.html")

