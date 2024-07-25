pip install python-aiml
import aiml
kernel = aiml.Kernel() 
kernel.learn("C:\\Users\\Asus\\OneDrive\\Desktop\\shruti\\startup.xml") 
kernel.respond("load assign 1")

while True: 
 input_txt= input(">input:")
 if input_txt.lower() == "thank you":
    print("> Bot: Goodbye! Take care and stay healthy.")
    break
 response =kernel.respond(input_txt) 
 print(">Bot: "+response)
