from flask import Flask , render_template
import json

# Loading portfolio data
def load_portfolio_data():

    try:
        with open("portfolio_data.json" , "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("ERROR: File not found")
        return {}
    except json.JSONDecodeError:
        print("ERROR: Could not decode file")
        return {}

# Flash application
app = Flask("Portfolio")


# Loading data from json
portfolio_data = load_portfolio_data()

about_me = portfolio_data.get("about_me" , {})
social_media = portfolio_data.get('social_media', [])
experiences = portfolio_data.get('experiences', [])
projects = portfolio_data.get('projects', [])


@app.context_processor
def inject_socials():
    return dict(social_media=social_media)


# Root Directory
@app.route('/' , strict_slashes = False)
def index():
    # Returns about me section
    return render_template("index.html" , about=about_me)


# Projects page
@app.route("/projects")
def projects_page():
    # Returns my projects
    return render_template("projects.html" , projects=projects)


# Experiences Page
@app.route('/experience')
def experience_page():
    """Serves the experience page."""
    return render_template('experiences.html', experiences=experiences)


app.run(debug=True, port=5000)