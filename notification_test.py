from pushbullet import Pushbullet

API = "Your PushBullet API KEY goes here"

test_str = "Hello world!"

pb = Pushbullet(API)

push = pb.push_note('This is a test.', test_str)
