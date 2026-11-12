from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10 )
        self.nom = (By.ID, "nom")     
        self.prenom = (By.ID, "prenom")  
        self.email = (By.ID, "email")
        self.telephone = (By.ID, "phone")
        self.password = (By.ID, "password")
        self.confirm_password = (By.ID, "confirmPassword")
        self.submit_button = (By.XPATH, "//button[.//span[contains(text(), 'Suivant')]]")  # Tuple avec By.XPATH et XPath
        self.company=(By.ID,"company_name")
        self.company_ice=(By.ID,"company_ice")
        self.company_address=(By.ID,"company_address")
        self.company_logo=(By.ID,"company_logo")
        self.final_button=(By.XPATH, "//button[.//span[contains(normalize-space(), \"S'inscrire\")]]")
        

    def fill_form(self, nom, prenom, email, tel, pwd, confirm_pwd):
        self.driver.find_element(*self.nom).send_keys(nom)
        self.driver.find_element(*self.prenom).send_keys(prenom)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.telephone).send_keys(tel)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.confirm_password).send_keys(confirm_pwd)

    def click_suivant(self):
         wait = WebDriverWait(self.driver, 10)

    # Attente jusqu'à ce que le bouton ne soit plus désactivé
         wait.until(lambda driver: self.driver.find_element(*self.submit_button).is_enabled())

         self.driver.find_element(*self.submit_button).click()
 

    def fill_second_step (self,company,company_ice,company_address,logo_path):
        self.driver.find_element(*self.company).send_keys(company)
        self.driver.find_element(*self.company_ice).send_keys(company_ice)
        self.driver.find_element(*self.company_address).send_keys(company_address)
        #self.driver.find_element(*self.company_logo).send_keys(logo_path)
        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(self.company_logo)
 ).send_keys(logo_path)
    #     WebDriverWait(self.driver, 10).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-next"))
    # )



    def click_valider(self) :
      self.driver.find_element(*self.final_button).click()

# / def click_suivant(self):
    # attendre que le bouton ne soit plus désactivé et cliquable
        #    WebDriverWait(self.driver, 15).until(
      #    EC.element_to_be_clickable( self.submit_button )).click()


