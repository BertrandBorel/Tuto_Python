# Créer un QR-code avec Python

# Source : Revue Coding, n°18, p.27.
# Bibliothèque : pyrqcode (pip install pyqrcode)



import pyqrcode 
from pyqrcode import QRCode

# lien url qui représente le code QR
var = 'https://github.com/BertrandBorel?tab=repositories'

# Génération du QR code
url = pyqrcode.create(var)

# création et enregistrement du fichier png nommé "monqr.png"
url.svg("moncodeQR.svg", scale = 8)