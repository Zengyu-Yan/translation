FROM python:3.9

# Install Flask and any other dependencies your app needs
RUN pip install Flask
RUN pip install pandas

# Copy the code for your app into the container
COPY app.py /app.py
COPY cleaned_dataset.csv ./

# Run the app when the container starts
CMD ["python", "/app.py"]