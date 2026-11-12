from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Utilisateur():
    def __init__(self,driver):
        self.driver = driver
        self.menu_utilisateurs = (By.XPATH, "//a[@href='/admin/users']")
        self.ajouter=(By.XPATH, "//button[contains(text(), 'Ajouter un utilisateur')]")
        self.nom=(By.CSS_SELECTOR, 'input[formcontrolname="nom"]')
        self.prenom=(By.CSS_SELECTOR, 'input[formcontrolname="prenom"]')   
        self.email=(By.CSS_SELECTOR, 'input[formcontrolname="email"]')
        self.telephone=(By.CSS_SELECTOR, 'input[formcontrolname="phone"]')
        self.role=(By.CSS_SELECTOR, 'input[formcontrolname="role"]')
        self.mot_de_passe=(By.CSS_SELECTOR, 'input[formcontrolname="password"]')
        #boutons
        self.fermer=(By.XPATH, '//button[@data-bs-dismiss="modal"]')
        self.ajout=(By.XPATH, '//form//button[@type="submit" and contains(text(), "Ajouter")]')
        self.modifier_buttons = driver.find_elements(By.XPATH, "//a[i[contains(@class, 'fa-user-pen')]]")
 
               
    def navigue_vers_utilisateur(self)  :
      wait = WebDriverWait(self.driver, 10) 
      menu=self.menu_utilisateurs
      try:
                element = wait.until(EC.element_to_be_clickable(menu))
                print(f"[INFO] Navigation vers : {element.text}")
                element.click()
                WebDriverWait(self.driver, 5).until(EC.staleness_of(element))  # attendre chargement
      except Exception as e:
                print(f"[ERREUR] Impossible de naviguer vers le menu : {menu} → {e}") 

    def fill_form_utilisateur(self, nom, prenom, email, tel, role, pwd )  :
        self.driver.find_element(*self.nom).send_keys(nom)
        self.driver.find_element(*self.prenom).send_keys(prenom)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.telephone).send_keys(tel)
        self.driver.find_element(*self.role).send_keys(role)
        self.driver.find_element(*self.mot_de_passe).send_keys(pwd)
  
                  
    def click_ajouter(self):
          self.driver.find_element(*self.ajouter).click()
          
    def click_ajout (self) :
          self.driver.find_element(*self.ajout).click()  
    def click_fermer(self)   :
          self.driver.find_element(*self.fermer).click ()
    def cliquer_bouton_modifier(self, email):
             xpath = f"//td[text()='{email}']/following-sibling::td/a[contains(@href, '/edit')]"
             self.driver.find_element(By.XPATH, xpath).click()
      #     WebDriverWait( timeout).until(
      #       EC.presence_of_element_located((By.XPATH, "//a[i[contains(@class, 'fa-user-pen')]]"))
      #   )
        
      #   # Récupérer tous les boutons correspondants
      #     boutons = (By.XPATH, "//a[i[contains(@class, 'fa-user-pen')]]")
        
      #     if boutons:
      #       boutons[8].click()
      #       print("Premier bouton 'Modifier' cliqué avec succès.")
      #     else:
      #       print("Aucun bouton 'Modifier' trouvé.")
    
      # except Exception as e:
      #   print(f"Erreur lors du clic sur le bouton 'Modifier' : {e}")

    def fill_information_modifier(self, nom, prenom, email, tel, role):
        print("jjsjjsjsjjs")
        self.driver.find_element(*self.nom).clear()
        self.driver.find_element(*self.nom).send_keys(nom)

        self.driver.find_element(*self.prenom).clear()
        self.driver.find_element(*self.prenom).send_keys(prenom)

        self.driver.find_element(*self.email).clear()
        self.driver.find_element(*self.email).send_keys(email)

        self.driver.find_element(*self.telephone).clear()
        self.driver.find_element(*self.telephone).send_keys(tel)

        self.driver.find_element(*self.role).clear()
        self.driver.find_element(*self.role).send_keys(role)

    def click_chek(self)  :
          self.driver.find_element(By.XPATH, "//input[@type='checkbox' and @formcontrolname='enabled']").click()
        
    def click_editer(self)  :
          self.driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Modifier')]").click()
    
    def click_supprimer(self, email):
    # Localise la ligne avec l’e-mail
           xpath_ligne = f"//td[text()='{email}']/parent::tr"
           ligne = self.driver.find_element(By.XPATH, xpath_ligne)
               # Cherche le 2e bouton <a> (le bouton supprimer) dans cette ligne
           bouton_supprimer = ligne.find_elements(By.XPATH, ".//a")[1]  # index 1 → deuxième bouton
           bouton_supprimer.click()

    def click_annuler(self):
          self.driver.find_element(By.XPATH, "//button[normalize-space()='Annuler']") .click()  
          print("hhhhh")

    def clcik__delete(self):
          self.driver.find_element(By.XPATH, "//button[normalize-space()='Oui, supprimez-le !']").click()
                
    def click_ok(self)   :
        self.driver.find_element(By.CSS_SELECTOR, "button.swal2-confirm.swal2-styled").click()          

             

