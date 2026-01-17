I am a Full Stack Developer in Frankfurt aiming to become an AI Solution Architect by 2026. This project uses Django and Docker, deployed on Render. Important: My static files are not in a single folder but spread across 'css', 'js', 'img', and 'resume'. Help me clean up redundant text files in the root and optimize the architecture.

## Overall Project Description

This project is a professional portfolio website for a Full Stack Developer transitioning into an AI Solution Architect role. It showcases software development projects, case studies, and a blog to demonstrate technical expertise and thought leadership. The primary goal is to create a polished, high-performance web presence that reflects the skills and aspirations of its owner.

## Technical Structure

This section serves as a source of truth for the project's architecture, asset locations, and key configuration files.

### Folder Hierarchy

- **/blog**: A Django app for the blog functionality.
- **/cases**: Contains case study documents (e.g., PDFs).
- **/media**: User-uploaded content, managed by Django's media handling.
- **/pages**: A Django app for core pages like "About" and "Contact".
- **/portfolio**: The main Django project folder containing settings and root URL configuration.
- **/scss**: Contains the SASS source files for styling.
- **/static**: The central location for all static assets.
  - **/static/css**: Compiled CSS files.
  - **/static/img**: All images.
  - **/static/js**: JavaScript files.
  - **/static/resume**: Resume files.
- **/templates**: Django HTML templates.
- **/node_modules**: Contains Node.js dependencies for frontend asset building.
- **/.venv**: The Python virtual environment for this project.

### Orphan Files in Root

The following files exist in the root directory and should be reviewed for cleanup or relocation:

- `exported_data.txt`
- `exported_data_complete.txt`
- `test_cloudinary.py`
- `db.sqlite3` (This is the development database, which is acceptable in the root for a simple project, but might be better placed in a data-specific folder in the future).

### Key Configuration Files

- **Django Core:**
  - `portfolio/settings.py`: The main settings file for the Django project. **Static files are now configured to be served from the `/static/` directory.**
  - `portfolio/urls.py`: The root URL configuration for the Django project.
  - `manage.py`: The command-line utility for Django.
- **Deployment (Render):**
  - `render.yaml`: The configuration file for deploying the project on Render.
  - `build.sh`: A script executed by Render to build the project.
  - `requirements.txt`: Specifies the Python dependencies.
  - `runtime.txt`: Specifies the Python runtime version for Render.
- **Frontend & Styling:**
  - `package.json`: Defines Node.js dependencies and scripts for frontend tasks (like compiling SASS).
  - `scss/main.scss`: The main SASS file that imports all other styling partials.
- **Docker:**
  - **Note:** You mentioned Docker in the initial description, but no `Dockerfile` was found in the project. This should be added if containerization is a goal.

### Deployment Workflow

Specify that the local environment is the primary sandbox for testing and that Render should only receive verified code. Document that DEBUG is our safety switch for static file handling."
