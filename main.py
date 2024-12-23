import streamlit as st
from post_generator import FewShotPosts
from post_generator import generate_post, user_feedback


length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]
tone_options = ["Formal", "Informal", "Professional", "Motivational", "Friendly"]
style_options = ["Inspirational", "Informative", "Question-based"]


def main():
    st.subheader("LinkedIn Post Generator")

    col1, col2, col3, col4, col5 = st.columns(5)

    fs = FewShotPosts()
    tags = fs.get_tags()
    with col1:
        selected_tag = st.selectbox("Topic", options=tags)

    with col2:
        selected_length = st.selectbox("Length", options=length_options)

    with col3:
        selected_language = st.selectbox("Language", options=language_options)

    with col4:
        selected_tone = st.selectbox("Tone", options=tone_options)

    with col5:
        selected_style = st.selectbox("Style", options=style_options)

    your_content = st.text_input("Content you wish to post")

    post = generate_post(selected_length, selected_language, selected_tag, your_content, selected_tone, selected_style)
    st.write(post)


    st.subheader("Do you like the generated post?")
    feedback = st.radio("Is the post acceptable?", ("None","Yes", "No"))
    user_feedback(feedback, post, selected_length, selected_language, selected_tag, selected_tag, selected_tone, selected_style)



if __name__ == "__main__":
    main()
