#Browser/Driver este un fisier care va contine instantierea driverului pentru browserul folosit in scopul testarii.
#Clasa Driver instantatiaza un driver de Chrome cu fereastra maximizata ce va astepta 2 secunde (incarcarea elementelor
# de pe pagina) si continue o metoda (close_driver) care la apelare ne va inchide driverul dupa finalizarea operatiilor necesare.
import unittest

from selenium import webdriver


class Browser(unittest.TestCase):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.delete_all_cookies()

    def close(self):
        self.driver.quit()
