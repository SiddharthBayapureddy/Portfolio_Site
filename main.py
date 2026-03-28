from flask import Flask, render_template, send_from_directory
import json
import os

def load_portfolio_data():

    # Loading json data
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
skills = portfolio_data.get('skills', [])
quote = portfolio_data.get('quote', {})

@app.context_processor
def inject_global_data():
    return dict(social_media=social_media)

@app.route('/', strict_slashes=False)
def index():
    return render_template(
        "index.html",
        about=about_me,
        projects=projects,
        experiences=experiences,
        skills=skills,
        quote=quote
    )

@app.route('/contact', strict_slashes=False)
def contact():
    return render_template("contact.html")

@app.route('/resume')
def resume():
    resume_filename = about_me.get('resume_path', 'Resume.pdf')
    return send_from_directory(os.getcwd(), resume_filename)

if __name__ == '__main__':
    app.run(debug=True, port=5000)