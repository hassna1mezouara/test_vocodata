from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class List_noir ():
    def __init__(self,driver):
        self.driver=driver
        self.input_mot = (By.ID, "mot")
        self.liste_noir=(By.CSS_SELECTOR, "a[routerlink='blacklist']")
        self.input_competence = (By.ID, "nom")


    def navigue_vers_list_noir(self):
        
      wait = WebDriverWait(self.driver, 10) 
      menu=self.liste_noir 
      try:
                element = wait.until(EC.element_to_be_clickable(menu))
                print(f"[INFO] Navigation vers : {element.text}")
                element.click()
                WebDriverWait(self.driver, 5).until(EC.staleness_of(element))  # attendre chargement
      except Exception as e:
                print(f"[ERREUR] Impossible de naviguer vers le menu : {menu} → {e}") 
    
    def click_ajouter_un_mot( self):
          self. driver.find_element(By.XPATH, "//button[contains(text(), 'Ajouter un Mot')]").click()
    
    def fill_form_mot(self,nom):
          self.driver.find_element(*self.input_mot).send_keys(nom)

    def click_confirmer_ajout(self) :
        self. driver.find_element(By.XPATH, "//button[text()='Ajouter' and @type='submit']") .click()

    def click_annuler_ajout(self):
          self.driver.find_element(By.XPATH, "//button[@data-bs-dismiss='modal' and contains(@class, 'btn-close')]").click()
    
    def modifier_mot(self,mot):
          
         xpath = f"//tr[td[text()='{mot}']]//a[contains(@href, '/edit')]"
         modifier_btn = self.driver.find_element(By.XPATH, xpath)
         modifier_btn.click()
         
    def fill_mot(self,mot) :
          self.driver.find_element(*self.input_mot).clear()
          self.driver.find_element(*self.input_mot).send_keys(mot)   

    def click_ok(self)   :
        self.driver.find_element(By.CSS_SELECTOR, "button.swal2-confirm.swal2-styled").click()           