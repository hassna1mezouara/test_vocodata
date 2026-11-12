from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import os

from all_tests.sofia_test import (  # remplace ce nom par celui de ton module
    test_login_Sofia,
    test_ajouter_grilles,
    test_ajouter_competence,
    test_modifier_valider_grille,
    test_supprimer_grille,
    test_ajouter_mot_list_noir,
    test_ajouter_mot_list_noir_existe,
    test_modifier_mot,
    test_supprimer_mot,
    test_paiement_link,
    test_paiement_carte,
)

def run_all_tests():
    # 1. Spécifie le chemin local vers chromedriver.exe
    driver_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'drivers', 'chromedriver.exe'))
    service = ChromeService(driver_path)

    # 2. Lance Chrome
    driver = webdriver.Chrome(service=service)
    driver.set_page_load_timeout(180)
    driver.maximize_window()

    try:
        # 3. Appelle chaque test avec le même driver
        test_login_Sofia(driver)
        test_ajouter_grilles(driver)
        test_ajouter_competence(driver)
        test_modifier_valider_grille(driver)
        test_supprimer_grille(driver)
        test_ajouter_mot_list_noir(driver)
        test_ajouter_mot_list_noir_existe(driver)
        test_modifier_mot(driver)
        test_supprimer_mot(driver)
        test_paiement_link(driver)
        test_paiement_carte(driver)

    except Exception as e:
        print(f"Erreur inattendue : {e}")
    finally:
        # 4. Ferme le navigateur à la fin
        driver.quit()
        print("Tous les tests ont été exécutés. Le navigateur a été fermé.")

if __name__ == "__main__":
    run_all_tests()
