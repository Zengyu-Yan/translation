# Multilingo

Multilingo is a language learning platform. In this repository, we will integrate a feature on the app in which students can practice translation skills by studying 10 translations a day. The dataset we have is 100 sets of parallel sentences for this task which is scrapped 
from a website.


## Task 1 - Data Processing

The data is firstly processed in order to be suitable for reading by the students. The processing step is in "data processing.ipynb". The prcocessed data is saved as "cleaned_dataset.csv".

## Task 2 - Writing a Flask-based API

The next step is to writ a Flask-based API which returns 10 translation pairs from the dataset. The code is in "app.py". I put everything into a docker container. You can find it in the package named "translation" in this page, or directly copy the following command to your local terminal and download the image.

```
docker pull ghcr.io/zengyu-yan/translation:main
```

After downloading the image, execute the code below to run the app:

```
docker run -d -p 5000:5000 ghcr.io/zengyu-yan/translation:main
```

Now you should be able to access the app page. To get the status of the API, access: http://localhost:5000/api/v1/status. To get the 10 translation pairs, access http://localhost:5000/api/v1/sentences. You can also directly get the status and sentences from the terminal using:

```
curl -X GET http://localhost:5000/api/v1/status
curl -X GET http://localhost:5000/api/v1/sentences
```

The app is also able to return 10 sentences starting from arbitary index, so that students can learn translation pairs from where they left last time. For example, instead of the first 10 sentences, you want to choose the 10th to 20th sentence pairs, you can add "?index=10" to the website: http://localhost:5000/api/v1/sentences?index=10, or simply run:


```
curl http://localhost:5000/api/v1/sentences\?index\=10
```

## Task 3 - Report

I conduct an intial research on Optical Character Recognition (OCR) and the report is in file "Initial Research on Optical Character Recognition.docx"
