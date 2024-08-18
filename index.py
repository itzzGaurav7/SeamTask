from instabot import Bot
import time

bot = Bot()

#login
bot.login(username="Username", password="password")

# extracting user comments  
def get_commenters(post_url):
    media_id = bot.get_media_id_from_link(post_url)
    comments = bot.get_media_comments_all(media_id)
    users = set()  # for unique users
    for comment in comments:
        users.add(comment['user']['username'])

    for user in users:
        print(user)

    with open("users.txt", "w") as user_file:
        user_file.write("User List:\n")
        for user in users:
            user_file.write(f"{user}\n")  
        
    return list(users)

# sending dm
def send_dm_to_commenters(users, message):
    successful = []
    failed = []
    
    for user in users:
        try:
            bot.send_message(message, user)
            successful.append(user)
            print(f"DM sent to: {user}")
            time.sleep(10)  #every 10 seconds message is sent
        except Exception as e:
            print(f"Failed to send DM to: {user}, Error: {e}")
            failed.append(user)
    
    return successful, failed

# main function
def main():
    post_url = input("Enter the post URL: ")  
    message = input("Input the message to be sent: ")
    
    users = get_commenters(post_url)
    successful, failed = send_dm_to_commenters(users, message)
    
    # writing results to a file
    with open("log.txt", "w") as log_file:
        log_file.write("Successfully sent to:\n")
        for user in successful:
            log_file.write(f"{user}\n")
        
        log_file.write("\nFailed to send to:\n")
        for user in failed:
            log_file.write(f"{user}\n")

if __name__ == "__main__":
    main()
