#Environment este un fisier prin intermediul caruia putem sa definim actiuni care
# sa fie executate inainte de fiecare test si respectiv dupa fiecare test.

#Metoda before_all, ce va fi executata inainte de fiecare test, creaza instanta de driver.
#Metoda after all, ce va fi executata dupa fiecare test, inchide instanta de driver.

from browser import Browser
from pages.register_page import RegisterPage


def before_all(context):
    context.driver = Browser()
    context.register_page_object = RegisterPage()


def after_all(context):
    context.driver.close()
