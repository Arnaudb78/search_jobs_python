#main

import sys
from PySide6.QtCore import * # c'est le coeur du système
from PySide6.QtWidgets import * #permet d'ajouter des btn etc..
from PySide6.QtGui import * # comme le widget mais plus précis

import random

from pathlib import Path 

#import mon fichier
import dialogs

#pour afficher la date 
import datetime

import sqlite3


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(900,700))

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        option_layout = QGridLayout()
        button_layout = QHBoxLayout()
        card_layout = QVBoxLayout()

        main_layout.addLayout(option_layout)
        main_layout.addLayout(button_layout)
        main_layout.addLayout(card_layout)

        # Card informations
        self.card_name_label = QLabel("Nom de la carte :")
        self.card_name_label.setText(" ")
        self.card_description_text = QLabel("Description de la fiche de poste :")
        self.card_description_text = QTextEdit(" ")
        self.card_url_label = QLabel("URL de l'annonce :")
        self.card_url_browser = QTextBrowser()  # Utilisez QTextBrowser pour l'URL
        self.card_url_browser.setOpenExternalLinks(True)  # Activez l'ouverture de liens externes
        self.card_url_browser.setPlainText(" ")  # Définissez le lien URL
        self.card_url_browser.setOpenExternalLinks(True)
        self.card_location = QLabel("Localisation")
        self.card_location_value = QLabel(" ")
        self.card_type = QLabel("Contrat :")
        self.card_type_value = QLabel(" ")

        
        # add informations to card...
        card_layout.addWidget(self.card_name_label)
        card_layout.addWidget(self.card_description_text)
        card_layout.addWidget(self.card_url_label)
        card_layout.addWidget(self.card_url_browser)
        card_layout.addWidget(self.card_location)
        card_layout.addWidget(self.card_location_value)
        card_layout.addWidget(self.card_type)
        card_layout.addWidget(self.card_type_value)
        
        #card size 
        self.card_description_text.setFixedHeight(200)
        self.card_description_text.setFixedWidth(300)
        self.card_url_browser.setFixedWidth(300)
        self.card_url_browser.setFixedHeight(70)

        #Element card position 
        # option_layout.addWidget( self.card_name_label, 0, 0)
        # option_layout.addWidget(self.card_description_text, 0, 1)
        # option_layout.addWidget(self.card_url_label, 1, 0)
        # option_layout.addWidget(self.card_url_browser, 1, 1)
        # option_layout.addWidget(self.card_location, 2, 0)
        # option_layout.addWidget(self.card_location_value, 2, 1)
        # option_layout.addWidget(self.card_type, 3, 0)
        # option_layout.addWidget(self.card_type_value, 3, 1)

        #date
        self.date_label = QLabel(self)
        self.date_label.setFont(QFont("Arial", 14))
        self.date_label.setText(self.get_current_date())

        #btn
        btn_quit = QPushButton("Quitter", self)

        #Checkbox params
        self.option_jobs = QCheckBox("Emploie")
        option_layout.addWidget(self.option_jobs, 0,1)
        self.option_alternating = QCheckBox("Alternance")
        option_layout.addWidget(self.option_alternating, 1, 1)
        self.option_stage = QCheckBox("Stage")
        option_layout.addWidget(self.option_stage, 0, 2)

        #checkbox check open application
        self.option_jobs.setChecked(True)

        #Connect btn
        btn_quit.clicked.connect(self.quit)
        

        #status bar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("(c) Moisi Corp Limited", 0)
        self.status_bar.addPermanentWidget(self.date_label)

        ##Database
        self.load_data()

    #Action btn
    def quit(self):
        if dialogs.confirm(self):
            QApplication.quit() 

    def copy(self):
        clipboard = QApplication.clipboard()
        clipboard.setText()
        

    #function date of the day...
    def get_current_date(self):
        current_date = datetime.date.today()
        return current_date.strftime("Date du jour : %d/%m/%Y") 
    
    def load_data(self):
    # Établir une connexion à la base de données
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        # Exécuter une requête pour récupérer les données
        query = "SELECT description, name, location, url, type FROM jobs"
        cursor.execute(query)
        data = cursor.fetchall()

        # Fermer la connexion à la base de données
        connection.close()

        # Mettre à jour les labels ou QTextBrowser de votre interface avec les données récupérées
        if data:
            description, name, location, url, type = data[2]  # Supposons que vous récupérez la première ligne de données
            self.card_name_label.setText(name)
            self.card_description_text.setText(description)
            self.card_location_value.setText(location)
            self.card_url_browser.setPlainText(url)
            self.card_type_value.setText(type)


app = QApplication(sys.argv)

window = MainWindow()
window.setWindowTitle("Search Jobs")
window.show()

app.exec()
