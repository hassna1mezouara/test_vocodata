from pages_super_admin.siteDisplay import Display
from selenium.webdriver.common.by import By
from pages_super_admin.inscription import LoginPage
from pages_super_admin.logs import Logs
from pages_super_admin.login import Login
from pages_super_admin.utilisateur import Utilisateur
from pages_super_admin.entreprise import Entreprise
import os
import openpyxl
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



####################################################site connection#########################################
def test_display_navigation_from_excel(setup):
    driver = setup
    workbook, sheet = get_sheet()
    url = sheet["C2"].value
    driver.get(url)
    dis = Display(driver)
    champs_locatorss = {
    2: (By.LINK_TEXT, "Accueil"),
    3: (By.ID, "navbarDropdown"),  # Solution a un id spécifique
    4: (By.LINK_TEXT, "Tarif"),
    5: (By.LINK_TEXT, "Contact"),
    6: (By.CSS_SELECTOR, "a[href='/auth/register']"),  # Inscription
    7: (By.CSS_SELECTOR, "a[href='/auth/login']")      # Connexion
} 
    time.sleep(1)
    extract_and_validate_placeholders(driver, sheet, champs_locatorss)
    dis.click_solution()
    dis.click_and_display_section(dis.features_locator, "Features")
    dis.click_solution()
    dis.click_and_display_section(dis.how_it_works_locator, "How it Works")
    dis.click_and_display_section(dis.tarif_locator, "Trafic")
    dis.click_and_display_section(dis.contact_locator, "Contact")
    dis.click_and_display_section(dis.inscription_locator, "Contact")
 
    try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
    except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")

    workbook.close() 



################################################################inscription 1#################################
def test_registration_field_extraction_and_validation(setup):
    driver = setup
    workbook, sheet = get_sheet()
    register_url = sheet["C9"].value
    driver.get(register_url)

    register = LoginPage(driver)

    # Liste des locators pour les champs du formulaire
    champs_locators = {
    10: (By.CSS_SELECTOR, "label[for='nom']"),               # Nom
    11: (By.CSS_SELECTOR, "label[for='prenom']"),            # Prénom
    12: (By.CSS_SELECTOR, "label[for='email']"),             # Email
    13: (By.CSS_SELECTOR, "label[for='phone']"),             # Téléphone
    14: (By.CSS_SELECTOR, "label[for='password']"),          # Mot de passe
    15: (By.CSS_SELECTOR, "label[for='confirmPassword']"),   }
    extract_and_validate_placeholders(driver, sheet, champs_locators)
   
    # 2. REMPLISSAGE DU FORMULAIRE
    try:
        nom = safe_value(sheet["C10"].value)
        prenom = safe_value(sheet["C11"].value)
        email = safe_value(sheet["C12"].value)
        telephone = safe_value(sheet["C13"].value)
        mot_de_passe = safe_value(sheet["C14"].value)
        confirmer_mot_de_passe = safe_value(sheet["C15"].value)
        entreprise_nom = safe_value(sheet["C16"].value)
        ice = safe_value(sheet["C17"].value)
        adresse = safe_value(sheet["C18"].value)

        # Remplir le formulaire
        register.fill_form(nom, prenom, email, telephone, mot_de_passe, confirmer_mot_de_passe)
        register.click_suivant()

        locators_foem2={16: (By.CSS_SELECTOR, "label[for='company_name']"),     
    17: (By.CSS_SELECTOR, "label[for='company_ice']"),       # ICE
    18: (By.CSS_SELECTOR, "label[for='company_address']") }
        extract_and_validate_placeholders(driver, sheet, locators_foem2)
        time.sleep(3)

        # Remplir l'étape 2 (entreprise)
        register.fill_second_step(entreprise_nom, ice, adresse, logo_path)
        time.sleep(3)
        register.click_valider()
        time.sleep(5)
        print("[OK] Formulaire rempli et soumis avec succès.")
 

    except Exception as e:
        print(f"[Erreur] Pendant le remplissage du formulaire : {e}")

     # 3. SAUVEGARDE DU FICHIER EXCEL
    try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
    except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")

    workbook.close() 

##########################################################inscription with the same information##########################

def test_registration_field_extraction_and_validation_2(setup):
    driver = setup
    workbook, sheet = get_sheet()
    register_url = sheet["C9"].value
    driver.get(register_url)

    register = LoginPage(driver)

    # Liste des locators pour les champs du formulaire
   

    # 2. REMPLISSAGE DU FORMULAIRE
    try:
        nom = safe_value(sheet["C21"].value)
        prenom = safe_value(sheet["C22"].value)
        email = safe_value(sheet["C23"].value)
        telephone = safe_value(sheet["C24"].value)
        mot_de_passe = safe_value(sheet["C25"].value)
        confirmer_mot_de_passe = safe_value(sheet["C26"].value)
        entreprise_nom = safe_value(sheet["C27"].value)
        ice = safe_value(sheet["C28"].value)
        adresse = safe_value(sheet["C29"].value)

        champs_locatorsss = {
                          #nas
    21: (By.CSS_SELECTOR, "label[for='nom']"),               # Nom
    22: (By.CSS_SELECTOR, "label[for='prenom']"),            # Prénom
    23: (By.CSS_SELECTOR, "label[for='email']"),             # Email
    24: (By.CSS_SELECTOR, "label[for='phone']"),             # Téléphone
    25: (By.CSS_SELECTOR, "label[for='password']"),          # Mot de passe
    26: (By.CSS_SELECTOR, "label[for='confirmPassword']"
         )   # Confirmez le mot de passe    
}
        time.sleep(3)
        extract_and_validate_placeholders(driver, sheet, champs_locatorsss)


        # Remplir le formulaire
        register.fill_form(nom, prenom, email, telephone, mot_de_passe, confirmer_mot_de_passe)
        register.click_suivant()

        locators_foem2={27: (By.CSS_SELECTOR, "label[for='company_name']"),     
    28: (By.CSS_SELECTOR, "label[for='company_ice']"),       # ICE
    29: (By.CSS_SELECTOR, "label[for='company_address']") }
        extract_and_validate_placeholders(driver, sheet, locators_foem2)

        # Remplir l'étape 2 (entreprise)
        register.fill_second_step(entreprise_nom, ice, adresse, logo_path)
        register.click_valider()
        print("[OK] Formulaire rempli et soumis avec succès.")
        last_locator={20:(By.ID,"swal2-html-container" )}
        extract_and_validate_placeholders(driver, sheet,  last_locator)
        time.sleep(5)  # Facultatif : temps d'attente pour observer la soumission
        
        

    except Exception as e:
        print(f"[Erreur] Pendant le remplissage du formulaire : {e}")

    # 3. SAUVEGARDE DU FICHIER EXCEL
    try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
    except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")

    workbook.close()     

########################################################login creer un compte######################
def test_login_cree_un_noveau_compte(setup):
     driver = setup
     workbook, sheet = get_sheet()
     url = sheet["C32"].value
     driver.get(url)
     log = Login(driver) 
     time.sleep(3)

     champs_locatorsss = {
                          #nas
    33: (By.CSS_SELECTOR, "label[for='nom']"),               # Nom
    34: (By.CSS_SELECTOR, "label[for='prenom']"),            # Prénom
    35: (By.CSS_SELECTOR, "label[for='email']"),             # Email
    36: (By.CSS_SELECTOR, "label[for='phone']"),             # Téléphone
    37: (By.CSS_SELECTOR, "label[for='password']"),          # Mot de passe
    38: (By.CSS_SELECTOR, "label[for='confirmPassword']"
         )   # Confirmez le mot de passe    
}  
    
     log.click_creer() 
     extract_and_validate_placeholders(driver, sheet, champs_locatorsss)
     time.sleep(3)
    #  locator={}
    #  extract_and_validate_placeholders(driver, sheet, locator)
     try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
     except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")

        workbook.close()     

###########################################login with uncorrect email #######################################

def test_login_with_incorrect_email(setup):
     driver = setup
     workbook, sheet = get_sheet()
     url = sheet["C40"].value
     driver.get(url)
     log = Login(driver) 
     try:
         email = safe_value(sheet["C41"].value)
         pwd=safe_value(sheet["C42"].value)
         log.fill_form_connexion(email,pwd)
         champs_locators={40:(By.CSS_SELECTOR,".swal2-html-container"),
            41:(By.CSS_SELECTOR, 'label[for="email"]'),
            42:(By.CSS_SELECTOR, 'label[for="password"]')}
         log.click_connexion()
         time.sleep(4)
         extract_and_validate_placeholders(driver, sheet, champs_locators)
     except:
         print("error")
     try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
     except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")

        workbook.close() 

####################################### login mot de pSSE OUBLIER############
def test_login(setup):
     driver = setup
     workbook, sheet = get_sheet()
     url = sheet["C32"].value
     driver.get(url)
     log = Login(driver) 
     try:
         email = safe_value(sheet["C45"].value)
         
     ##recuperation  
         champs_locators={45:(By.CSS_SELECTOR, "label[for='email'].form-label"),
         }
         time.sleep(2)
         log.click_mot_de_passe_oublier()
         log.fill_form_connexion_oublier(email)
         time.sleep(1)
         extract_and_validate_placeholders(driver, sheet, champs_locators)
         log.click_renitialise()
         time.sleep(2)
     except Exception as e:
        print(f"[Erreur] Pendant le remplissage du formulaire : {e}")     
     try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
     except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")

        workbook.close()     
############################3login succes#############################################

def login_once(driver, sheet):
    url = safe_value(sheet["C48"].value)
    driver.get(url)
    log = Login(driver)
    email = safe_value(sheet["C49"].value)
    pwd = safe_value(sheet["C50"].value)
    log.fill_form_connexion(email, pwd)
    log.click_connexion()
    time.sleep(2)
    return log
def test_login_succes(setup):
     driver = setup
     workbook, sheet = get_sheet()
     log = login_once(driver, sheet)
     log = Login(driver) 
     try:
         
         champs_locators={
            49:(By.CSS_SELECTOR, 'h5.card-title.text-primary'),
            50:(By.CSS_SELECTOR, 'p.mb-4'),
            51:(By.XPATH, '//span[text()="Tableau de bord"]'),
            52:(By.XPATH, '//span[contains(text(), "Grilles")]'),
            53:(By.XPATH, '//span[text()="Utilisateurs"]'),
            54:(By.XPATH, '//span[text()="Entreprises"]'),
            55:(By.XPATH, '//span[text()="Transactions"]') ,
            56:(By.XPATH, '//span[text()="Logs"]')              }
       
         time.sleep(2)
         extract_and_validate_placeholders(driver, sheet, champs_locators)
         log.naviguer_dans_menus()
         
     except:
         print("error")
     try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
     except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")

        workbook.close()   
####################################################creation d'un utilisateur##########################333             
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
             59 : (By.XPATH, '//label[@for="nom"]')  ,            # "Nom"
             60 : (By.XPATH, '//label[@for="prenom"]') ,       # "Prénom"
             61 : (By.XPATH, '//label[@for="email"]') ,         # "Email"
             62 :(By.XPATH, '//label[@for="phone"]') ,         # "Telephone"
             63 :(By.XPATH, '//label[@for="role"]') ,           # "Role"
             64: (By.XPATH, '//label[@for="password"]')    # "M
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
             67 : (By.XPATH, '//label[@for="nom"]')  ,            # "Nom"
             68 : (By.XPATH, '//label[@for="prenom"]') ,       # "Prénom"
             69 : (By.XPATH, '//label[@for="email"]') ,         # "Email"
             70 :(By.XPATH, '//label[@for="phone"]') ,         # "Telephone"
             71 :(By.XPATH, '//label[@for="role"]') ,           # "Role"
             72 : (By.XPATH, '//label[@for="password"]')    # "M
         }
         entreprise=Entreprise(driver)
         entreprise.naviguer_vers_entreprise()
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
             75 : (By.XPATH, '//label[@for="nom"]')  ,            # "Nom"
             76 : (By.XPATH, '//label[@for="prenom"]') ,       # "Prénom"
             77 : (By.XPATH, '//label[@for="email"]') ,         # "Email"
             78 :(By.XPATH, '//label[@for="phone"]') ,         # "Telephone"
             79 :(By.XPATH, '//label[@for="role"]') ,           # "Role"
             80 : (By.XPATH, '//label[@for="password"]')    # "M
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
             82:((By.XPATH, "//h5[contains(text(), \"Modifier l'utilisateur\")]")),
             83 : (By.XPATH, '//label[@for="nom"]')  ,            # "Nom"
             84 : (By.XPATH, '//label[@for="prenom"]') ,       # "Prénom"
             85 : (By.XPATH, '//label[@for="email"]') ,         # "Email"
             86 :(By.XPATH, '//label[@for="phone"]') ,         # "Telephone"
             87 :(By.XPATH, '//label[@for="role"]') ,           # "Role"
             88 : (By.XPATH, "//label[contains(text(),\"Activation de l'Email\")]")   # "M
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
         
         champs_locators={ 90:(By.ID, "swal2-title"),
                          91:(By.ID, "swal2-html-container")
            
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

#########################################PAGE LOGS ########################
def test_exporter (setup) : 
    driver=setup
    
    workbook, sheet = get_sheet()
    
    logg=Logs(driver)
    try:
        
        logg.naviguer_vers_logs()
        time.sleep(2)
        logg.click_exporter()
        time.sleep(3)
    except Exception as e:
        print("error",e)
    try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
    except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")
        workbook.close()
       
######################################## modifier et valider l'entreprise #############
def test_modifier_valider_entreprise(setup):
    driver=setup
    workbook, sheet = get_sheet()
  
    entreprise=Entreprise(driver)
    try:
         
         entreprise_nom = safe_value(sheet["C97"].value)
         ice = safe_value(sheet["C98"].value)
         adresse = safe_value(sheet["C99"].value)
         
         champs_locatorss={
             97: (By.CSS_SELECTOR, "label[for='name']"),     
    98: (By.CSS_SELECTOR, "label[for='ice']"),       # ICE
    99: (By.CSS_SELECTOR, "label[for='company_address']") }


         entreprise.naviguer_vers_entreprise()
         time.sleep(4)
         entreprise.cl_modifier("smart")
         time.sleep(3)
         extract_and_validate_placeholders(driver,sheet,champs_locatorss)
         entreprise.fill_form_entreprise(entreprise_nom,ice,adresse,logo_path)
         entreprise.click_chek()
         time.sleep(2)
         entreprise.click_editer()
         time.sleep(4)
         entreprise.click_ok()
    except Exception as e:
         print("error",e)
    try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
    except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")
        workbook.close()   
######################################## supprimer un entreprise ##############          
def test_supprimer_entreprise(setup) :
    driver=setup
    workbook, sheet = get_sheet()
   
    entreprise=Entreprise(driver)
    try:
         
         champs_locatorss={
             102:(By.ID, "swal2-title"),     
             103: (By.ID, "swal2-html-container"),      
    }     
         
         time.sleep(3)
         entreprise.naviguer_vers_entreprise()
         time.sleep(3)
         entreprise.cl_supprimer("smart")
         time.sleep(4)
         extract_and_validate_placeholders(driver,sheet,champs_locatorss)
         entreprise.annuler_supr()
         time.sleep(4)
         entreprise.click_ok()
    except Exception as e:
         print("error",e)
    try:
        workbook.save(excel_path)
        print("[OK] Sauvegarde réussie dans Excel.")
    except PermissionError:
        print("[Erreur] Ferme le fichier Excel avant de sauvegarder.")
        workbook.close()   








