**TITLE : GENERATION OF HAND - WRITING FROM TEXT BY USING GENERATIVE ADVERSARIAL NETWORKS**

This repository contains a Python Flask application for converting text files into handwritten PDFs. The application takes a text file as input, converts the text into handwritten format, and generates a PDF document containing the handwritten text. The application simulates handwritten text by generating images of handwritten characters and combining them into a PDF document and in a PNG file.
A GAN is a type of neural network architecture used for generating new data samples that are similar to a given dataset. GANs are commonly used in various applications, including image generation, style transfer, and data augmentation. They consist of two neural networks, the generator and the discriminator, which are trained together in a competitive manner.

**INTRODUCTION**

The project consists of a web application built using Flask, a Python web framework, along with some PyQt5 code for a graphical user interface (GUI) window. The application's main functionality is to convert text input into handwritten-style images and then combine these images into a PDF file. Let's break down the components and functionality of the code:

--Flask Web Application (app.py):--
This part of the code defines a Flask web application responsible for serving HTML templates and handling HTTP requests.
It provides two routes:
/: The root route renders an HTML template (index.html) containing a form to upload a text file.
/generate: This route handles the POST request sent when the form is submitted. It reads the uploaded text file, processes it to generate handwritten-style images, combines these images into a PDF file, and then serves the PDF file for download.

--Text to Handwriting Functionality (worddd and generate_pdf_text functions):--
The worddd function is responsible for converting input text into a series of images resembling handwritten text. It splits the input text into words and processes each word to generate handwritten-style images.
The generate_pdf_text function takes the processed text and converts it into a PDF file. It generates images for each word using the worddd function, combines these images into a PDF file using the FPDF library, and saves the PDF file.

--PyQt5 GUI (Window class):--
The PyQt5 code defines a GUI window (Window class) with buttons for various actions related to managing student records.
It includes functionality to add student details, search for student records using their roll number, and delete student records.
The GUI also includes dialogs for entering roll numbers to search for student records and delete records.

--SQLite Database Handling (DBHelper class):--
There's a SQLite database helper class (DBHelper) responsible for managing student records.
It includes methods to add student records, search for student records by roll number, and delete student records.

--HTML Template (index.html):--
The HTML template provides a simple user interface with a form to upload a text file.
Overall, the application combines Flask for the web interface, PyQt5 for the GUI, and Python libraries like PIL (Python Imaging Library) and FPDF for text-to-image and PDF generation functionalities, respectively. It demonstrates a combination of web development, GUI programming, and file manipulation in Python

**REQUIREMENTS**

Here are the main requirements and their usage:

Flask: Flask is a web framework for Python. It is used to create web applications, APIs, and other web services. In this code, Flask is used to create a web application that allows users to upload a text file and generate a PDF file containing handwritten-style text based on the content of the uploaded file. Flask is used to define routes (@app.route decorators), handle file uploads (request.files), render HTML templates (render_template), and serve the generated PDF file (send_file).

PIL (Python Imaging Library): PIL is a library for image processing tasks in Python. In this code, PIL is used to manipulate images, specifically to generate handwritten-style text images based on the input text. Functions from PIL are used to open background images, paste characters onto the background, and save the resulting images.

fpdf: fpdf is a library for generating PDF files in Python. In this code, fpdf is used to create a PDF document and add pages containing handwritten-style text images generated using PIL. The FPDF class is instantiated to create a PDF object, pages are added using the add_page method, and images are inserted onto the pages using the image method.

PyQt5: PyQt5 is a set of Python bindings for the Qt application framework. It allows Python programmers to create GUI applications. In this code, PyQt5 is used to create a GUI window for entering and searching student records in a database. PyQt5 classes such as QMainWindow, QDialog, QPushButton, QLabel, QLineEdit, QComboBox, QTableWidget, and layout managers like QGridLayout and QVBoxLayout are used to design and layout the GUI components.

SQLite3: SQLite3 is a lightweight, serverless database engine that is included as part of the Python standard library. In this code, SQLite3 is used to create and interact with a simple relational database (sdms.db) for storing student and faculty records. The sqlite3 module is used to connect to the database, execute SQL queries, and manipulate data.
