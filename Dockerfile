FROM python:3-slim

RUN mkdir /app
RUN adduser web
ENV FLASK_APP=app.py

WORKDIR /app
RUN chown web:nogroup /app
COPY --chown=web:nogroup ./ /app
RUN pip install -r requirements.txt

USER web
EXPOSE 3455
CMD ["waittress-serve", "--port", "3455", "--call", "flaskr:create_app"]
