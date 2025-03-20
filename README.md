# HCI-helloWorld
A Mini Coding assignment to work with AI APIs

This Python application utilizes Hugging Face's API to generate text using the GPT-2 model, which is one of the popular generative models. The application sends a simple prompt ("Hello World, this is a test of the Hugging Face API.") to the model and receives a generated response, which is then printed.

2. Prerequisites
Hugging Face Account: You must have a Hugging Face account to generate an API token.
Python 3.x: The application is developed using Python 3.x. Ensure you have it installed.
Dependencies: The 'requests' library is required to make API calls and the 'transformers' library is required to run the huggingface api.

You can install by running the following commands in your terminal:
--pip install transformers
--pip install requests


Instructions:

To run this project, you need to enter your huggingface api in the variable "API_TOKEN" in the helloWorld.py file.
After that, enter your prompt in the variable 'data', replace the string "Say Hello World in a creative way, just use a single sentence." with your own prompt.

After running the file, you should get your response.
