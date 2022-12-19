FROM python:3.9

# Copy the code for your app into the container
COPY requirements.txt /requirements.txt
COPY app.py /app.py
ADD dataset ./

# Install flask and pandas
RUN pip3 install -r requirements.txt

# Run the app when the container starts
CMD ["python", "/app.py"]