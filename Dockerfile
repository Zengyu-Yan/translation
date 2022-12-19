FROM python:3.9

# Install flask and pandas
RUN pip install flask
RUN pip install pandas

# Copy the code for your app into the container
COPY app.py /app.py
ADD dataset ./

# Run the app when the container starts
CMD ["python", "/app.py"]