from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages_Sofia.sofia_login import Login
from pages_Sofia.grilles import Grilles
from pages_Sofia.list_noir import List_noir
from pages_Sofia.paiement import Paiment
from pages_Sofia.analyser import Analyser
from pages_super_admin.utilisateur import Utilisateur
from pages_Sofia.enregistremet import Enregistrement


from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import openpyxl
import traceback
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#################################################################FONCTION POUR RECUPERER LES DONNEES ET CONNECTER A EXEL###################################

logo_path = r"C:\Users\pc\AppData\Roaming\Microsoft\Windows\Network Shortcuts\test_automatisation2\test\image.png"
excel_path = os.path.abspath(r"C:\Users\pc\Downloads\data_exel3.xlsx")

def extract_and_validate_placeholders(driver, sheet, champs_locators):
    for row, (by, locator) in champs_locators.items():
        try:
            # Attendre que l'élément soit présent et visible
            champ_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((by, locator))
            )
            
            # Extraire le texte affiché
            label_text = champ_element.text.strip()
            print(label_text)

            # Écrire le texte dans colonne E
            sheet[f"E{row}"] = label_text
            print(f"[OK] Texte extrait pour ligne {row} : '{label_text}'")
            
            # Lire la valeur attendue depuis Excel (colonne F)
            valeur_attendue = safe_value(sheet[f"F{row}"].value)
            print(valeur_attendue)

            # Comparer
            if label_text.lower() == valeur_attendue.lower():
                sheet[f"G{row}"] = "ok"
                print(f"[VALIDATION OK] E{row} == F{row}")
            else:
                sheet[f"G{row}"] = "ko"
                print(f"[VALIDATION KO] E{row} != F{row}")

        except Exception as e:
            sheet[f"E{row}"] = "Erreur extraction"
            sheet[f"G{row}"] = "ko"
            print(f"[Erreur] Ligne {row} : {e}")

def get_sheet():
    workbook = openpyxl.load_workbook(excel_path)
    sheet = workbook.active
    return workbook, sheet

def safe_value(cell_value):
    return cell_value if cell_value is not None else ""

def login_once(driver, sheet):
    url = sheet["C106"].value
    driver.get(url)
    log = Login(driver)
    email = safe_value(sheet["C107"].value)
    pwd = safe_value(sheet["C108"].value)
    log.fill_form_connexion(email, pwd)
    log.click_connexion()
    time.sleep(2)

################## login
def test_login(setup):
    driver=setup
    workbook, sheet = get_sheet()
    login_once(driver, sheet)

##################################login with the sofia#######################3
def test_llogin_Sofia(setup: WebDriver):
     driver = setup
     workbook, sheet = get_sheet()
     log = Login(driver) 
     try:
        
       
         champs_locators = {
    107: (By.CSS_SELECTOR, 'h5.card-title.text-primary'),  
    108: (By.CSS_SELECTOR, 'p.mb-4'),
    109: (By.XPATH, '//span[text()="Tableau de bord"]'),
    110: (By.XPATH, '//span[contains(text(), "Grilles")]'),
    111: (By.XPATH, '//span[text()="Utilisateurs"]'),
    113: (By.XPATH, '//span[text()="Transactions"]'),
    114: (By.XPATH, '//span[text()="Logs"]'),
    115: (By.XPATH, '//span[text()="Analyser"]'),
    116: (By.XPATH, '//span[text()="Enregistrements"]'),
    117: (By.XPATH, '//span[text()="Liste Noire"]'),
    118: (By.XPATH, '//span[text()="Paiement"]')
}

         time.sleep(2)
         extract_and_validate_placeholders(driver, sheet, champs_locators)
         log.naviguer_dans_menus()
         time.sleep(2)
         
     except:
         print("error")
     try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
     except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")

        workbook.close() 

############################################# test_page de grilles##########
def test_ajouter_grilles(setup: WebDriver):
     driver = setup
     workbook, sheet = get_sheet()
     grilles=Grilles(driver)
     try:
        
         nom=safe_value(sheet["C121"].value)
         champs_locators={
                          120:((By.XPATH, "//h1[text()='Ajouter une grille']")),
                          121:((By.XPATH, "//label[contains(text(), 'Nom')]"))

         }
         grilles.navigue_vers_grilles()
         grilles.click_ajouter_grilles()
         extract_and_validate_placeholders(driver,sheet,champs_locators)
         grilles.fill_grill(nom)
         time.sleep(2)
         grilles.click_ajouter()
         time.sleep(3)
     except:
         print("error")
     try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
     except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")

        workbook.close() 

# ###################3 ajouter une competence###################   
def test_ajouter_competence(setup: WebDriver):
     driver = setup
     workbook, sheet = get_sheet()
     grilles=Grilles(driver)
     try:
         com=safe_value(sheet["C123"].value)
         champs_locators={
                          123:((By.ID, "exampleModalLabel")),
                          124:((By.XPATH, "//label[@for='nom']"))

         }
         grilles.navigue_vers_grilles()
         grilles.a_competence('testt')
         time.sleep(2)
         grilles.ajouter_competence()
         time.sleep(2)
         grilles.fill_grill(com)
         time.sleep(3)
         extract_and_validate_placeholders(driver,sheet,champs_locators)
         grilles.click_ajo_com()
         time.sleep(3)
     except:
         print("error")
     try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
     except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")

        workbook.close() 

###################################modifier et valider une grille:###
def test_modifier_valider_grille(setup: WebDriver):
      driver=setup
      workbook, sheet = get_sheet()
      grilles=Grilles(driver)
      try:
        
         champs_locators={126:((By.XPATH, '//h5[text()="Modifier Grille"]')),
                          127:((By.XPATH, "//label[@for='uuid']")),
                          128:((By.XPATH, "//label[@for='nom']"))}
         grilles.navigue_vers_grilles()
         grilles.modifier_grille()
         time.sleep(2)
         grilles.click_chek()
         time.sleep(3)
         extract_and_validate_placeholders(driver,sheet,champs_locators)
         time.sleep(3)
         grilles.click_modifierr()
         time.sleep(2)
         grilles.click_ok()
        

      except:
         print("error")
      try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
      except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")

        workbook.close() 

##########################supprimer un grillle #######
def test_supprimer_grille(setup: WebDriver):
      driver=setup
      workbook, sheet = get_sheet()
   
      grilles=Grilles(driver)
      try:
        
        
         champs_locators={ 130:((By.ID, "swal2-title")),
                          131:((By.ID, "swal2-html-container"))}
            
         grilles.navigue_vers_grilles()
         grilles.supprimer_grille('testt')
         extract_and_validate_placeholders(driver,sheet,champs_locators)
         time.sleep(2)
         grilles.clcik__deletee()
         time.sleep(3)
         grilles.click_ok()
         
      
      except Exception as e:
           print("Une erreur est survenue :", str(e))
           traceback.print_exc()
      try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
      except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")

        workbook.close() 

#################################### ajouter un mot dans la liste noir
def test_ajouter_mot_list_noir(setup: WebDriver):
     driver = setup
     workbook, sheet = get_sheet()
     
     list_noir=List_noir(driver)

     try:
        
         
         champs_locators={
                          133:((By.XPATH, "//h1[contains(text(), 'Ajouter un Mot')]")),
                          134:((By.XPATH, "//label[text()='Mot']"))

         }
         list_noir.navigue_vers_list_noir()
         
         list_noir.click_ajouter_un_mot()
         time.sleep(3)
         list_noir.fill_form_mot("deadline de rapport")
         time.sleep(3)
         extract_and_validate_placeholders(driver,sheet,champs_locators)
         list_noir.click_confirmer_ajout()
         time.sleep(3)
         champs={135:(By.ID, "swal2-title"),
                        136:(By.ID, "swal2-html-container")}
         extract_and_validate_placeholders(driver,sheet,champs)
         time.sleep(3)
         list_noir.click_ok()
     except:
         print("error")
     try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
     except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")

        workbook.close() 


############### ajouter avec meme donnes 
def test_ajouter_mot_list_noir_existe(setup: WebDriver):
     driver = setup
     workbook, sheet = get_sheet()
     list_noir=List_noir(driver)

     try:
         
         
         champs_locators={
                          138:((By.XPATH, "//h1[contains(text(), 'Ajouter un Mot')]")),
                          139:((By.XPATH, "//label[text()='Mot']"))

         }
         list_noir.navigue_vers_list_noir()
         
         list_noir.click_ajouter_un_mot()
         time.sleep(3)
         list_noir.fill_form_mot("deadline de rapport")
         time.sleep(3)
         extract_and_validate_placeholders(driver,sheet,champs_locators)
         list_noir.click_confirmer_ajout()
         time.sleep(3)
         champs={140:(By.ID, "swal2-title"),
                        141:(By.ID, "swal2-html-container")}
         extract_and_validate_placeholders(driver,sheet,champs)
         time.sleep(3)
         list_noir.click_ok()
     except:
         print("error")
     try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
     except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")

        workbook.close() 








###################### modifier le mot 
def test_modifier_mot(setup: WebDriver):
      driver=setup
      workbook, sheet = get_sheet()
     
     
      grilles=Grilles(driver)
      list_noir=List_noir(driver)
      try:
         
         champs_locators={143:((By.XPATH, '//h5[text()="Modifier Grille"]')),
                          144:((By.XPATH, "//label[@for='uuid']")),
                          145:((By.XPATH, "//label[@for='mot']"))}
         list_noir.navigue_vers_list_noir()
         list_noir.modifier_mot("deadline de rapport")
         time.sleep(2)
         list_noir.fill_mot("deadline de rapport")
         time.sleep(3)
         extract_and_validate_placeholders(driver,sheet,champs_locators)
         grilles.click_modifierr()
         time.sleep(2)
         grilles.click_ok()
      except:
         print("error")
      try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
      except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")

        workbook.close() 

################################### supprimer le mot ######
def test_supprimer_mot(setup: WebDriver):
      driver=setup
      workbook, sheet = get_sheet()
      
       
      grilles=Grilles(driver)
      list_noir=List_noir(driver)

      try:
         
         champs_locators={ 147:((By.ID, "swal2-title")),
                          148:((By.ID, "swal2-html-container"))}
         list_noir.navigue_vers_list_noir()   
         grilles.supprimer_grille('deadline de rapport')
         extract_and_validate_placeholders(driver,sheet,champs_locators)
         time.sleep(2)
         grilles.clcik__deletee()
         time.sleep(3)
         grilles.click_ok()
      
      except Exception as e:
           print("Une erreur est survenue :", str(e))
           traceback.print_exc()
      try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
      except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")

        workbook.close() 
######################################### test de paiment ####
def test_paiement_link(setup: WebDriver):
    driver = setup
    workbook, sheet = get_sheet()
    paiment = Paiment(driver)

    try:
        emaill = safe_value(sheet["C153"].value)

        champs_locators = {
            150: (By.XPATH, '//h1[contains(text(), "Paiement rapide et sécurisé en un clic")]'),
            151: (By.XPATH, '//p[@data-testid="intro-headline-subtitle" and contains(text(), "Enregistrez vos informations")]'),
            152: (By.XPATH, '//div[contains(@class, "PanelGroupExpandedHeader") and text()="Connexion"]'),
            153: (By.XPATH, '//label//span[contains(text(), "E-mail")]')
        }

        paiment.navigue_vers_paiment()
        paiment.remplir_minutes(50)
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_value((By.ID, "amount"), " "))
        paiment.click_achat()
        time.sleep(3)

        main_window = driver.current_window_handle
        paiment.click_payer_par_link()

        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
        new_window = [w for w in driver.window_handles if w != main_window][0]
        driver.switch_to.window(new_window)

        paiment.entrer_email(emaill)
        extract_and_validate_placeholders(driver, sheet, champs_locators)

        #  Fermer la fenêtre de paiement
        driver.close()

        #  Revenir à la fenêtre principale
        driver.switch_to.window(main_window)
        driver.get("https://vocodata.com/admin/dashboard")

    except Exception as e:
        print("Une erreur est survenue :", str(e))
        traceback.print_exc()

    try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
    except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")
        workbook.close()

           

##############################  payer par carte 
def test_paiement_carte(setup: WebDriver) :
    driver=setup
    workbook, sheet = get_sheet()
    
    paiment=Paiment(driver)
    try:
         
         emaill=safe_value(sheet["C156"].value)
         info_carte=safe_value(sheet["C157"].value)
         nom_carte=safe_value(sheet["C158"].value)

         champs_locators={ 156:(By.XPATH, "//span[contains(text(), 'E-mail')]"),
                          157:((By.XPATH, "//span[text()='Informations de la carte']")),
                          158 :(By.XPATH, "//span[text()='Nom du titulaire de la carte']"),
                          159 :(By.XPATH, "//span[text()='Pays ou région']"),
                          160:(( By.XPATH, "//div[text()='Enregistrer mes informations en toute sécurité pour pouvoir payer mes prochains achats en un clic']"))}
         paiment.navigue_vers_paiment()
         paiment.remplir_minutes(50)
         wait = WebDriverWait(driver, 10)
         wait.until(EC.text_to_be_present_in_element_value((By.ID, "amount"), " "))
         paiment.click_achat()
         time.sleep(6)
         extract_and_validate_placeholders(driver,sheet,champs_locators)
         paiment.fill_form_carte(emaill,info_carte,nom_carte)
         paiment.cocher_checkbox()
         time.sleep(2)
         driver.get("https://vocodata.com/admin/dashboard")

      
    except Exception as e:
           print("Une erreur est survenue :", str(e))
           traceback.print_exc()
    try:
            workbook.save(excel_path)
            print("[OK] Sauvegarde réussie dans Excel.")
    except PermissionError:
            print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")

            workbook.close() 
          


############################### analyser un audio ##################
def test_analyse_audio(setup: WebDriver) :
    driver=setup
    workbook, sheet = get_sheet()
    audio_path=r"C:\Users\pc\AppData\Roaming\Microsoft\Windows\Network Shortcuts\test_automatisation2\all_tests\ARIRO CHAIMA.mp3"
    analyse=Analyser(driver)
    #audio_path=r'C:\Users\pc\AppData\Roaming\Microsoft\Windows\Network Shortcuts\audio_test'
    try:
         
         champs_locators={ 162: (By.XPATH, "//c-card-header[normalize-space(text())=\"Analyseur de Qualité d'Appel (QCA)\"]"),
                          163:(By.ID, "grille"),
                          164:(By.XPATH, "//label[@for='enregistrement' and contains(text(), 'Enregistrement')]")
                          }
         analyse.naviguer_vers_analyser()
         time.sleep(3)
         extract_and_validate_placeholders(driver,sheet,champs_locators)
         analyse.select_grille()
         time.sleep(3)
         analyse.click_select_fichier(audio_path)
         analyse.click_sur_analyser()
         analyse.click_ok()

    except Exception as e:
           print("Une erreur est survenue :", str(e))
           traceback.print_exc()
    try:
            workbook.save(excel_path)
            print("[OK] Sauvegarde réussie dans Excel.")
    except PermissionError:
            print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")

            workbook.close() 


def test_creeer_utilisateur(setup) :
    driver=setup
    workbook, sheet = get_sheet()
    
    utilisateur=Utilisateur(driver)
    try:
         
         nom = safe_value(sheet["C59"].value)
         prenom = safe_value(sheet["C60"].value)
         emaill = safe_value(sheet["C61"].value)
         tel = safe_value(sheet["C62"].value)
         role=safe_value(sheet["C63"].value)
         pwdd = safe_value(sheet["C64"].value)
    
         
         champs_loators={
             167 : (By.XPATH, '//label[@for="nom"]')  ,            # "Nom"
             168 : (By.XPATH, '//label[@for="prenom"]') ,       # "Prénom"
             169 : (By.XPATH, '//label[@for="email"]') ,         # "Email"
             170 :(By.XPATH, '//label[@for="phone"]') ,         # "Telephone"
             171 :(By.XPATH, '//label[@for="role"]') ,           # "Role"
             172: (By.XPATH, '//label[@for="password"]')    # "M
         }
        
        
         utilisateur.navigue_vers_utilisateur()
         utilisateur.click_ajouter()
         time.sleep(2)
         extract_and_validate_placeholders(driver, sheet, champs_loators)
         utilisateur.fill_form_utilisateur(nom,prenom,emaill,tel,role,pwdd)
         utilisateur.click_ajout()
         extract_and_validate_placeholders(driver, sheet, champs_loators)
         time.sleep(4)
         last_locator={66:(By.ID,"swal2-html-container" )}
         extract_and_validate_placeholders(driver, sheet,  last_locator)
         utilisateur.click_ok()
         time.sleep(4)  
    except:
         print("error")
    try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
    except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")

        workbook.close()   
###########################################################creation d un utilisateur avec les memes donnes ################        
def test_creer_meme_utilisateur(setup) :
    driver=setup
    driver = setup
    workbook, sheet = get_sheet()
    
    utilisateur=Utilisateur(driver)
    try:
        
         nom = safe_value(sheet["C67"].value)
         prenom = safe_value(sheet["C68"].value)
         emaill = safe_value(sheet["C69"].value)
         tel = safe_value(sheet["C70"].value)
         role=safe_value(sheet["C71"].value)
         pwdd = safe_value(sheet["C72"].value)
    
         
         champs_loators={
             174 : (By.XPATH, '//label[@for="nom"]')  ,            # "Nom"
             175 : (By.XPATH, '//label[@for="prenom"]') ,       # "Prénom"
             176 : (By.XPATH, '//label[@for="email"]') ,         # "Email"
             177 :(By.XPATH, '//label[@for="phone"]') ,         # "Telephone"
             178 :(By.XPATH, '//label[@for="role"]') ,           # "Role"
             179 : (By.XPATH, '//label[@for="password"]')    # "M
         }
         analyser=Analyser(driver)
         analyser.naviguer_vers_analyser()
         utilisateur.navigue_vers_utilisateur()
         utilisateur.click_ajouter()
         time.sleep(2)
         utilisateur.fill_form_utilisateur(nom,prenom,emaill,tel,role,pwdd)
         utilisateur.click_ajout()
         extract_and_validate_placeholders(driver, sheet, champs_loators)
         time.sleep(4)
         last_locator={66:(By.ID,"swal2-html-container" )}
         extract_and_validate_placeholders(driver, sheet,  last_locator)
         utilisateur.click_ok()
    except:
         print("error")
    try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
    except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")

        workbook.close()  
#######################################################fermer sans creer un utilisateur###########################
def test_fermer_sans_creation(setup) :
    driver=setup
    
    workbook, sheet = get_sheet()
   
    utilisateur=Utilisateur(driver)
    try:
        
         champs_loators={
             183 : (By.XPATH, '//label[@for="nom"]')  ,            # "Nom"
             184 : (By.XPATH, '//label[@for="prenom"]') ,       # "Prénom"
             185 : (By.XPATH, '//label[@for="email"]') ,         # "Email"
             186 :(By.XPATH, '//label[@for="phone"]') ,         # "Telephone"
             187 :(By.XPATH, '//label[@for="role"]') ,           # "Role"
             188 : (By.XPATH, '//label[@for="password"]')    # "M
         }
         
         utilisateur.navigue_vers_utilisateur()
         utilisateur.click_ajouter()
         time.sleep(2)
         extract_and_validate_placeholders(driver, sheet, champs_loators)
         utilisateur.click_fermer()
         time.sleep(4)
    except:
         print("error")
    try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
    except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")

        workbook.close()  
###################################### modifier un utilisateur   ################3####     
def test_modifier_utilisateur(setup):
    driver=setup
    workbook, sheet = get_sheet()
    utilisateur=Utilisateur(driver)
    try:
         
    
         nom = safe_value(sheet["C83"].value)
         prenom = safe_value(sheet["C84"].value)
         emaill = safe_value(sheet["C85"].value)
         tel = safe_value(sheet["C86"].value)
         role=safe_value(sheet["C87"].value)
         champs_locators={
             190:((By.XPATH, "//h5[contains(text(), \"Modifier l'utilisateur\")]")),
             191 : (By.XPATH, '//label[@for="nom"]')  ,            # "Nom"
             192 : (By.XPATH, '//label[@for="prenom"]') ,       # "Prénom"
             193 : (By.XPATH, '//label[@for="email"]') ,         # "Email"
             194 :(By.XPATH, '//label[@for="phone"]') ,         # "Telephone"
             195 :(By.XPATH, '//label[@for="role"]') ,           # "Role"
             196 : (By.XPATH, "//label[contains(text(),\"Activation de l'Email\")]")   # "M
             }
         
         utilisateur.navigue_vers_utilisateur()
         utilisateur.cliquer_bouton_modifier(emaill)
         time.sleep(2)
         extract_and_validate_placeholders(driver, sheet, champs_locators)
         utilisateur.fill_information_modifier(nom,prenom,emaill,tel,role)
         time.sleep(2)
         utilisateur.click_chek()
         time.sleep(2)
         utilisateur.click_editer()
         time.sleep(2)
         utilisateur.click_ok()
    except Exception as e:
        print("error",e)
    try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
    except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")
        workbook.close()  
 #################################################supprimer un utilisateur#####################
def test_supprimer_utilisateur(setup):
    
    driver = setup
    workbook, sheet = get_sheet()
    
    utilisateur=Utilisateur(driver)
    emaill = safe_value(sheet["C85"].value)
    try:
         
         champs_locators={ 198:(By.ID, "swal2-title"),
                          199:(By.ID, "swal2-html-container")
            
             }
         
         utilisateur.navigue_vers_utilisateur()
         #time.sleep(2)
         utilisateur.click_supprimer(emaill)
         time.sleep(1)
         extract_and_validate_placeholders(driver, sheet, champs_locators)
         time.sleep(1)
         #utilisateur.click_annuler()
         utilisateur.clcik__delete()
         time.sleep(1)
         utilisateur.click_ok()
    except Exception as e:
        print("error",e)
    try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
    except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")
        workbook.close()   

#################### ENREGISTREMENT DETAILS 
def test_afficher_details(setup):
    
    driver = setup
    workbook, sheet = get_sheet()
    enre=Enregistrement(driver)
    
    try:
         
         champs_locators={ 198:(By.ID, "swal2-title"),
                          199:(By.ID, "swal2-html-container")
            
             }
         
         enre.navigue_vers_enregistremet()
         enre.click_details()
    except Exception as e:
        print("error",e)
    try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
    except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")
        workbook.close()



################ TELECHARGER LE RAPPORT 
def test_telecharger_rapport(setup):
    
    driver = setup
    workbook, sheet = get_sheet()
    enre=Enregistrement(driver)
    
    try:
         
         champs_locators={ 198:(By.ID, "swal2-title"),
                          199:(By.ID, "swal2-html-container")
            
             }
         
         enre.navigue_vers_enregistremet()
         enre.telecharger()
    except Exception as e:
        print("error",e)
    try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
    except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")
        workbook.close()


#############TELECHARGER PAR CLIC
def test_enregister_par_clic(setup):
    
    driver = setup
    workbook, sheet = get_sheet()
    enre=Enregistrement(driver)
    
    try:
         
         champs_locators={ 198:(By.ID, "swal2-title"),
                          199:(By.ID, "swal2-html-container")
            
             }
         
         enre.navigue_vers_enregistremet()
         enre.telcharger_par_click()
    except Exception as e:
        print("error",e)
    try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
    except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")
        workbook.close()




################### SUPPRIMER L'audio
def test_supprimer(setup):
    
    driver = setup
    workbook, sheet = get_sheet()
    enre=Enregistrement(driver)
    utilisateur=Utilisateur(driver)
    try:
         
         champs_locators={ 198:(By.ID, "swal2-title"),
                          199:(By.ID, "swal2-html-container")
            
             }
         
         enre.navigue_vers_enregistremet()
         enre.supprimer()
    except Exception as e:
        print("error",e)
    try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
    except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")
        workbook.close()


            


