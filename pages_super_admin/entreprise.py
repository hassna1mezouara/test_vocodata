from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Entreprise():
    def __init__(self,driver):
        self.driver=driver
        self.menu_entreprises = (By.XPATH, "//a[@href='/admin/companies']")
        self.company=(By.ID,"name")
        self.company_ice=(By.ID,"ice")
        self.company_address=(By.ID,"company_address")
        #self.company_logo=(By.ID,"company_logo")
        self.input_logo = (By.ID, "company_logo")


    def naviguer_vers_entreprise(self):
          wait = WebDriverWait(self.driver, 10) 
          menu=   self.menu_entreprises
          try:
                element = wait.until(EC.element_to_be_clickable(menu))
                print("succes navigation")
                element.click()
                WebDriverWait(self.driver, 5).until(EC.staleness_of(element))  # attendre chargement
          except Exception as e:
                print(f"[ERREUR] Impossible de naviguer vers le menu : {menu} → {e}")   


   


    def cl_modifier(self, name_entreprise):
      wait = WebDriverWait(self.driver, 15)
    
      rows = self.driver.find_elements(By.CSS_SELECTOR, "tbody tr")
      for row in rows:
        if name_entreprise.lower() in row.text.lower():
            try:
                modifier_btn = row.find_element(By.CSS_SELECTOR, "a.btn-outline-success[href*='/edit']")

                # S'assurer que le bouton est visible et cliquable
                wait.until(EC.element_to_be_clickable(modifier_btn))

                # Scroll pour que le bouton soit dans le champ de vision
                self.driver.execute_script("arguments[0].scrollIntoView(true);", modifier_btn)
                
                # Pause légère pour la stabilité
                import time
                time.sleep(1)

                # Clic sur le bouton
                modifier_btn.click()
                break
            except Exception as e:
                print(f"[ERREUR] Impossible de cliquer sur le bouton modifier : {e}")
                break


#     def cl_modifier(self,name_entreprise):

#            rows = self.driver.find_elements(By.CSS_SELECTOR, "tbody tr")
#            for row in rows:
#               if name_entreprise.lower() in row.text.lower():
#                   modifier_btn = row.find_element(By.CSS_SELECTOR, "a.btn-outline-success[href*='/edit']")
#                   modifier_btn.click()
#                   break              
    
    def fill_form_entreprise(self,company,company_ice,company_address,logo_path):
        self.driver.find_element(*self.company).clear()
        self.driver.find_element(*self.company).send_keys(company)

        self.driver.find_element(*self.company_ice).clear()
        self.driver.find_element(*self.company_ice).send_keys(company_ice)
        
        self.driver.find_element(*self.company_address).clear()
        self.driver.find_element(*self.company_address).send_keys(company_address)
        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(self.input_logo)
 ).send_keys(logo_path)


    def click_chek(self)  :
          checkbox = self.driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="valide"]')
          if not checkbox.is_selected():
             checkbox.click()
        
    def click_editer(self)  :
          
          bouton_modifier = self.driver.find_element(By.XPATH, '//button[text()="Modifier"]')
          bouton_modifier.click()
    
    def cl_supprimer(self, nom_entreprise):
     wait = WebDriverWait(self.driver, 10)  # attendre jusqu'à 10 secondes

    # Attendre que le tableau soit présent
     wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'table tbody tr')))

     rows = self.driver.find_elements(By.CSS_SELECTOR, 'table tbody tr')
     for row in rows:
        nom = row.find_element(By.TAG_NAME, 'td').text.strip().lower()
        if nom == nom_entreprise.lower():
            # Attendre que le bouton soit cliquable avant de cliquer
            bouton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-outline-danger')))
            bouton.click()
            break



    def oui_supr(self):
          bouton_oui = self.driver.find_element(By.CSS_SELECTOR, "button.swal2-confirm")
          bouton_oui.click()
    def annuler_supr(self) :
              bouton_annuler = self.driver.find_element(By.CSS_SELECTOR, "button.swal2-cancel")
              bouton_annuler.click()
              print("yeeeeeeeeeeeeeeeeees")

    def click_ok(self)   :
        self.driver.find_element(By.CSS_SELECTOR, "button.swal2-confirm.swal2-styled").click()               