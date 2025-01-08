import streamlit as st

from models.models import Answer, Question
from data.sample import SampleQuestions

question: Question = SampleQuestions.get_spoiled_question()
guessed_answers: list[str] = []
current_guess: str = ''

def submit_guess(guess: str) -> None:
    global guessed_answers
    guessed_answers.append(guess)
    print('current_guess: ' + guess)
    print('guessed_answers: ')
    print(guessed_answers)

def main():
    st.image('images/Squad Squabble 2.webp', width=300)
    st.text('We surveyed 100 people')
    st.text(f'The top {len(question.answers)} answers are on the board')
    st.title(question.text)
    user_input = st.text_input(label ='Your Guess: ')
    st.button('Submit', on_click=lambda: submit_guess(user_input))
    col1, col2 = st.columns(2)

    with col1:
        for answer in question.answers[0:3]:
            if answer.text in guessed_answers:
                st.text_input(label="answer", value=answer.text, disabled=True, key=answer.text, label_visibility='hidden')
            else:
                st.text_input(label="answer", value='',disabled=True, key=answer.text, label_visibility='hidden')
    if len(question.answers) > 3:
        with col2:
            for answer in question.answers[3:len(question.answers)]:
                if answer.text in guessed_answers:
                    st.text_input(label="answer", value=answer.text, disabled=True, key=answer.text, label_visibility='hidden')
                else:
                    st.text_input(label="answer", value='',disabled=True, key=answer.text, label_visibility='hidden')


if __name__ == "__main__":
    main()


# Name Something That Can Be Spoiled	Milk	56	Food	17	Kids	13	A Surprise	5

