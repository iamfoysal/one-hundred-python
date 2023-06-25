from plyer import notification
import time

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10 # seconds
    )

def main():

    title = input("Enter the notification title: ")
    message = input("Enter the notification message: ")

    show_notification(title, message)

if __name__ == '__main__':
    main()





