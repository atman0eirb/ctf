from flask import Flask, request, render_template, abort
import os

app = Flask(__name__)

# Répertoire autorisé pour les fichiers et les articles


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view')
def view():
    
    article = request.args.get('article')
    article = "/app/templates/" + article
    try:
        with open(article, 'r') as file:
            content = file.read()
        return render_template('view_file.html', content=content)
    except Exception as e:
        return f"Error occured"


if __name__ == '__main__':
    app.run(debug=True)
