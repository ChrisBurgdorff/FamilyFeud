class Answer:
    def __init__(self, text: str, popularity: int):
        self.text = text
        self.popularity = popularity

class Question:
    def __init__(self, text: str, answers: list[Answer] = []):
        self.text = text
        self.answers = answers

class Score:
    def __init__(self, total: int = 0, incorrect_guesses: int = 0):
        self.total = total
        self.incorrect_guesses = incorrect_guesses