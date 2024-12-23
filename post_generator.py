import pandas as pd
import json
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
import streamlit as st



load_dotenv()
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama3-8b-8192")

class FewShotPosts:
    def __init__(self, file_path="data/processed_posts.json"):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)

    def load_posts(self, file_path):
        with open(file_path, encoding="utf-8") as f:
            posts = json.load(f)
            self.df = pd.json_normalize(posts)
            self.df['length'] = self.df['line_count'].apply(self.categorize_length)

            all_tags = self.df['tags'].apply(lambda x: x).sum()
            self.unique_tags = list(set(all_tags))

    def get_filtered_posts(self, length, language, tag):
        df_filtered = self.df[
            (self.df['tags'].apply(lambda tags: tag in tags)) & 
            (self.df['language'] == language) & 
            (self.df['length'] == length) 
        ]
        return df_filtered.to_dict(orient='records')

    def categorize_length(self, line_count):
        if line_count < 5:
            return "Short"
        elif 5 <= line_count <= 10:
            return "Medium"
        else:
            return "Long"

    def get_tags(self):
        return self.unique_tags
    


few_shot = FewShotPosts()


def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"


def generate_post(length, language, tag, your_content, selected_tone, selected_style):


    prompt = get_prompt(length, language, tag, your_content, selected_tone, selected_style)
    response = llm.invoke(prompt)
    print( f'response{response}')
    return response.content


def get_prompt(length, language, tag, your_content, selected_tone, selected_style):
    length_str = get_length_str(length)

    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.

    1) Topic: {tag}
    2) Length: {length_str}
    3) Language: {language}
    4) Tone: {selected_tone}
    5) Style: {selected_style}
    If Language is Hinglish then it means it is a mix of Hindi and English. 
    The script for the generated post should always be in English.
    4) Use the writing style as per the following examples.
    5) The following content is provided by the user. Please revise it to sound more professional and in line with the tone of the examples:
    Your content: "{your_content}"
    '''

    examples = few_shot.get_filtered_posts(length, language, tag)

    if len(examples) > 0:
        prompt += "4) Use the writing style as per the following examples."

    for i, post in enumerate(examples):
        post_text = post['text']
        prompt += f'\n\n Example {i+1}: \n\n {post_text}'

        if i == 1: 
            break

    return prompt



def user_feedback(feedback, generated_post, length, language, tag, content, tone, style):
    if feedback == "Yes":
        st.success("Thank you for your feedback! Your post is ready.")
    elif feedback == "No":
        st.write("Regenerating your post...")
        new_generated_post = generate_post(length, language, tag, content, tone, style)
        st.subheader("New Generated Post:")
        st.write(new_generated_post)
        feedback = st.radio("Is the post acceptable?", ("Yes", "No"),key=f"feedback_{new_generated_post}")
        user_feedback(feedback, new_generated_post, length, language, tag, content, tone, style)

