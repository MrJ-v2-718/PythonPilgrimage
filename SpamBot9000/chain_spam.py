import os
from importlib import reload
import email_spam

mod_time = os.path.getmtime(send_gmail.__file__)

emails = [  # Could be large list or stored in file
    'somerando@microsoft.com',
    'secretary@whitehouse.gov',
    'janitor@vatican.va'
]

my_email = 'Pappy1@gmail.com'
subject = 'Spam!'
text = ("If you don't forward this email to 5 people, "
        "you will stub your pinky toe on a door frame!")

for addr in emails:
    email_spam.send(subject, addr, my_email, text)

    # Check if file has been modified
    last_mod = os.path.getmtime(email_spam.__file__) 
    if last_mod > mod_time:
        mod_time = last_mod
        reload(email_spam)

