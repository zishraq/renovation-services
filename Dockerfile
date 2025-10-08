FROM python:3.11-slim

# Set environment variables for safety
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install OS dependencies (postgres client + gcc for psycopg2)
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential libpq-dev curl && \
    rm -rf /var/lib/apt/lists/*

# Create a non‑root user
RUN useradd -ms /bin/bash django
WORKDIR /app
COPY --chown=django:django requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the project (excluding .git, __pycache__, etc.)
COPY --chown=django:django . .

# Switch to non‑root user
USER django

# Collect static files at build time (optional – you can also do it at runtime)
RUN python manage.py collectstatic --noinput

# Expose the port gunicorn will listen on
EXPOSE 8000

# Default command
CMD ["gunicorn", "renovation_site.wsgi:application", "--bind", "0.0.0.0:8000"]