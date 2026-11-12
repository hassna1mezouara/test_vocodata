from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Logs():
    def __init__(self,driver):
        self.driver=driver
        self.menu_logs = (By.XPATH, "//a[@href='/admin/logs']")

    

    def naviguer_vers_logs(self):
          wait = WebDriverWait(self.driver, 10) 
          menu=self.menu_logs 
          try:
                element = wait.until(EC.element_to_be_clickable(menu))
                print(f"[INFO] Navigation vers : {element.text}")
                element.click()
                WebDriverWait(self.driver, 5).until(EC.staleness_of(element))  # attendre chargement
          except Exception as e:
                print(f"[ERREUR] Impossible de naviguer vers le menu : {menu} → {e}") 
    def click_exporter(self) :
         btn_export = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Exporter en Excel')]")
         btn_export.click()
         