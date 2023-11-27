import os  

from flask import Flask, render_template, request

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template("head.html")

@app.route('/data', methods = ['GET', 'POST'])
def books_data():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        description = request.form['description']
        publication_date = request.form['publication_date']
        new_book = Book(title = title, )
    return render_template("books.html")

@app.route('/images', methods = ['GET', 'POST'])
def images():
    if request.method == 'POST':
        file = request.files.get('file')
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))
        return "Zapisano obraz"
    return render_template("books_img.html")

if __name__ == '__main__':
    app.run(debug=True)

