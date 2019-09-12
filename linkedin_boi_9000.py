#!/usr/bin/python
import praw
import config
import pdb
import re
import os
import random
import time

linkedin_quotes = ["How have you been?", "Please keep in touch", "I will", "Will do", "Thanks", "Done", "Please check", "Thank you very much", 
"Have a nice day", ":)", "What about you?", "What do you do?", ":D", "Where do you live?", "Where are you working now?", "Congrats on the anniversary!", 
"Oh...","Hmm", "Goodbye", "Thank you", "You too", "Good night", "Take care", "See you soon", "Regards", "Resume", "Thanks for sharing", 
"I'll get back to you", "Haha", "Just kidding", "How about you?", "Where are you these days?", "Where are you now?", "How's life", 
"Keep in touch", "I'm good", "Take care", "See you soon", "Long time no see", "Hope all is well", "How are you?", "Hey, *insert your name here*", 
"Thanks for reaching out", "How can I help you?"]

def bot_login():
	r = praw.Reddit(username = config.username, 
			password = config.password, 
			client_id = config.client_id, 
			client_secret = config.client_secret,
			user_agent = "test")
	return r

def run_bot():
    user = r.redditor('dood1337')
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    # If we have run the code before, load the list of comments we have replied to
    else:
    # Read the file into a list and remove any empty values
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = list(filter(None, comments_replied_to))
    for comment in user.comments.new():
        time.sleep(5)
        if comment.id not in comments_replied_to:
            try: 
                print(comment.body)
                if ( (len(comments_replied_to) % 1000 ) == 0 ):
                    comment.reply("""
                           ---                                     
                        -        --                             
                    --( /     \ )XXXXXXXXXXXXX                   
                --XXX(   O   O  )XXXXXXXXXXXXXXX-              
               /XXX(       U     )        XXXXXXX\               
             /XXXXX(              )--   XXXXXXXXXXX\             
            /XXXXX/ (      O     )   XXXXXX   \XXXXX\
            XXXXX/   /            XXXXXX   \   \XXXXX----        
            XXXXXX  /          XXXXXX         \  ----  -         
    ---     XXX  /          XXXXXX      \           ---        
      --  --  /      /\  XXXXXX            /     ---=         
        -        /    XXXXXX              '--- XXXXXX         
          --\/XXX\ XXXXXX                      /XXXXX         
            \XXXXXXXXX                        /XXXXX/
             \XXXXXX                         /XXXXX/         
               \XXXXX--  /                -- XXXX/       
                --XXXXXXX---------------  XXXXX--         
                   \XXXXXXXXXXXXXXXXXXXXXXXX-            
                     --XXXXXXXXXXXXXXXXXX-)""")
                else:
                	comment.reply(linkedin_quotes[random.randint(0, len(linkedin_quotes)-1)])
                comments_replied_to.append(comment.id)
            except praw.exceptions.APIException as e:
                if e.error_type == 'DELETED_COMMENT':
                    print("Comment " + comment.id + " was deleted")
                    comments_replied_to.append(comment.id)
                elif e.error_type == 'RATELIMIT':
                	print(e)
                	print("ratelimit exception oops time to become a sleepy boi")
                	break
                else:
                    comment.reply(linkedin_quotes[random.randint(0, len(linkedin_quotes)-1)])
                    print(e)
                    comments_replied_to.append(comment.id)
        with open("comments_replied_to.txt", "w") as f:
            for comment_id in comments_replied_to:
                f.write(comment_id + "\n")

if __name__ == "__main__":
    r = bot_login()
    run_bot()

