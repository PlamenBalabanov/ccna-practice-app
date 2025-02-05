from flask import Flask, render_template, request, redirect, url_for, flash, session
from app import app, db
from app.models import Question
from sqlalchemy.sql import func
import csv
from io import TextIOWrapper

@app.route('/')
def index():
    # Initialize session for seen questions if not already set
    if 'seen_questions' not in session:
        session['seen_questions'] = []

    # Fetch a random question that the user hasn't seen yet
    total_questions = Question.query.count()
    if len(session['seen_questions']) >= total_questions:
        flash('You have answered all the questions!', 'info')
        return render_template('index.html', question=None, total_questions=total_questions, progress=100)

    # Get a random question not in the seen_questions list
    question = Question.query.filter(~Question.id.in_(session['seen_questions'])).order_by(func.random()).first()

    # Add the question ID to the seen_questions list
    if question:
        session['seen_questions'].append(question.id)
        session.modified = True  # Ensure the session is saved

    # Calculate progress
    progress = len(session['seen_questions']) / total_questions * 100

    return render_template('index.html', question=question, total_questions=total_questions, progress=progress)

@app.route('/reset', methods=['POST'])
def reset_session():
    # Reset the seen_questions list
    session['seen_questions'] = []
    session.modified = True
    return redirect(url_for('index'))

#@app.route('/delete/<int:question_id>', methods=['POST'])
#def delete_question(question_id):
#    question = Question.query.get_or_404(question_id)
#    db.session.delete(question)
#    db.session.commit()
#    flash('Question deleted successfully!', 'success')
#    return redirect(url_for('index'))

@app.route('/add', methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        if 'csv_file' in request.files:
            # Handle bulk upload via CSV
            csv_file = request.files['csv_file']
            if csv_file.filename.endswith('.csv'):
                try:
                    csv_reader = csv.DictReader(TextIOWrapper(csv_file, encoding='utf-8'))
                    for row in csv_reader:
                        new_question = Question(
                            text=row['text'],
                            image_url=row['image_url'],
                            option_a=row['option_a'],
                            option_b=row['option_b'],
                            option_c=row['option_c'],
                            option_d=row['option_d'],
                            correct_answer=row['correct_answer'],  # e.g., "A,B,C"
                            explanation=row['explanation']
                        )
                        db.session.add(new_question)
                    db.session.commit()
                    flash('Questions uploaded successfully!', 'success')
                except Exception as e:
                    db.session.rollback()
                    flash(f'Error uploading CSV: {str(e)}', 'error')
            else:
                flash('Invalid file format. Please upload a CSV file.', 'error')
        else:
            # Handle single question addition
            text = request.form['text']
            image_url = request.form['image_url']
            option_a = request.form['option_a']
            option_b = request.form['option_b']
            option_c = request.form['option_c']
            option_d = request.form['option_d']
            option_e = request.form.get('option_e', None)
            option_f = request.form.get('option_f', None)
            correct_answer = request.form['correct_answer']  # e.g., "A,B,C"
            explanation = request.form['explanation']

            new_question = Question(
                text=text,
                image_url=image_url,
                option_a=option_a,
                option_b=option_b,
                option_c=option_c,
                option_d=option_d,
                option_e=option_e,
                option_f=option_f,
                correct_answer=correct_answer,
                explanation=explanation
            )
            db.session.add(new_question)
            db.session.commit()
            flash('Question added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add_question.html')

# New routes for additional pages
@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy_policy.html')

@app.route('/about-us')
def about_us():
    return render_template('about_us.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submission (e.g., send email)
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Add your logic here (e.g., send email or save to database)
        flash('Your message has been sent!', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route('/terms-of-service')
def terms_of_service():
    return render_template('terms_of_service.html')
