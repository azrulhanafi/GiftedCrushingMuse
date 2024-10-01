import os
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

#story generator 
def story_gen(prompt):
    system_prompt = """
    You are a world renowned 50 years experience                  children storyteller. 
    you will be given a concept to generate a story     suitable for ages 5-7 years old 
    """

    prompt = "friendship between ali and abu"

    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=1.3,
        max_tokens=100
    )

    return response.choices[0].message.content

  #story cover prompt generator 
def image_gen(prompt):
    response = client.images.generate(
        model = 'dall-e-2',
        prompt = prompt,
        size = '256x256',
        n=1,
      )

    return response.data[0].url

  #storybook method 
def storybook(prompt):
    story = story_gen(prompt)
    cover = image_gen(story)
    image = image_gen(cover)
    st.image(image)
    st.writer(story)

st.title("Storybook Generator for kids for fun")
st.divider()

prompt = st.text_input("Enter your story concept:")

if st.button("Generate Storybook"):
    story = story_gen(prompt)
    cover = cover_gen(story)
    image = image_gen(cover)

    st.write(image)
    st.write(story)

def cover_gen(prompt)
    system_prompt = """"
    you will be given a children story book. 
    Generate a prompt for a cover art that is suitable and         shows off the story themes. The prompt will be sent to         dall-e-2"""

response = client.chat.completions.create(model='gpt-3.5-turbo', messages=[{
    "role": "system","content": system_prompt}')

{"role": "user", "content": prompt}
      ],
      temperature=1.3,
      max_tokens=200
  )

  return response.choices[0].message.content