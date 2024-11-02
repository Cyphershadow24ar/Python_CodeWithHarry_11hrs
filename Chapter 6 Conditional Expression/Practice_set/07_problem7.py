#Write a program to find out whether a given post is talking about "harry" or not ?

# post ="Hey aniket why can't you focus on your carrier and studies and life bro ?"
post = input("Enter the post: ")

if("Aniket".lower() in post.lower()):
    print("This post is talking about Aniket.")
else:
    print("This post is not talking about Aniket.")