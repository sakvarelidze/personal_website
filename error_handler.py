from saba import *
from config import *

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html")


@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html")
