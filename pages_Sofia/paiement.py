from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class Paiment:
    def __init__(self, driver):
        self.driver = driver
        self.paiments = (By.CSS_SELECTOR, "a[routerlink='payment/checkout']")
        self.email = (By.ID, "search-email")
        self.emailll=(By.ID, "email")
        self.info_carte=(By.ID, "cardNumber")
        self.nom_carte=(By.ID, "billingName")

    def navigue_vers_paiment(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            element = wait.until(EC.element_to_be_clickable(self.paiments))
            print(f"[INFO] Navigation vers : {element.text}")
            element.click()
        except Exception as e:
            print(f"[ERREUR] Impossible de naviguer vers le menu : {self.paiments} → {e}")

    def remplir_minutes(self, valeur):
        champ_minutes = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "minutes"))
        )
        champ_minutes.clear()
        champ_minutes.send_keys(str(valeur))
        print("Champ 'Nombre de minutes' rempli avec :", valeur)

    def click_achat(self):
        try:
            self.driver.find_element(By.XPATH, "//button[span[text()=\"Finaliser l'achat\"]]").click()
            print("[OK] Clic sur le bouton 'Finaliser l'achat'.")
        except Exception as e:
            print(f"[ERREUR] Impossible de cliquer sur le bouton achat : {e}")

    def click_payer_par_link(self):
     wait = WebDriverWait(self.driver, 15)
     try:
        time.sleep(1)
        iframe = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "iframe[name^='__privateStripeFrame']"))
        )
        self.driver.switch_to.frame(iframe)
        print("[INFO] Bascule dans l'iframe Stripe réussie.")

        button = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
        button.click()
        print("[OK] Clic sur le bouton de paiement effectué.")

        # Revenir au contenu principal
        self.driver.switch_to.default_content()
        
       
        main_window = self.driver.current_window_handle
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)

        for handle in self.driver.window_handles:
            if handle != main_window:
                self.driver.switch_to.window(handle)
                print("[INFO] Bascule vers la nouvelle fenêtre Stripe.")
                break

     except TimeoutException:
        print("[ERREUR] Timeout : bouton de paiement introuvable.")
     except Exception as e:
        print(f"[ERREUR] Échec lors du clic sur le bouton 'Payer par Link' : {e}")



    def entrer_email(self, email):
     try:
        wait = WebDriverWait(self.driver, 15)
        input_email = wait.until(EC.presence_of_element_located((By.ID, "search-email")))
        input_email.clear()
        input_email.send_keys(email)
        print("[OK] E-mail saisi avec succès.")
     except Exception as e:
        print("[ERREUR] Impossible de remplir le champ email :", str(e))


    def connait_champs(self):
        inputs = self.driver.find_elements(By.TAG_NAME, 'input')
        print(f"[DEBUG] {len(inputs)} champs input trouvés.")
    
        for i, inp in enumerate(inputs, 1):
              try:
                t = inp.get_attribute('type')
                n = inp.get_attribute('name')
                p = inp.get_attribute('placeholder')
                print(f"{i}. type: {t}, name: {n}, placeholder: {p}")
              except:
                 continue     


    def click_bouton_payer(self):
     try:
        wait = WebDriverWait(self.driver, 20)

        # Attendre la présence du bouton dans le DOM
        bouton = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button[data-testid='pay-button']"))
        )

        # Attendre que le bouton soit activé (pas disabled)
        wait.until(lambda d: bouton.is_enabled())

        # Vérifier le texte du bouton pour confirmer le montant
        texte_bouton = bouton.text.strip()
        print(f"[INFO] Texte du bouton trouvé : '{texte_bouton}'")

        if "Payer MAD" in texte_bouton:
            bouton.click()
            print("[OK] Clic sur le bouton 'Payer' effectué.")
        else:
            print(f"[ERREUR] Le texte du bouton ne contient pas le montant attendu : {texte_bouton}")

     except TimeoutException:
        print("[ERREUR] Timeout : le bouton de paiement n'est pas prêt.")
     except Exception as e:
        print(f"[ERREUR] Échec lors du clic sur le bouton de paiement : {e}")


    def fill_form_carte(self,email,info_catre,nom_carte) :
           self.driver.find_element(*self.emailll).send_keys(email)
           self.driver.find_element(*self.info_carte).send_keys(info_catre)
           self.driver.find_element(*self.nom_carte).send_keys(nom_carte)

    def cocher_checkbox(self):
     checkbox_locator = (By.ID, "enableStripePass")
     checkbox = self.driver.find_element(*checkbox_locator)  # Récupérer l'élément web
     if not checkbox.is_selected():
        checkbox.click()     


    def  click_paimet(self)   :
       self.driver.find_element(By.CSS_SELECTOR, "div.SubmitButton-CheckmarkIcon").click()
  