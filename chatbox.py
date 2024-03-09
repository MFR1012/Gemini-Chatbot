import re

questions_answers = [
    (r'hello', "Hello, how can I assist you?"),
    (r'who are you', "Hello, I am MFR AI PROMAX?"),
    (r'i need help finding a hospital, can you help me', "I'm always willing to help. Based on your location through positioning, the hospitals near you are Bach Mai Hospital and An Viet Hospital."),
    (r'can you give me the address of bach mai hospital', "Address XX, YY, ZZ."),
    (r'does bach mai hospital have consultations on saturdays', "Yes."),
    (r'what are the operating hours of bach mai hospital', "24/7"),
    (r'is bach mai hospital good', "Yes"),
    (r'what diseases does an viet hospital treat', "Google please."),
    (r'does the hospital have consultations on saturdays', "Which hospital, where?"),
    (r'where does dr. nguyen thi hoai an work', "I'm afraid Ms. An has been fired."),
    (r'is dr. nguyen thi hoai an good', "She must be good if she wasn't fired."),
    (r'what are dr. nguyen thi hoai an\'s consultation hours', "She has been cooked since xx/yy/zz."),
    (r'which is a good hospital for musculoskeletal diseases in hanoi', "Bach Mai Hospital."),
    (r'do you sell baby clothes', "I'm a chatbot?"),
    (r'do you work on sundays', "I work all the time because I'm an AI, but if you don't ask much, I get lazy.")
]

def get_response(input_str):
    input_str = input_str.lower()
    for pattern, response in questions_answers:
        if re.search(pattern, input_str):
            return response
    return "I'm sorry, I don't have a response for that."


while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("Bot:", response)