import praw
# import config
import time
import os
import json

def bot_login(credfile):
	
	credfile = 'credfile.json'
	credfile_prefix = ''
	
	print("Logging in...")
	
	# Read credentials to a dictionary
	with open(credfile) as fh:
		creds = json.loads(fh.read())
		
	r = praw.Reddit(client_id=creds['client_id'], client_secret=creds['client_secret'], user_agent=creds['user_agent'])
	
	print("Logged in!")
	
	return r


def run_bot(r, comments_replied_to):
	print("Searching last 1,000 comments")

	for comment in r.subreddit('test').comments(limit=1000):
		if "sample user comment" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
			print("String with \"sample user comment\" found in comment " + comment.id)
			comment.reply("Hey, I like your comment!")
			print("Replied to comment " + comment.id)

			comments_replied_to.append(comment.id)

			with open ("comments_replied_to.txt", "a") as f:
				f.write(comment.id + "\n")

	print("Search Completed.")

	print(comments_replied_to)

	print("Sleeping for 10 seconds...")
	#Sleep for 10 seconds...		
	time.sleep(10)

def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = filter(None, comments_replied_to)

	return comments_replied_to

credfile = 'credfile.json'
r = bot_login(credfile)
comments_replied_to = get_saved_comments()
print(comments_replied_to)

while True:
	run_bot(r, comments_replied_to)
