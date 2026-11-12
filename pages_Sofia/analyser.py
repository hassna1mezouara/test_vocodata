from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.support.ui import Select
 
class Analyser ():
    def __init__(self,driver) :
        self.driver=driver
        self.champ_grille=(By.ID, "grille")
        self.analyser=(By.CSS_SELECTOR, "a[routerlink='analyser']")
        
    def naviguer_vers_analyser(self)    :
         wait = WebDriverWait(self.driver, 10) 
         menu=self.analyser 
         try:
                element = wait.until(EC.element_to_be_clickable(menu))
                print(f"[INFO] Navigation vers : {element.text}")
                element.click()
               
         except Exception as e:
                print(f"[ERREUR] Impossible de naviguer vers le menu : {menu} → {e}") 


    def select_grille(self, valeur='Telecom'):
        wait = WebDriverWait(self.driver, 10)
    
    # Attendre que le select soit présent dans le DOM
        select_element = wait.until(EC.presence_of_element_located((By.ID, "grille")))
    
    # Créer un objet Select et choisir l'option par texte visible
        select = Select(select_element)
        select.select_by_visible_text(valeur)
       
        print(f"La grille '{valeur}' a été sélectionnée.")

    def click_select_fichier(self,file_path):
         self.driver.find_element(By.ID, "enregistrement").send_keys(file_path)
        

    def click_sur_analyser(self)   :
        self.driver.find_element(By.XPATH, "//button[span[text()='Analyser']]").click()
        
    def click_ok(self)   :
        self.driver.find_element(By.CSS_SELECTOR, "button.swal2-confirm.swal2-styled").click()    