import sys
from pyowm import OWM
from PySide2 import QtCore, QtGui, QtWidgets
from weather_form import Ui_Dialog

# Create app
app = QtWidgets.QApplication(sys.argv)

# init
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()


# Hook Logic
def get_weather():
    owm = OWM('15f9a50154a2eee7ffca2758ae178d7a')
    # I get API-key on the https://home.openweathermap.org/api_keys
    # must be login first
    place = ui.lineEdit.text()
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    ui.label.setText(f'Температура: {temp}')


ui.pushButton.clicked.connect(get_weather)

# Main Loop
sys.exit(app.exec_())
