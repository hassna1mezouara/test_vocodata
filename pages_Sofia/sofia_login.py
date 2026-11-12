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

        self.menu_dashboard = (By.XPATH, "//a[@href='/admin/dashboard']")
        self.analyser=(By.CSS_SELECTOR, "a[routerlink='analyser']")
        self.menu_grilles = (By.XPATH, "//a[@href='/admin/grilles']")
        self.enregistrement=(By.CSS_SELECTOR, "a[routerlink='enregistrements']")
        self.liste_noir=(By.CSS_SELECTOR, "a[routerlink='blacklist']")
        self.menu_utilisateurs = (By.XPATH, "//a[@href='/admin/users']")
        self.paiments=(By.CSS_SELECTOR, "a[routerlink='payment/checkout']")
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

       
    

    def naviguer_dans_menus(self):
        menus = [
            self.menu_dashboard,
            self.analyser,
            self.menu_grilles,
            self.enregistrement,
            self.liste_noir,
            self.menu_utilisateurs,
            self.paiments,
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
  