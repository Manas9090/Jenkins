#pip install openai
import streamlit as st
import openai 
openai.api_key = "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"  # Replace with your actual OpenAI API key
def sentiment_analysis(text):
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages=[
            {"role": "system","content": "You are a helpful assistant."},
            {"role":"user","content": f"Analyze the sentiment of the following text:\n\n{text}"}

        ],
        
    )

    sentiment=response["choices"][0]["message"]["content"]
    return sentiment

def main(): 
    st.title("LLM Chat Application")

    user_input = st.text_input("You: ", "")

    if st.button("Send"):
        if user_input:
            response = sentiment_analysis(user_input)
            st.text_area("Assistant:", value=response, height=300)
        else:
            st.warning("Please enter a message.") 

if __name__ == "__main__":
    main()
