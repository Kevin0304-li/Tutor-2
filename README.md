# AI Explainer Website

A bilingual (English/Chinese) Flask-based website that explains AI concepts in simple terms, with customizable explanation levels and role-based content.

## Features

- **Bilingual Support**: Toggle between English and Chinese explanations
- **Customizable Explanation Levels**: 
  - Normal mode for standard explanations
  - Simple mode ("Treat me like a 5-year-old") for simplified explanations
- **Role-Based Content**: Different explanations for students and teachers
- **Interactive Visualizations**: Using Chart.js to visualize AI concepts
- **Community Features**: Post, comment, and like functionality
- **User Authentication**: Register, login, and maintain user profiles

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite (can be upgraded to PostgreSQL/MySQL)
- **Frontend**: HTML, CSS, JavaScript with Bootstrap
- **Visualization**: Chart.js
- **Authentication**: Flask-Login

## Setup & Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ai-explainer
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python app.py
   ```

5. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Project Structure

```
/
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
├── static/              # Static files
│   ├── css/             # CSS stylesheets
│   ├── js/              # JavaScript files
│   └── img/             # Images
├── templates/           # HTML templates
│   ├── base.html        # Base template
│   ├── index.html       # Home page
│   ├── explanation.html # AI explanations
│   ├── visualization.html # Visualizations
│   ├── community.html   # Community page
│   └── ...
└── uploads/             # User uploaded content
```

## Customization

- Edit the content in `templates/explanation.html` to add more AI topics
- Modify visualizations in `templates/visualization.html`
- Customize styles in `static/css/style.css`

## Deployment

This application can be deployed on:

- PythonAnywhere
- Heroku
- Render
- Any web server with Python support

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 