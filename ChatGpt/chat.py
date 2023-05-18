import openai
openai.api_key ='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'
while True:
 ask= input ("Dua'a : ")
 response = openai.Completion.create(
  model="text-davinci-003",
  prompt=ask,
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.6,
  
)
 text=response ['choices'][0]['text']
 print ("chatgpt" + text)


