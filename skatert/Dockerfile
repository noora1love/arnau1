FROM python:3.11

# Настроить и активировать виртуальную среду
ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

# Команды Python будут выполнены в виртуальной среде
COPY .. /skatert
RUN pip install --no-cache-dir -r /skatert/requirements.txt

RUN pip install gunicorn
WORKDIR /skatert

ENV DJANGO_SETTINGS_MODULE=skatert.settings
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH /skatert

RUN python manage.py collectstatic --noinput
CMD ["gunicorn", "skatert.wsgi:application", "--bind", "0.0.0.0:8000"]

#EXPOSE 8000