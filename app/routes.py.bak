from flask import Flask, render_template, request, redirect, url_for, flash
from app import app, db
from app.models import Question
from sqlalchemy.sql import func
import csv
from io import TextIOWrapper

@app.route('/')
def index():
    # Fetch a random question
    question = Question.query.order_by(func.random()).first()
    total_questions = Question.query.count()
    return render_template('index.html', question=question, total_questions=total_questions)

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
                csv_reader = csv.DictReader(TextIOWrapper(csv_file, encoding='utf-8'))
                for row in csv_reader:
                    new_question = Question(
                        text=row['text'],
                        image_url=row['image_url'],
                        option_a=row['option_a'],
                        option_b=row['option_b'],
                        option_c=row['option_c'],
                        option_d=row['option_d'],
                        correct_answer=row['correct_answer'],
                        explanation=row['explanation']
                    )
                    db.session.add(new_question)
                db.session.commit()
                flash('Questions uploaded successfully!', 'success')
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
            correct_answer = request.form['correct_answer']
            explanation = request.form['explanation']

            new_question = Question(
                text=text,
                image_url=image_url,
                option_a=option_a,
                option_b=option_b,
                option_c=option_c,
                option_d=option_d,
                correct_answer=correct_answer,
                explanation=explanation
            )
            db.session.add(new_question)
            db.session.commit()
            flash('Question added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add_question.html')
