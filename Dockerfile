FROM python:3-slim

# Prepare application environment
RUN mkdir /app
RUN adduser web
ENV FLASK_APP=app.py

WORKDIR /app
RUN chown web:nogroup /app

# Install Python dependencies
COPY --chown=web:nogroup ./requirements.txt /app
RUN pip install -r requirements.txt

# Install application files
COPY --chown=web:nogroup ./ /app

USER web
EXPOSE 3455
CMD ["waittress-serve", "--port", "3455", "--call", "flaskr:create_app"]
