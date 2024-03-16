<h1 align="center" style="border-bottom: none">
    <b>
        <a href="https://www.google.com"> GENERATION OF HAND - WRITING FROM TEXT BY USING GENERATIVE ADVERSARIAL NETWORKS </a><br>
    </b>
    ⭐️ Text to Hand - Writing  ⭐️ <br>
</h1>

This repository contains a Python Flask application for converting text files into handwritten PDFs. The application takes a text file as input, converts the text into handwritten format, and generates a PDF document containing the handwritten text. The application simulates handwritten text by generating images of handwritten characters and combining them into a PDF document and in a PNG file.
A GAN is a type of neural network architecture used for generating new data samples that are similar to a given dataset. GANs are commonly used in various applications, including image generation, style transfer, and data augmentation. They consist of two neural networks, the generator and the discriminator, which are trained together in a competitive manner.

## TEAM DETAILS
`Team number` : VH083

|           Name           |         Email         |
|--------------------------|-----------------------|
| PATHAN MOHAMMAD ASIF     | 99210041705@klu.ac.in |
| PEETA ANJANA SREE        | 9921004816@klu.ac.in  |
| BHAVANAM POOJITHA        | 9921004090@klu.ac.in  |
| BORRA LAKSHMI NRUSIMHA   | 99210042132@klu.ac.in |

## PROBLEM STATEMENT
The problem statement is the need to efficiently generate handwritten-style text from input text files and produce PDF documents containing this handwritten-style text. This is particularly useful in scenarios where users want to add a personalized or creative touch to their documents, such as handwritten letters, notes, or invitations.

Severity of the Problem:
The severity of this problem can vary depending on the context. In certain situations, such as sending personalized letters or invitations, the ability to incorporate handwritten-style text can significantly enhance the emotional impact and personalization of the communication. In educational settings, generating handwritten-style text for worksheets or learning materials can make them more engaging for students. Therefore, while the problem may not be critical in all contexts, it can greatly enhance user experience and effectiveness in specific scenarios.

Need for a Solution:
The need for a solution arises from the limitations of traditional text processing and document generation methods. Standard fonts lack the personal touch and authenticity of handwritten text, which may be desired for various purposes, including communication, marketing, education, and creative expression. Additionally, manually writing or scanning handwritten text is time-consuming and may not be feasible for large-scale document production. Therefore, an automated solution for generating handwritten-style text from input text files and incorporating it into PDF documents can streamline the process, save time, and improve the overall quality and appeal of the output.

Group of People Facing the Problem:
The group of people facing this problem includes individuals and organizations across various domains who require personalized or creative document generation capabilities. This may include:

**1. Individuals:** Individuals who want to create handwritten-style letters, invitations, or notes for personal or professional purposes.

**2.Businesses:** Businesses looking to personalize marketing materials, such as advertisements, brochures, or greeting cards, to better connect with customers.

**3.Educators:** Educators who want to create engaging learning materials, such as worksheets, quizzes, or lesson plans, with handwritten-style text to capture students' attention.

**4.Designers:** Graphic designers and artists who seek to incorporate handwritten elements into their designs for aesthetic appeal or branding purposes.

**5.Event Planners:** Event planners who need to create customized invitations, menus, or signage with handwritten-style text to set the tone for their events.


## ABOUT THE PROJECT

The provided project offers several key details and features to effectively solve the problem of generating handwritten-style text from input text files and incorporating it into PDF documents. Here are some notable aspects:

- Handwriting Style Generation: The project utilizes deep learning techniques, likely including Generative Adversarial Networks (GANs), to generate handwritten-style text from input text files. This allows users to input plain text and obtain output text with a handwritten appearance, mimicking the natural variability and imperfections typically found in human handwriting.

- Customization Options: Users may have the option to customize various aspects of the handwritten-style text generation process, such as the style, size, and alignment of the text. This flexibility enables users to tailor the output to their specific preferences and requirements, whether they desire a formal, casual, or artistic handwriting style.

- PDF Document Generation: Once the handwritten-style text is generated, the project facilitates the integration of this text into PDF documents. Users can specify the layout, formatting, and additional content of the PDF documents, allowing for the creation of personalized letters, notes, invitations, worksheets, or other types of documents.

- Batch Processing: The project may support batch processing capabilities, enabling users to generate handwritten-style text and create multiple PDF documents in a single operation. This feature is particularly useful for scenarios where users need to process large volumes of text or produce multiple documents concurrently.

- Scalability and Performance: The underlying algorithms and technologies used in the project are designed for scalability and performance, allowing for efficient processing of text data and rapid generation of handwritten-style text and PDF documents. This ensures that users can achieve their desired outcomes quickly and reliably, even when working with large datasets or complex document structures.

- User-Friendly Interface: The project likely includes a user-friendly interface that simplifies the process of inputting text, customizing settings, and generating PDF documents with handwritten-style text. Intuitive controls, visual previews, and helpful prompts may be provided to guide users through each step of the process, regardless of their level of technical expertise.

By combining these features, the project offers a comprehensive solution to the problem of generating handwritten-style text and incorporating it into PDF documents. It empowers users to add a personal and creative touch to their communications and materials, enhancing their effectiveness and appeal across various contexts and applications.

**INTRODUCTION**

The project consists of a web application built using Flask, a Python web framework, along with some PyQt5 code for a graphical user interface (GUI) window. The application's main functionality is to convert text input into handwritten-style images and then combine these images into a PDF file. Let's break down the components and functionality of the code:

- Flask Web Application (app.py):
This part of the code defines a Flask web application responsible for serving HTML templates and handling HTTP requests.
It provides two routes:
/: The root route renders an HTML template (index.html) containing a form to upload a text file.
/generate: This route handles the POST request sent when the form is submitted. It reads the uploaded text file, processes it to generate handwritten-style images, combines these images into a PDF file, and then serves the PDF file for download.

- Text to Handwriting Functionality (worddd and generate_pdf_text functions):
The worddd function is responsible for converting input text into a series of images resembling handwritten text. It splits the input text into words and processes each word to generate handwritten-style images.
The generate_pdf_text function takes the processed text and converts it into a PDF file. It generates images for each word using the worddd function, combines these images into a PDF file using the FPDF library, and saves the PDF file.

- PyQt5 GUI (Window class):
The PyQt5 code defines a GUI window (Window class) with buttons for various actions related to managing student records.
It includes functionality to add student details, search for student records using their roll number, and delete student records.
The GUI also includes dialogs for entering roll numbers to search for student records and delete records.

- SQLite Database Handling (DBHelper class):
There's a SQLite database helper class (DBHelper) responsible for managing student records.
It includes methods to add student records, search for student records by roll number, and delete student records.

- HTML Template (index.html):
The HTML template provides a simple user interface with a form to upload a text file.
Overall, the application combines Flask for the web interface, PyQt5 for the GUI, and Python libraries like PIL (Python Imaging Library) and FPDF for text-to-image and PDF generation functionalities, respectively. It demonstrates a combination of web development, GUI programming, and file manipulation in Python

**REQUIREMENTS**

Here are the main requirements and their usage:

- Flask: Flask is a web framework for Python. It is used to create web applications, APIs, and other web services. In this code, Flask is used to create a web application that allows users to upload a text file and generate a PDF file containing handwritten-style text based on the content of the uploaded file. Flask is used to define routes (@app.route decorators), handle file uploads (request.files), render HTML templates (render_template), and serve the generated PDF file (send_file).

- PIL (Python Imaging Library): PIL is a library for image processing tasks in Python. In this code, PIL is used to manipulate images, specifically to generate handwritten-style text images based on the input text. Functions from PIL are used to open background images, paste characters onto the background, and save the resulting images.

- fpdf: fpdf is a library for generating PDF files in Python. In this code, fpdf is used to create a PDF document and add pages containing handwritten-style text images generated using PIL. The FPDF class is instantiated to create a PDF object, pages are added using the add_page method, and images are inserted onto the pages using the image method.

- PyQt5: PyQt5 is a set of Python bindings for the Qt application framework. It allows Python programmers to create GUI applications. In this code, PyQt5 is used to create a GUI window for entering and searching student records in a database. PyQt5 classes such as QMainWindow, QDialog, QPushButton, QLabel, QLineEdit, QComboBox, QTableWidget, and layout managers like QGridLayout and QVBoxLayout are used to design and layout the GUI components.

- SQLite3: SQLite3 is a lightweight, serverless database engine that is included as part of the Python standard library. In this code, SQLite3 is used to create and interact with a simple relational database (sdms.db) for storing student and faculty records. The sqlite3 module is used to connect to the database, execute SQL queries, and manipulate data.

## TECHNICAL IMPLEMENTATION

The technical implementation of the project involves several key steps, including data preprocessing, model training, PDF generation, and integration into a web application. Below is a high-level overview of how each component may be implemented:

**Data Preprocessing:**

- The project begins with collecting a dataset of handwritten text samples, preferably in a digitized format. This dataset may include various styles of handwriting to increase diversity.
- The text data is preprocessed to extract individual characters or words, remove noise, and standardize the format.
- Additionally, if the project aims to generate handwriting based on specific input text data, such as user input or extracted from PDF documents, preprocessing techniques such as tokenization and embedding may be applied.

**Model Training:**

- Deep learning models, such as Generative Adversarial Networks (GANs) or Recurrent Neural Networks (RNNs), are trained on the preprocessed dataset.
- For GAN-based approaches, the generator network learns to generate handwritten-style text given random noise or input text data, while the discriminator network learns to distinguish between real and generated samples.
- Training involves iterative optimization to minimize the difference between generated and real handwriting samples, typically using techniques like backpropagation and stochastic gradient descent.
- Hyperparameter tuning and model evaluation are performed to optimize the performance of the trained models.

**PDF Generation:**

- Once the handwriting generation models are trained, the next step is to integrate them with a PDF generation library, such as ReportLab.
- The PDF generation process involves creating a new PDF document or modifying an existing one to include handwritten-style text.
- Text content, formatting, and layout are determined based on user input or predefined templates.
- Handwritten-style text generated by the models is inserted into the PDF document according to the specified positions and formatting rules.

**Deployment and Scaling:**

- The completed application, including trained models, PDF generation functionality, and web interface components, is deployed to a hosting environment, such as cloud infrastructure or a dedicated server.
- Deployment considerations include scalability, reliability, and performance optimization to ensure smooth operation under varying usage loads.
- Monitoring and maintenance procedures are implemented to track application performance, address issues, and update components as needed.
- By following this technical implementation workflow, the project can successfully generate handwritten-style text and integrate it into PDF documents, providing a valuable tool for users to create personalized and visually appealing content.

![Flow chart](https://github.com/pathanasif1015/VH083-Innovators-Vashisht-Hackathon-IIITDM/assets/123537588/56f78934-4240-4c48-95d6-936a1f913e10)

## TECHSTACKS USED
`Tensorflow` , `PyTorch` , `GANs` , `RNNs` , `NLTK` , `SpaCy` , `ReportLab` , `Flask` , `Django` , `React.js` , `Vue.js` , `Python` , `JavaScript` , `Numpy` , `Pandas` , `Git` , `Docker`

## HOW TO RUN LOCALLY

- **Clone the repository** : First, you need to clone the repository from GitHub to your local machine. You can do this using the following command in your terminal or command prompt:
```
  git clone <https://github.com/pathanasif1015/VH083-Innovators-Vashisht-Hackathon-IIITDM>
```
- **Install Dependecies** : Navigate to the project directory and install any dependencies required by the project. This typically involves using a package manager like pip for Python projects or npm for JavaScript projects. Look for a requirements.txt file for Python projects or a package.json file for Node.js projects to identify the dependencies.

```
  cd project-directory
pip install -r requirements.txt
```
- **Configure Environment:** Some projects might require you to set up environment variables or configuration files. Refer to the project documentation or README file for instructions on how to set up the environment.

- **Run the Application**: Once dependencies are installed and the environment is configured, you can run the application. This could involve running a script, starting a server, or executing a specific command depending on the project.
 ```
 python app.py
```
- **Access the Application:** Once the application is running locally, you can access it using a web browser or any other appropriate client. The application might run on localhost or a specific IP address and port number. Check the project documentation or console output for details on how to access the application.

## CODE

**App py.file**
```
from flask import Flask, render_template, request, send_file
from PIL import Image
from fpdf import FPDF
import random

app = Flask(__name__)

# open background image
BG = Image.open("font/bg.png")

# set size of sheet to background image width
sizeOfSheet = BG.width

# set initial gap and cursor position (_)
gap, _ = 0, 0

# allowed characters
allowedChars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM, .-?!() 1234567890'

# function to add character/letter to current line in the image
def write(char):
    global gap, _
    if char == '\n':
        pass
    elif char == 'space':
        gap += 40  # arbitrary value; gap can be changed
    else:
        # lowercase the character
        char.lower()
        cases = Image.open("font/%s.png" % char)
        BG.paste(cases, (gap, _))
        size = cases.width
        gap += size
        del cases

# function to add word to current line in the image
def write_word(word):
    global gap, _
    # check if word is too long for current line
    if gap > sizeOfSheet - 95 * (len(word)):
        gap = 0
        _ += 200  # arbitrary value;

    # iterate over each letter in word
    for letter in word:
        # check if letter is an allowed character
        if letter in allowedChars:
            # if uppercase letter, make lowercase and add flag for uppercase version
            if letter.isupper():
                letter = letter.lower()
                letter += 'upper'
            # replace certain punctuation characters with corresponding flag names
            elif letter == '.':
                letter = "fullstop"
            elif letter == '!':
                letter = 'exclamation'
            elif letter == '?':
                letter = 'question'
            elif letter == ',':
                letter = 'comma'
            elif letter == '(':
                letter = 'braketop'
            elif letter == ')':
                letter = 'braketcl'
            elif letter == '-':
                letter = 'hiphen'
            write(letter)
            # Add a random space to place letters width of the image.
            xs = random.randint(10, 15)
            gap += xs
    # Add a space of random width after every word.
    xs = random.randint(50, 100)
    gap += xs

# function to convert input text into series of images
def worddd(input_text):
    global gap, _
    # split input text into list of words
    words_list = input_text.split(' ')
    for word in words_list:
        # check if word includes new line character
        if '\n' in word:
            # make gap 0 and increase cursor position (_) to move next line
            write_word(word.split('\n')[0])
            gap = 0
            _ += 200  # arbitrary value;
            write_word(word.split('\n')[1])
        # if no new line character, add word to image
        else:
            write_word(word)
            # add space character between each word
        write('space')


# function to generate images and combine into PDF file
def generate_pdf_text(data):
    global BG, gap, _

    # determine number of chunks to split text input into based on length of text
    nn = len(data) // 600
    chunks, chunk_size = len(data), len(data) // (nn + 1)
    p = [data[i:i + chunk_size] for i in range(0, chunks, chunk_size)]

    # create list to store image filenames
    imagelist = []

    # iterate over chunks and append space at the end of each chunk to add new line
    for i in range(len(p)):
        p[i] += ' '

    # join chunks using '\n' separator to add new line between each chunk
    data_with_newlines = '\n'.join(p)

    # call worddd function to convert text into image and save temporary image files
    worddd(data_with_newlines)
    BG.save(f"0outt.png")
    imagelist.append("0outt.png")

    BG1 = Image.open("font/bg.png")
    BG = BG1
    gap = 0
    _ = 0

    pdf = FPDF()

    # create new page and add image to it sequentially
    for image in imagelist:
        pdf.add_page()
        pdf.image(image, 0, 0, 210, 297)

    pdf.output("output.pdf", "F")

    for image in imagelist:
        Image.open(image).close()


def generate_pdf_file(file_path):
    with open(file_path, 'r') as f:
        data = f.read()

    generate_pdf_text(data)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    file = request.files['text']
    file_path = f'uploads/{file.filename}'
    file.save(file_path)

    generate_pdf_file(file_path)

    return send_file('output.pdf', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
```

**Skip to Content file**
```
from flask import Flask, render_template, request, send_file
from PIL import Image
from fpdf import FPDF
import random

app = Flask(__name__)

# open background image
BG = Image.open("font/bg.png")

# set size of sheet to background image width
sizeOfSheet = BG.width

# set initial gap and cursor position (_)
gap, _ = 0, 0

# allowed characters
allowedChars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM, .-?!() 1234567890'

# function to add character/letter to current line in the image
def write(char):
    global gap, _
    if char == '\n':
        pass
    elif char == 'space':
        gap += 40  # arbitrary value; gap can be changed
    else:
        # lowercase the character
        char.lower()
        cases = Image.open("font/%s.png" % char)
        BG.paste(cases, (gap, _))
        size = cases.width
        gap += size
        del cases

# function to add word to current line in the image
def write_word(word):
    global gap, _
    # check if word is too long for current line
    if gap > sizeOfSheet - 95 * (len(word)):
        gap = 0
        _ += 200  # arbitrary value;

    # iterate over each letter in word
    for letter in word:
        # check if letter is an allowed character
        if letter in allowedChars:
            # if uppercase letter, make lowercase and add flag for uppercase version
            if letter.isupper():
                letter = letter.lower()
                letter += 'upper'
            # replace certain punctuation characters with corresponding flag names
            elif letter == '.':
                letter = "fullstop"
            elif letter == '!':
                letter = 'exclamation'
            elif letter == '?':
                letter = 'question'
            elif letter == ',':
                letter = 'comma'
            elif letter == '(':
                letter = 'braketop'
            elif letter == ')':
                letter = 'braketcl'
            elif letter == '-':
                letter = 'hiphen'
            write(letter)
            # Add a random space to place letters width of the image.
            xs = random.randint(10, 15)
            gap += xs
    # Add a space of random width after every word.
    xs = random.randint(50, 100)
    gap += xs

# function to convert input text into series of images
def worddd(input_text):
    global gap, _
    # split input text into list of words
    words_list = input_text.split(' ')
    for word in words_list:
        # check if word includes new line character
        if '\n' in word:
            # make gap 0 and increase cursor position (_) to move next line
            write_word(word.split('\n')[0])
            gap = 0
            _ += 200  # arbitrary value;
            write_word(word.split('\n')[1])
        # if no new line character, add word to image
        else:
            write_word(word)
            # add space character between each word
        write('space')


# function to generate images and combine into PDF file
def generate_pdf_text(data):
    global BG, gap, _

    # determine number of chunks to split text input into based on length of text
    nn = len(data) // 600
    chunks, chunk_size = len(data), len(data) // (nn + 1)
    p = [data[i:i + chunk_size] for i in range(0, chunks, chunk_size)]

    # create list to store image filenames
    imagelist = []

    # iterate over chunks and append space at the end of each chunk to add new line
    for i in range(len(p)):
        p[i] += ' '

    # join chunks using '\n' separator to add new line between each chunk
    data_with_newlines = '\n'.join(p)

    # call worddd function to convert text into image and save temporary image files
    worddd(data_with_newlines)
    BG.save(f"0outt.png")
    imagelist.append("0outt.png")

    BG1 = Image.open("font/bg.png")
    BG = BG1
    gap = 0
    _ = 0

    pdf = FPDF()

    # create new page and add image to it sequentially
    for image in imagelist:
        pdf.add_page()
        pdf.image(image, 0, 0, 210, 297)

    pdf.output("output.pdf", "F")

    for image in imagelist:
        Image.open(image).close()


def generate_pdf_file(file_path):
    with open(file_path, 'r') as f:
        data = f.read()

    generate_pdf_text(data)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    file = request.files['text']
    file_path = f'uploads/{file.filename}'
    file.save(file_path)

    generate_pdf_file(file_path)

    return send_file('output.pdf', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
```

## RESULTS

**Font Sample**

![image](https://github.com/pathanasif1015/VH083-Innovators-Vashisht-Hackathon-IIITDM/assets/123537588/9ba2047a-1de0-4215-977d-cc8ff7bb36c3)

**Running in CMD**

![Screenshot (2)](https://github.com/pathanasif1015/VH083-Innovators-Vashisht-Hackathon-IIITDM/assets/123537588/f33b75ba-2d0e-481e-89d8-4854f176bec4)

**Interface Design**

![Screenshot (3)](https://github.com/pathanasif1015/VH083-Innovators-Vashisht-Hackathon-IIITDM/assets/123537588/c2bc918d-7c7b-4c6c-a288-7875067471a3)

**Sample text data**

![Screenshot (4)](https://github.com/pathanasif1015/VH083-Innovators-Vashisht-Hackathon-IIITDM/assets/123537588/d77466a4-bcff-464c-8fe9-770fd72802df)

**Generated Hand-Writing**

![Screenshot (5)](https://github.com/pathanasif1015/VH083-Innovators-Vashisht-Hackathon-IIITDM/assets/123537588/e1c614de-f665-412a-bbbf-27827a9ebe29)

## WHAT'S NEXT

Expanding the project to create a website and app where users can access their own handwriting by uploading their handwritten fonts is an exciting future plan. Here are some key steps and considerations for implementing this feature:

- **User Interface Design:**
   - Design a user-friendly interface for both the website and the mobile app, allowing users to easily upload their handwritten samples.
Consider implementing features such as drag-and-drop functionality or camera integration for capturing handwritten samples directly from mobile devices.
Handwriting Recognition System:
   - Develop or integrate a handwriting recognition system that can process the uploaded handwritten samples.
Utilize machine learning techniques, such as deep learning models or GANs, to accurately recognize and digitize the handwritten text.
Train the recognition system on diverse handwriting styles to ensure robust performance across different users.

- **Font Generation:**

   - Once the handwriting is recognized, generate a digital font based on the user's handwriting style.
   - Implement algorithms to convert the recognized handwriting into vector-based font glyphs.
   - Provide customization options for users to adjust parameters such as stroke thickness, spacing, and alignment to personalize their fonts.

- **Preview and Download:**
   - Offer users the ability to preview their generated fonts in real-time.
   - Allow users to download the generated fonts in various formats compatible with popular design software or word processors.

- **User Authentication and Privacy:**
   - Implement user authentication mechanisms to secure user accounts and access to generated fonts.
   - Ensure compliance with data privacy regulations and provide users with control over their data and uploaded content.

- **Cross-Platform Compatibility:**
   - Ensure that the website and mobile app are compatible with a wide range of devices and operating systems.
   - Optimize the user experience for both desktop and mobile users.
     
- **Community and Sharing Features:**
   - Create a platform where users can share their generated fonts with others in the community.
   - Implement social features such as liking, commenting, and sharing to encourage user engagement and collaboration.
     
- **Feedback and Improvement:**
   - Collect user feedback to continuously improve the handwriting recognition accuracy and font generation quality.
   - Iterate on the system based on user suggestions and usage patterns to enhance the overall user experience.

 
- **SAMPLE INTERFACE OF FUTURE WORK FOR UPLOADING OWN HAND-WRITING**
  
![image](https://github.com/pathanasif1015/VH083-Innovators-Vashisht-Hackathon-IIITDM/assets/123537588/7073d821-0c25-4fc8-bb89-f2204b63b89f)

## DECARATION

We confirm that the project showcased here was either developed entirely during the hackathon or underwent significant updates within the hackathon timeframe. We understand that if any plagiarism from online sources is detected, our project will be disqualified, and our participation in the hackathon will be revoked.
