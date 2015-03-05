from flask import Flask, render_template, request, redirect, Markup, url_for
import markdown
from search_mod import search_request, scrape_site

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    with open('readme.md') as r:
        content = r.read()
        r.close()

    readme = Markup(markdown.markdown(content))

    if request.method == 'POST':
        return redirect('results')
    return render_template('home.html', readme=readme)


@app.route('/results', methods=['GET', 'POST'])
def results():
    page_type = 'results'

    results = search_request(request.form['searchfield'])

    return render_template('results.html', page_type=page_type, results=results)


@app.route('/results/article', methods=['GET', 'POST'])
def view_article():
    page_type = 'view_article'
    
    article = scrape_site(request.form['view'])

    return render_template('results.html', page_type=page_type, article=article)

if __name__ == '__main__':
    app.run(debug=True)