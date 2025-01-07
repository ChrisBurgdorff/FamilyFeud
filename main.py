import streamlit as st

from models import Answer

answer_1: Answer = Answer('Chicken Wings', 54)

def main():
    st.title("Hello World")


if __name__ == "__main__":
    main()

