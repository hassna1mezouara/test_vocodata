from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Enregistrement ():
    def __init__(self,driver):
        self.driver=driver
        self.menu_enregistrement=(By.XPATH, '//span[text()="Enregistrements"]')





    def navigue_vers_enregistremet(self)   :
         wait = WebDriverWait(self.driver, 10) 
         menu=   self.menu_enregistrement
         try:
                element = wait.until(EC.element_to_be_clickable(menu))
                print("succes navigation")
                element.click()
                WebDriverWait(self.driver, 5).until(EC.staleness_of(element))  # attendre chargement
         except Exception as e:
                print(f"[ERREUR] Impossible de naviguer vers le menu : {menu} → {e}")  

    def click_details(self):
        self.driver.find_element(By.CSS_SELECTOR, 'a[href^="/admin/enregistrements/"]').click()

    def telcharger_par_click(self):
         self.driver.find_element(By.CSS_SELECTOR, 'a[href$=".xlsx"]').click()
         
    def telecharger(self):
         self.driver.find_element(By.CSS_SELECTOR, 'a[href$=".pdf"]').click()

    def supprimer (self):
         self.driver.find_element(By.CSS_SELECTOR, 'button .fa-trash').click()
                   
                          

        