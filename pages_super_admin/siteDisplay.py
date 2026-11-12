from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Display:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)
        self.solution_locator = (By.XPATH, "//a[contains(text(),'Solution')]")
        self.features_locator = (By.CSS_SELECTOR, "a.dropdown-item[href='#features']")
        self.how_it_works_locator = (By.CSS_SELECTOR, "a.dropdown-item[href='#how-it-works']")
        self.tarif_locator = (By.CSS_SELECTOR, "a.nav-item.nav-link[href='#pricing']")
        self.contact_locator = (By.CSS_SELECTOR, "a.nav-item.nav-link[href='#contact']")
        self.inscription_locator = (By.CSS_SELECTOR, "a.nav-item.nav-link[href='/auth/register']")
        #self.login_locator = (By.CSS_SELECTOR, 'a[href="/auth/login"]')

    def click_solution(self):
        """Clique sur 'Solution' pour ouvrir le menu déroulant"""
        solution_button = self.wait.until(EC.element_to_be_clickable(self.solution_locator))
        solution_button.click()

    def click_and_display_section(self, locator, section_name):
        """Clique sur une section du menu déroulant et affiche son contenu"""
        try:
            # Clique sur l'élément du menu
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            print(f"Clicked on: {section_name}")

            # Extraire l'ID de la section à partir du locator
            section_id = locator[1].split('#')[-1]
            section_content_locator = (By.ID, section_id)

            # Attendre que l'élément soit dans le DOM
            self.wait.until(EC.presence_of_element_located(section_content_locator))
            content = self.driver.find_element(*section_content_locator)

            # Scroll jusqu'à la section pour la rendre visible
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", content)

            # Attendre que la section soit visible
            self.wait.until(EC.visibility_of(content))
            print(f"Content of {section_name}:\n{content.text}\n")

        except TimeoutException:
            print(f"Timeout lors de l'affichage de la section {section_name}")
        except Exception as e:
            print(f"Erreur lors de l'affichage de la section {section_name}: {e}")

    
