import os
from app import create_app

config = os.getenv('PROJECT_SETTINGS') or 'development'
app = create_app()

@app.shell_context_processor
def make_shell_context():
    """Extend the Flask shell context."""
    return {'app': app}

if __name__ == '__main__':
    with app.app_context():
        app.run(host='0.0.0.0')
