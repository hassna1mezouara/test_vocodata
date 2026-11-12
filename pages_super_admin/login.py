from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
class Login:
    def __init__(self,driver):
        self.driver = driver
        self.email=(By.ID,"email")
        self.mot_de_passe=(By.ID,"password")
        self.connexion= (By.XPATH, "//button[text()='Connexion']")
        self.locator_mdp_oublie = (By.XPATH, "//a[@href='/auth/password/forgot']/small[text()='Mot de passe oublié?']")
        self.locator_cree=(By.LINK_TEXT, "Créer un compte")
        self.menu_dashboard = (By.XPATH, "//a[@href='/admin/dashboard']")
        self.menu_grilles = (By.XPATH, "//a[@href='/admin/grilles']")
        self.menu_utilisateurs = (By.XPATH, "//a[@href='/admin/users']")
        self.menu_entreprises = (By.XPATH, "//a[@href='/admin/companies']")
        self.menu_transactions = (By.XPATH, "//a[@href='/admin/transactions']")
        self.menu_logs = (By.XPATH, "//a[@href='/admin/logs']")

    def fill_form_connexion(self, email , pwd):
          wait = WebDriverWait(self.driver, 10)

          email_input = wait.until(EC.visibility_of_element_located((By.ID, "email")))
          password_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))

          email_input.send_keys(email)
          password_input.send_keys(pwd)
          #self.driver.find_element(*self.email).send_keys(email)
          #self.driver.find_element(*self.password).send_keys(pwd)

    def click_connexion (self):
       wait = WebDriverWait(self.driver, 10)
       wait.until(lambda driver: self.driver.find_element(*self.connexion).is_enabled())
       self.driver.find_element(*self.connexion).click()

    def click_mot_de_passe_oublier(self):
         self.driver.find_element(*self.locator_mdp_oublie).click()

    def fill_form_connexion_oublier(self, email ):
          wait = WebDriverWait(self.driver, 10)
          email_input = wait.until(EC.visibility_of_element_located((By.ID, "email")))
          email_input.send_keys(email)     
    
    def click_creer(self):
         self.driver.find_element(*self.locator_cree).click()


    def naviguer_dans_menus(self):
        menus = [
            self.menu_dashboard,
            self.menu_grilles,
            self.menu_utilisateurs,
            self.menu_entreprises,
            self.menu_transactions,
            self.menu_logs
                              ]

        wait = WebDriverWait(self.driver, 10)

        for menu in menus:
            try:
                element = wait.until(EC.element_to_be_clickable(menu))
                print(f"[INFO] Navigation vers : {element.text}")
                element.click()
                WebDriverWait(self.driver, 5).until(EC.staleness_of(element))  # attendre chargement
            except Exception as e:
                print(f"[ERREUR] Impossible de naviguer vers le menu : {menu} → {e}")
    def click_renitialise(self)  :
         btn_envoyer = self.driver.find_element(By.XPATH, "//button[text()='Envoyer le lien de réinitialisation']")
         btn_envoyer.click()   
    def click_retour(self)   :
         lien_retour = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Retour à la page de connexion')]")
         lien_retour.click()                      