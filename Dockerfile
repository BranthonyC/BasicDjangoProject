# Use the official Python image as the base image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy the Django project files into the container
COPY . /code/

# EXPOSE 8000

# # # Run the Django development server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
