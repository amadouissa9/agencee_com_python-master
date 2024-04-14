# DAO -> Data Access Object
# CRUD
import database
from employes.employe import Employe
class EmployeDao:
    # attributs de classe
    connexion = database.connect_db()
    cursor = connexion.cursor()
    
    def __init__(self):
        pass

    @classmethod    
    def create(cls,nom, prenom, matricule, fonction, departement):
        sql = """ INSERT INTO employe(nom,prenom,matricule,fonction,departement)
                  VALUES(%s,%s,%s,%s,%s)
              """ 
        params = (nom, prenom, matricule, fonction, departement)
        try:
            EmployeDao.cursor.execute(sql, params)
            EmployeDao.connexion.commit()
            EmployeDao.cursor.close()
            message = f"L'employé de matricule {matricule} est ajouté avec succès"
        except Exception as error:
            message = f"Une erreur est survenue lors de l'ajout de l'employé, si ça persiste veuillez contacter l'administrateur", error     
        
        return message
    
    @classmethod
    def list_all(cls):
        sql = "SELECT * FROM employe"
        try:
            EmployeDao.cursor.execute(sql)
            employes = EmployeDao.cursor.fetchall()
            message = "success"
            EmployeDao.cursor.close()
        except Exception as error:
            #print(error) # Pour le deboggage en developpement.
            message = "Une erreur est survennue lors de la récuperation des données"
            employes = []
        return (employes, message)
    
    @classmethod # filtrer via le matricule.
    def list_one(cls, matricule):
        sql = "SELECT * FROM employe WHERE matricule=%s"
        EmployeDao.cursor.execute(sql, (matricule,))
        employe = EmployeDao.cursor.fetchone()
        EmployeDao.cursor.close()
        return employe
    
    @classmethod
    def delete(cls, matricule):
        sql = "DELETE FROM employe WHERE matricule=%s"
        EmployeDao.cursor.execute(sql, (matricule,))
        EmployeDao.connexion.commit()
        EmployeDao.cursor.close()

        return f"L'employé de matricule {matricule} est suprimé avec succès"
    
    @classmethod
    def update(cls,nom, prenom, matricule, fonction, departement):
        sql = """UPDATE employe SET nom=%s,prenom=%s,matricule=%sfonction=%s,departement=%s
                   WHERE id=1
              """
        params = (nom, prenom, matricule, fonction, departement)
        EmployeDao.cursor.execute(sql, params)
        EmployeDao.connexion.commit() 
        EmployeDao.cursor.close()

        return f"L'employé de matricule {matricule} est mise à avec succès"

    @classmethod
    def test(cls):
        print('test employeDAO') 
        

