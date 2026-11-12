from datetime import datetime, timedelta, timezone
from typing import Final, NamedTuple

from flask import Flask, render_template

app = Flask(__name__)

RECENCY_THRESHOLD: Final[timedelta] = timedelta(days=30)


class LiberaryInfo(NamedTuple):
    now: datetime
    start: datetime
    end: datetime
    day: int | None
    this_years: datetime
    time_until: timedelta
    recently_ended: bool

    @staticmethod
    def for_year(year: int) -> datetime:
        return datetime(year, 3, 17, 0, 0, 0, tzinfo=timezone.utc)

    @staticmethod
    def get(ref_now: datetime | None = None) -> LiberaryInfo:
        now = datetime.now(tz=timezone.utc) if ref_now is None else ref_now
        this_years = LiberaryInfo.for_year(now.year)
        this_years_end = this_years + timedelta(days=47)

        if this_years > now:
            # hasn't happened yet
            # this year's Liberary is also the upcoming one
            start = this_years
        else:
            # already passed, get next year's
            start = LiberaryInfo.for_year(now.year + 1)

        time_until = start - now

        # the "end time" within the anomalous period
        # and the "day of the month" of Liberary
        end = start + timedelta(days=47)

        if this_years < now < this_years_end:
            day = (now - this_years).days + 1
        else:
            day = None

        # determine if it "recently ended", meaning, outside of
        # the anomalous period, it's been within this period since the start/end
        recently_ended = start > now > start + RECENCY_THRESHOLD

        return LiberaryInfo(
            now=now,
            start=start,
            end=end,
            day=day,
            this_years=this_years,
            time_until=time_until,
            recently_ended=recently_ended,
        )


@app.route("/")
def liberary_countdown():
    liberary = LiberaryInfo.get()
    return render_template(
        "countdown.html",
        info=liberary,
        days=liberary.time_until.days,
    )


@app.route("/liberary")
def liberary_day_off():
    # hidden route that pretends it's presently Liberary,
    # and returns the equivalent date in SCP-3455
    # otherwise, returns the normal timer

    liberary = LiberaryInfo.get()

    if liberary.day is None:
        # not in the time period
        return liberary_countdown()

    return render_template(
        "inside.html",
        info=liberary,
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/scp")
def scp_redirect():
    return app.redirect("https://scpwiki.com/scp-3455")
