from operator import attrgetter


def safe_attrgetter(obj, *attrs, default=None):  # py3 declaration
    """The fail-safe version of attrgetter"""
    v = []
    for attr in attrs:
        try:
            x = attrgetter(attr)(obj)
        except:
            x = default
        v.append(x)
    return v[0] if len(v) == 1 else v


def days_hours_minutes(td):
    """Return total days, remaining hours, remaining
    minutes given timedelta object
    """
    return td.days, td.hours, td.minutes


def duration_from_timedelta(td, only="all"):
    """Return a valid JSON dict of Duration type
    for timedelta object
    """
    days, hours, minutes = days_hours_minutes(td)
    codes = []
    if days > 0:
        codes.append(
            {
                "value": days,
                "unit": "day",
                "system": "http://unitsofmeasure.org",
                "code": "d",
            }
        )
    if hours > 0:
        codes.append(
            {
                "value": hours,
                "unit": "hour",
                "system": "http://unitsofmeasure.org",
                "code": "h",
            }
        )
    if minutes > 0:
        codes.append(
            {
                "value": minutes,
                "unit": "minute",
                "system": "http://unitsofmeasure.org",
                "code": "min",
            }
        )
    return codes


__all__ = ["safe_attrgetter", "days_hours_minutes", "duration_from_timedelta"]
