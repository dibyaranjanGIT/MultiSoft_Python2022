import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title="**Please Drink Water Now!!",
            message="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
            app_icon="path to your .ico file",
            timeout=12
        )
        #time.sleep(6)
        time.sleep(60 * 60)

# To run a programm in the backgroud use the below command

# pythonw jiban.py # you have to kill the process from task bar once you started it.