"""
Code for user_greetings tool.
"""

import datetime

def greet_user() -> str:
    text = ""
    
    current_time = datetime.datetime.now()
    if current_time.hour < 12:
        text = "Good morning!"
    elif current_time.hour < 18:
        text = "Good afternoon!"
    else:
        text = "Good evening!"
    
    text += "\n\nCan you please introduce yourself?"

    return text
