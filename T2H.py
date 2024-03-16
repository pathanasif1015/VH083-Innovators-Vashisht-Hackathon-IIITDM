from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
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
