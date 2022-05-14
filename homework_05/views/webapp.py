from flask import (
    Blueprint,
    render_template,
)
from views.endpoints import ENDPOINTS as endpoints

webapp = Blueprint("webapp", __name__)


@webapp.get("/", endpoint=endpoints.get("Index"))
def index_view():
    return render_template("app/index.html")


@webapp.get("/about/", endpoint=endpoints.get("About"))
def show_about():
    return render_template("app/about.html")

