from flask import Flask, render_template
import json

def load_portfolio_data():

    # Loadinf json data
    try:
        with open("portfolio_data.json", "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("ERROR: File 'portfolio_data.json' not found.")
        return {}
    except json.JSONDecodeError:
        print("ERROR: Could not decode JSON from 'portfolio_data.json'.")
        return {}

# Flask application
app = Flask("Portfolio")

# Loading all data from JSON
portfolio_data = load_portfolio_data()
about_me = portfolio_data.get("about_me", {})
social_media = portfolio_data.get('social_media', [])
experiences = portfolio_data.get('experiences', [])
projects = portfolio_data.get('projects', [])

@app.context_processor
def inject_global_data():
    return dict(social_media=social_media)

@app.route('/', strict_slashes=False)
def index():
    return render_template(
        "index.html",
        about=about_me,
        projects=projects,
        experiences=experiences
    )

@app.route('/contact', strict_slashes=False)
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)