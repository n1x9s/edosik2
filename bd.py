import os
from app import Feedback


def extract_data_to_file():
    feedback_data = Feedback.query.all()
    project_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(project_directory, 'bd.txt')

    with open(file_path, 'w') as file:
        for feedback in feedback_data:
            file.write(
                f"ID: {feedback.id}, Name: {feedback.name}, Email: {feedback.email}, Message: {feedback.message}\n")
