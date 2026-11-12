from datetime import date, datetime, timezone

from flask import Flask

app = Flask(__name__)


def liberary_start(year: int) -> datetime:
    return datetime(year, 3, 17, 0, 0, 0, tzinfo=timezone.utc)


def next_liberary_start() -> datetime:
    now = datetime.now(tz=timezone.utc)
    liberary = liberary_start(now.year)
    if liberary < now:
        # it already passed
        return liberary_start(now.year + 1)

    # it hasn't happened yet
    return liberary


@app.route("/")
def liberary_countdown():
    raise NotImplementedError


@app.route("/liberary")
def liberary_day_off():
    # hidden route that pretends it's presently Liberary,
    # and returns the equivalent date in SCP-3455
    # otherwise, returns the normal timer

    raise NotImplementedError


@app.route("/scp")
def scp_redirect():
    return app.redirect("https://scpwiki.com/scp-3455")
