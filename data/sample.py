from models.models import Answer, Question

class SampleQuestions:
    @staticmethod
    def get_spoiled_question() -> Question:
        return Question(
            'Name Something That Can Be Spoiled',
            [
                Answer('Milk', 56),
                Answer('Food', 17),
                Answer('Kids', 13),
                Answer('Surprise', 5)
            ]
        )
    
    @staticmethod
    def get_all_questions() -> list[Question]:
        return [
            SampleQuestions.get_spoiled_question(),
            # Add more questions here as needed
        ]