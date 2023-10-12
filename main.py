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
        card_name_label = QLabel("Nom de la carte : Acteur PH Premium")
        card_description_text = QTextEdit("Description de la carte...")
        card_url_label = QLabel("URL de l'annonce :")
        card_url_browser = QTextBrowser()  # Utilisez QTextBrowser pour l'URL
        card_url_browser.setOpenExternalLinks(True)  # Activez l'ouverture de liens externes
        card_url_browser.setPlainText("https://fr.indeed.com/?from=gnav-jobsearch--indeedmobile&vjk=d796ad4bb90c7fbc&advn=4190676325902957")  # Définissez le lien URL
        card_url_browser.setOpenExternalLinks(True)

        # add informations to card...
        card_layout.addWidget(card_name_label)
        card_layout.addWidget(card_description_text)
        card_layout.addWidget(card_url_label)
        card_layout.addWidget(card_url_browser)
        
        #card size 
        card_description_text.setFixedHeight(300)
        card_description_text.setFixedWidth(300)
        card_url_browser.setFixedWidth(300)
        card_url_browser.setFixedHeight(70)

        #date
        self.date_label = QLabel(self)
        self.date_label.setAlignment(Qt.AlignTop | Qt.AlignRight)
        self.date_label.setFont(QFont("Arial", 14))
        self.date_label.setText(self.get_current_date())
        main_layout.addWidget(self.date_label)

        #btn
        btn_quit = QPushButton("Quitter", self)
        btn_copy = QPushButton("Copy", self)
        btn_generate = QPushButton("Générer", self)
        button_layout.addWidget(btn_quit)
        button_layout.addWidget(btn_copy)
        button_layout.addWidget(btn_generate)


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
        btn_copy.clicked.connect(self.copy)

        #status bar
        self.setStatusBar(QStatusBar(self))
        self.status = self.statusBar()

    #Action btn
    def quit(self):
        if dialogs.confirm(self):
            QApplication.quit() 

    def copy(self):
        clipboard = QApplication.clipboard()
        clipboard.setText()
        


    def get_current_date(self):
        # Utilisez la bibliothèque datetime pour obtenir la date actuelle
        current_date = datetime.date.today()
        return current_date.strftime("Date du jour : %d/%m/%Y") 

app = QApplication(sys.argv)

window = MainWindow()
window.setWindowTitle("Search Jobs")
window.show()

app.exec()
