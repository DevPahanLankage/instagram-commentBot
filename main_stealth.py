import pprint
import sys, os
import time
import json
import random
from instagram_private_api import Client, ClientError
from contextlib import contextmanager
from colorama import Fore, Back
from colorama import init
init(autoreset=True)

sys.stdout.write('\033[A\033[K')

def usernameInput():
    username = input("Username: \n")
    return username

def passwordInput():
    password = input("Password: \n")
    return password

refreshReady = False
commentsReady = False
delay = 0
commentinput = ''
commentList = []
previousComments = {}

@contextmanager
def hide():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout

def getReady():
    global refreshReady
    global commentsReady
    global delay
    global commentinput
    global commentList
    while commentsReady == False:
        print('Please enter your comment or comments, separated by ' + Fore.RED + 'a colon.\n' + Fore.RESET
            + 'Example - ' + Back.WHITE + Fore.BLACK + 'comment 1:comment 2:comment 3')
        commentinput = input()
        commentList = commentinput.split(':')
        checkEmpty = 0
        for i in range(len(commentList)):
            if all('' == s or s.isspace() for s in commentList[i]):
                print(Back.LIGHTWHITE_EX + Fore.RED + '\n One or more item(s) in list are empty!')
                commentList = ''
                checkEmpty += 1
                break
        if checkEmpty == 0:
            commentsReady = True
            break

    while refreshReady == False:
        delay = input("\nPlease enter how many seconds you would like to wait between each refresh. A longer wait means a lesser chance of being action blocked, press enter to start program. \n")
        try:
            val = int(delay)
            refreshReady = True
            print("Autorefresh set to " + str(delay) +  " seconds. Press CTRL+C to choose new preferences or close the tab to stop.")
            return val
        except ValueError:
            try:
                val = float(delay)
                refreshReady = True
                print("Autorefresh set to " + str(delay) +  " seconds. Press CTRL+C to choose new preferences or close the tab to stop.")
                return val
            except ValueError:
                print(Back.LIGHTWHITE_EX + Fore.RED + "Inputted value is not a number!")

def stopLoop():
    global refreshReady
    global commentsReady
    refreshReady = False
    commentsReady = False

def human_like_delay():
    """Add human-like random delays to avoid detection"""
    delay = random.uniform(2, 8)  # Random delay between 2-8 seconds
    time.sleep(delay)

def get_timeline_stealth(api):
    """Get timeline with stealth methods"""
    try:
        # Try different method names that might exist
        methods_to_try = [
            'feed_timeline',
            'timeline_feed', 
            'get_timeline',
            'feed_timeline_feed',
            'user_feed'
        ]
        
        for method_name in methods_to_try:
            if hasattr(api, method_name):
                method = getattr(api, method_name)
                result = method()
                if result:
                    return result
        
        # If no method works, try direct API call
        return api._call_api('feed/timeline/')
        
    except Exception as e:
        print(f"Timeline error: {e}")
        return None

def post_comment_stealth(api, media_id, text):
    """Post comment with stealth methods"""
    try:
        # Add random delay before commenting
        human_like_delay()
        
        # Try different comment methods
        methods_to_try = [
            'media_comment',
            'post_comment',
            'comment_media',
            'add_comment'
        ]
        
        for method_name in methods_to_try:
            if hasattr(api, method_name):
                method = getattr(api, method_name)
                result = method(media_id, text)
                if result:
                    return result
        
        # If no method works, try direct API call
        return api._call_api(f'media/{media_id}/comment/', params={'comment_text': text})
        
    except Exception as e:
        print(f"Comment error: {e}")
        return False

print(Back.WHITE + Fore.BLACK + 'Instagram top comment bot, contact me at @simpifies if you have any questions\n')
print(Fore.RED + 'time to make some money niggas')
print(Fore.WHITE + 'if you dont want to get action blocked, use http://stcb.rf.gd\n')
print(Fore.YELLOW + '🕵️ STEALTH MODE: Using anti-detection techniques\n')

username = usernameInput()
password = passwordInput()

try:
    # Create client with stealth settings
    api = Client(
        username, 
        password,
        auto_patch=True,
        drop_incompat_key=True,
        timeout=30
    )
    
    print('\n' + Fore.CYAN + '✅ Logged in with stealth mode!')
    
    while True:
        getReady()
        while refreshReady == True and commentsReady == True:
            try:
                # Get timeline feed with stealth method
                timeline = get_timeline_stealth(api)
                
                # Read existing logs
                try:
                    with open('logData.txt', 'r') as logfile:
                        logs = logfile.read()
                except FileNotFoundError:
                    logs = ""
                
                if timeline and 'items' in timeline:
                    timeline_items = timeline['items']
                    i = 0
                    total = len(timeline_items)
                    
                    while i <= total - 1:
                        try:
                            text = random.choice(commentList)
                            media_id = timeline_items[i]['id']
                            post_username = timeline_items[i]['user']['username']
                            post_timestamp = timeline_items[i]['taken_at']
                            now_timestamp = time.time()
                            difference = float(now_timestamp) - float(post_timestamp)
                            
                            if media_id in logs:
                                status = Back.GREEN + Fore.BLACK + "[Success]"
                                msg = '[Already commented.]'
                            elif difference > 60:
                                status = Back.LIGHTWHITE_EX + Fore.BLACK + '[Expired]'
                                msg = '[More than 60 seconds]'
                            elif not timeline_items[i]['comment_count'] == 0:
                                status = Back.YELLOW + Fore.BLACK + '[-Failed-]'
                                msg = '[ Not first comment ]'
                            else:
                                status = Back.CYAN + Fore.BLACK + '[  Run  ]'
                                msg = '[Making comment.....]'
                                
                                # Make comment with stealth method
                                comment_result = post_comment_stealth(api, media_id, text)
                                previousComments[media_id] = text
                                
                                if comment_result:
                                    try:
                                        with open('logData.txt', 'a+') as savelog:
                                            savelog.seek(0)
                                            data = savelog.read(100)
                                            if len(data) > 0:
                                                savelog.write("\n")
                                            savelog.write(media_id)
                                    except IOError as e:
                                        print(f"Warning: Could not write to logData.txt: {e}")
                                else:
                                    try:
                                        with open('logData.txt', 'a+') as savelog:
                                            savelog.seek(0)
                                            data = savelog.read(100)
                                            if len(data) > 0:
                                                savelog.write("\n")
                                            savelog.write(media_id)
                                    except IOError as e:
                                        print(f"Warning: Could not write to logData.txt: {e}")
                                    
                                    msg = '[Unknown Error (Comments may be off)]'
                                    status = Back.YELLOW + Fore.BLACK + "[-FAILED-]"
                            
                            # Display results
                            if status == Back.CYAN + Fore.BLACK + '[  Run  ]' or status == Back.GREEN + Fore.BLACK + "[Success]":
                                comment_text = previousComments.get(media_id, '--none--')
                                print('({}) {}'.format(i, status) + Back.RESET + Fore.RESET + ' {} | {} | User: {} | Post age: '.format(msg, comment_text, post_username) + Back.YELLOW + Fore.BLACK + str(round(difference)) + Back.RESET)
                            elif status == Back.RED + Fore.BLACK + "[-FAILED-]":
                                comment_text = previousComments.get(media_id, '--none--')
                                print('({}) {}'.format(i, status) + Back.RESET + Fore.RESET + ' {} | {} | User: {} | Post age: '.format(msg, comment_text, post_username) + Back.YELLOW + Fore.BLACK + str(round(difference)) + Back.RESET)
                                sys.exit()
                            elif status == Back.YELLOW + Fore.BLACK + '[-Failed-]':
                                print('({}) {}'.format(i, status) + Back.RESET + Fore.RESET + ' {} | User: {} | Post age: '.format(msg, post_username) + Back.YELLOW + Fore.BLACK + str(round(difference)) + Back.RESET)
                            else:
                                print('({}) {}'.format(i, status) + Back.RESET + Fore.RESET + ' {} | --none-- | User: {} | Post age: '.format(msg, post_username) + Back.YELLOW + Fore.BLACK + str(round(difference)) + Back.RESET)
                                
                        except KeyError:
                            print('({}) '.format(i) + Back.YELLOW + Fore.BLACK + "[Couldn't get post]")
                        i += 1
                    
                    # Add human-like delay between cycles
                    human_like_delay()
                    time.sleep(float(delay))      
                    for x in range(i):
                        sys.stdout.write('\033[A\033[K')
                        
            except KeyboardInterrupt:
                print(Back.GREEN + Fore.BLACK + "\n Input received. Stopping.                                                                                                         ")
                stopLoop()
            except Exception as e:
                print(f"Error: {e}")
                # Add longer delay on error to avoid detection
                time.sleep(random.uniform(10, 20))
                
except ClientError as e:
    print(f"Login failed: {e}")
    print(Fore.YELLOW + "Try using a different account or wait before retrying")
except Exception as e:
    print(f"Unexpected error: {e}")
