from os import getenv
import datetime

def utility_text_processors():
    message = "Thank you for visiting"

    def deployment_environment():
        return getenv('FLASK_ENV', None)

    def current_year():
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")
        return year

    return dict(
        mymessage=message,
        deployment_environment=deployment_environment(),
        year=current_year(),
    )


