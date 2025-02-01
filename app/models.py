from app import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    image_url = db.Column(db.String(200))
    option_a = db.Column(db.String(200), nullable=False)
    option_b = db.Column(db.String(200), nullable=False)
    option_c = db.Column(db.String(200), nullable=False)
    option_d = db.Column(db.String(200), nullable=False)
    correct_answer = db.Column(db.String(10), nullable=False)  # Store multiple answers as "A,B,C"
    explanation = db.Column(db.String(1000))

    def __repr__(self):
        return f'<Question {self.text}>'
