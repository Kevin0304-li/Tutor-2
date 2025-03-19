from flask import Flask, render_template, flash, redirect, url_for, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
import os
from sqlalchemy import event
# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Create upload folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize database
db = SQLAlchemy(app)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'warning'

# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default='student')  # 'student', 'teacher', etc.
    profile_image = db.Column(db.String(200), default='default_profile.jpg')
    posts = db.relationship('Post', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)
    progress = db.relationship('UserProgress', backref='user', lazy=True)

# Post model for community page
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_path = db.Column(db.String(200))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    likes = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comments = db.relationship('Comment', backref='post', lazy=True)

# Comment model
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

# Learning Progress Models
class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_en = db.Column(db.String(100), nullable=False)
    name_zh = db.Column(db.String(100), nullable=False)
    description_en = db.Column(db.Text)
    description_zh = db.Column(db.Text)
    icon = db.Column(db.String(50))
    order = db.Column(db.Integer)
    parent_id = db.Column(db.Integer, db.ForeignKey('topic.id'))
    children = db.relationship('Topic', backref=db.backref('parent', remote_side=[id]))
    concepts = db.relationship('Concept', backref='topic', lazy=True)
    user_progress = db.relationship('UserProgress', backref='topic', lazy=True)

class Concept(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_en = db.Column(db.String(100), nullable=False)
    name_zh = db.Column(db.String(100), nullable=False)
    content_en = db.Column(db.Text)
    content_zh = db.Column(db.Text)
    difficulty = db.Column(db.String(20))  # beginner, intermediate, advanced
    estimated_time = db.Column(db.Integer)  # in minutes
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    quiz_questions = db.relationship('QuizQuestion', backref='concept', lazy=True)

class QuizQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_en = db.Column(db.Text, nullable=False)
    question_zh = db.Column(db.Text, nullable=False)
    options_en = db.Column(db.JSON)
    options_zh = db.Column(db.JSON)
    correct_answer = db.Column(db.Integer)
    explanation_en = db.Column(db.Text)
    explanation_zh = db.Column(db.Text)
    concept_id = db.Column(db.Integer, db.ForeignKey('concept.id'), nullable=False)

class UserProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    concept_id = db.Column(db.Integer, db.ForeignKey('concept.id'), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    quiz_score = db.Column(db.Float)
    last_activity = db.Column(db.DateTime, default=datetime.utcnow)

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    language = session.get('language', 'english')
    explanation_level = session.get('explanation_level', 'normal')
    return render_template('index.html', language=language, level=explanation_level)

@app.route('/set_language/<language>')
def set_language(language):
    session['language'] = language
    return redirect(request.referrer or url_for('index'))

@app.route('/set_level/<level>')
def set_level(level):
    session['explanation_level'] = level
    return redirect(request.referrer or url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('index'))
        else:
            flash('Login failed. Please check your credentials.', 'danger')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role', 'student')
        
        # Check if username or email exists
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            flash('Username or email already exists.', 'danger')
            return redirect(url_for('register'))
        
        # Handle profile image
        profile_image = 'default_profile.jpg'
        if 'profile_image' in request.files:
            file = request.files['profile_image']
            if file and file.filename and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'profiles', filename)
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                file.save(file_path)
                profile_image = f'profiles/{filename}'
        
        # Create new user
        new_user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password),
            role=role,
            profile_image=profile_image
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/community')
@login_required
def community():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('community.html', posts=posts)

@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        # Handle image upload
        image_path = None
        if 'image' in request.files:
            file = request.files['image']
            if file and file.filename and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'posts', filename)
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                file.save(file_path)
                image_path = f'uploads/posts/{filename}'
        
        new_post = Post(
            title=title,
            content=content,
            image_path=image_path,
            user_id=current_user.id
        )
        
        db.session.add(new_post)
        db.session.commit()
        
        flash('Your post has been created!', 'success')
        return redirect(url_for('community'))
    
    return render_template('create_post.html')

@app.route('/post/<int:post_id>/comment', methods=['POST'])
@login_required
def add_comment(post_id):
    post = Post.query.get_or_404(post_id)
    content = request.form.get('content')
    
    if content:
        comment = Comment(
            content=content,
            post_id=post.id,
            user_id=current_user.id
        )
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been added!', 'success')
    
    return redirect(url_for('community'))

@app.route('/explanation')
def explanation():
    language = session.get('language', 'english')
    explanation_level = session.get('explanation_level', 'normal')
    role = current_user.role if current_user.is_authenticated else 'student'
    
    # Get all topics with progress
    topics = Topic.query.order_by(Topic.order).all()
    
    if current_user.is_authenticated:
        for topic in topics:
            # Calculate progress percentage
            total_concepts = len(topic.concepts)
            if total_concepts > 0:
                completed_concepts = UserProgress.query.filter_by(
                    user_id=current_user.id,
                    topic_id=topic.id,
                    completed=True
                ).count()
                topic.progress = int((completed_concepts / total_concepts) * 100)
            else:
                topic.progress = 0
    else:
        # For non-authenticated users, show 0 progress
        for topic in topics:
            topic.progress = 0
    
    return render_template('explanation.html',
                          language=language,
                          level=explanation_level,
                          role=role,
                          topics=topics)

@app.route('/visualization')
@login_required
def visualization():
    return render_template('visualization.html')

@app.route('/api/quiz/<int:concept_id>')
@login_required
def get_quiz_questions(concept_id):
    language = session.get('language', 'english')
    questions = QuizQuestion.query.filter_by(concept_id=concept_id).all()
    
    quiz_data = []
    for q in questions:
        quiz_data.append({
            'id': q.id,
            'question': q.question_en if language == 'english' else q.question_zh,
            'options': q.options_en if language == 'english' else q.options_zh,
            'correct': q.correct_answer
        })
    
    return jsonify(quiz_data)

@app.route('/api/progress', methods=['POST'])
@login_required
def update_progress():
    data = request.get_json()
    concept_id = data.get('concept_id')
    completed = data.get('completed', False)
    quiz_score = data.get('quiz_score')
    
    concept = Concept.query.get_or_404(concept_id)
    
    progress = UserProgress.query.filter_by(
        user_id=current_user.id,
        concept_id=concept_id
    ).first()
    
    if not progress:
        progress = UserProgress(
            user_id=current_user.id,
            topic_id=concept.topic_id,
            concept_id=concept_id
        )
        db.session.add(progress)
    
    progress.completed = completed
    progress.quiz_score = quiz_score
    progress.last_activity = datetime.utcnow()
    
    db.session.commit()
    
    return jsonify({'status': 'success'})

# Create database tables if they don't exist
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True) 