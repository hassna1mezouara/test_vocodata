from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class Grilles ():
    def __init__(self,driver):
        self.driver=driver
        self.input_nom = (By.ID, "nom")
        self.menu_grilles = (By.XPATH, "//a[@href='/admin/grilles']")
        self.input_competence = (By.ID, "nom")


    def navigue_vers_grilles(self):
        
      wait = WebDriverWait(self.driver, 10) 
      menu=self.menu_grilles 
      try:
                element = wait.until(EC.element_to_be_clickable(menu))
                print(f"[INFO] Navigation vers : {element.text}")
                element.click()
                WebDriverWait(self.driver, 5).until(EC.staleness_of(element))  # attendre chargement
      except Exception as e:
                print(f"[ERREUR] Impossible de naviguer vers le menu : {menu} → {e}") 

    def click_ajouter_grilles(self)  :
       self.driver.find_element(By.XPATH, "//button[contains(text(), 'Ajouter une grille')]").click() 

    def fill_grill(self,nom):
        self.driver.find_element(*self.input_nom).send_keys(nom)

    def click_ajouter(self)   :
         self.driver.find_element(By.XPATH, "//button[text()='Ajouter']").click() 

    def click_close(self):
        self.driver.find_element(By.XPATH, "//button[text()='Close']").click()

    def click_croix(self) :
        self. driver.find_element(By.CLASS_NAME, "btn-close") .click()  
    def a_competence(self, nom_grille):
     try:
        # Localiser la ligne correspondant au nom de la grille
        row_xpath = f"//table//tr[td[1][text()='{nom_grille}']]"
        row = self.driver.find_element(By.XPATH, row_xpath)

        # Trouver le bouton avec la classe FontAwesome dans cette ligne
        button = row.find_element(By.CLASS_NAME, "fa-arrow-up-right-from-square")
        button.click()

     except Exception as e:
        print(f"Erreur : {e}")
        return None
    def ajouter_competence(self):
        self.driver.find_element(By.XPATH, "//button[@data-bs-target='#exampleModal' and contains(., 'Ajouter une compétence')]").click()

    def  click_ajo_com(self):
         self.driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Ajouter')]").click()

    def click_annuler(self)  :
        self.driver.find_element(By.XPATH, "//button[@data-bs-dismiss='modal' and contains(text(), 'Close')]").click()

    ###############pour modifier et valider : 
    def modifier_grille(self):
        rows = self.driver.find_elements(By.XPATH, '//table/tbody/tr')
        for row in rows:
          grid_name = row.find_element(By.XPATH, './td[1]').text.strip().lower()
          if grid_name == 'testt':
             edit_button = row.find_element(By.XPATH, './/a[contains(@href, "/edit")]')
             edit_button.click()
             break          
    def click_chek(self)  :
          checkbox = self.driver.find_element(By.XPATH, '//input[@type="checkbox" and @formcontrolname="validated"]')
          if not checkbox.is_selected():
               checkbox.click()
    def click_modifierr(self):
         self.driver.find_element(By.XPATH, '//button[text()="Modifier"]').click()    

    ####################SUpprimer un grille###########
    # def supprimer_grille(self):
    #     rows = self.driver.find_elements(By.XPATH, "//table/tbody/tr[td[1][normalize-space()='test']]")
    #     for row in rows:
    #           row.find_element(By.XPATH, ".//a[contains(@class,'btn-outline-danger')]").click()

    def supprimer_grille(self, nom):
     try: 
        xpath_ligne = f"//tr[td[normalize-space(text())='{nom}']]"
        ligne = self.driver.find_element(By.XPATH, xpath_ligne)
        bouton_supprimer = ligne.find_element(By.XPATH, ".//a[contains(@class, 'btn-outline-danger')]")
        bouton_supprimer.click()
        print(f"[OK] Suppression lancée pour la grille : {nom}")
     except Exception as e:
        print(f"[ERREUR] Impossible de supprimer la grille '{nom}' : {e}")       

    def click_annulerr(self):
          self.driver.find_element(By.XPATH, "//button[text()='Annuler']") .click()  
          print("hhhhh")

    def clcik__deletee(self):
          self.driver.find_element(By.XPATH, "//button[text()='Oui, supprimez-le !']").click()
                
    def click_ok(self)   :
        self.driver.find_element(By.CSS_SELECTOR, "button.swal2-confirm.swal2-styled").click()         
                   