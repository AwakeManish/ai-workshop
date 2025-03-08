#importing the library
import google.generativeai as genai

#configure the api key
genai.configure(api_key="AIzaSyA1zN-pOA-_bkefHtV1mnB_vLXClPTxq2c")

#declaring the model
model =genai.GenerativeModel("gemini-1.5-pro")

#asking for response
response = model.generate_content("What is AI")

#printing the response
print(response.text)