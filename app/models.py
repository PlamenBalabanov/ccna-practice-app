from app import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000), nullable=False)
    image_url = db.Column(db.String(200))
    option_a = db.Column(db.String(200), nullable=False)
    option_b = db.Column(db.String(200), nullable=False)
    option_c = db.Column(db.String(200), nullable=False)
    option_d = db.Column(db.String(200), nullable=False)
    option_e = db.Column(db.String(200))  # Optional
    option_f = db.Column(db.String(200))  # Optional
    correct_answer = db.Column(db.String(10), nullable=False)  # Allow up to 10 characters
    explanation = db.Column(db.String(1000))

    def __repr__(self):
        return f'<Question {self.text}>'
