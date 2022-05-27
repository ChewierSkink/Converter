# Импортируем потоковый ввод
import sys
# Импортируем интерфейс
from design import Ui_MainWindow
# Импортируем функции для работы программы
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


ko1 = [0, 0]
ko2 = [0, 0]
kd1 = 1
kd2 = 1
r = 0

# Основной класс
class Conv(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Назначаем строку только для чтения
        self.lineEdit_2.setReadOnly(True)

        # Равнение ввода по правому краю
        self.lineEdit.setAlignment(Qt.AlignRight)
        self.lineEdit_2.setAlignment(Qt.AlignRight)

        # Создание групп кнопок
        self.group_11 = QButtonGroup()
        self.group_11.addButton(self.radioButton)
        self.group_11.addButton(self.radioButton_2)
        self.group_11.addButton(self.radioButton_3)
        self.group_11.addButton(self.radioButton_4)
        self.group_11.addButton(self.radioButton_33)
        self.group_11.addButton(self.radioButton_34)
        self.group_11.addButton(self.radioButton_35)
        self.group_11.addButton(self.radioButton_36)
        self.group_11.addButton(self.radioButton_53)
        self.group_11.addButton(self.radioButton_55)
        self.group_11.addButton(self.radioButton_56)
        self.group_11.addButton(self.radioButton_57)
        self.group_11.addButton(self.radioButton_58)
        self.group_11.addButton(self.radioButton_63)
        self.group_11.addButton(self.radioButton_64)
        self.group_11.addButton(self.radioButton_65)
        self.group_11.addButton(self.radioButton_66)
        self.group_11.addButton(self.radioButton_71)
        self.group_11.addButton(self.radioButton_72)
        self.group_11.addButton(self.radioButton_73)
        self.group_11.addButton(self.radioButton_74)
        self.group_11.addButton(self.radioButton_79)
        self.group_11.addButton(self.radioButton_80)
        self.group_11.addButton(self.radioButton_81)
        self.group_11.addButton(self.radioButton_82)
        self.group_11.addButton(self.radioButton_83)
        self.group_11.addButton(self.radioButton_89)
        self.group_11.addButton(self.radioButton_91)
        self.group_11.addButton(self.radioButton_92)
        self.group_11.addButton(self.radioButton_93)
        self.group_11.addButton(self.radioButton_94)
        self.group_11.addButton(self.radioButton_95)
        self.group_11.addButton(self.radioButton_96)
        self.group_11.addButton(self.radioButton_103)
        self.group_11.addButton(self.radioButton_104)
        self.group_11.addButton(self.radioButton_105)
        self.group_11.addButton(self.radioButton_106)
        self.group_11.addButton(self.radioButton_107)
        self.group_12 = QButtonGroup()
        self.group_12.addButton(self.radioButton_5)
        self.group_12.addButton(self.radioButton_6)
        self.group_12.addButton(self.radioButton_7)
        self.group_12.addButton(self.radioButton_8)
        self.group_12.addButton(self.radioButton_49)
        self.group_12.addButton(self.radioButton_50)
        self.group_12.addButton(self.radioButton_51)
        self.group_12.addButton(self.radioButton_52)
        self.group_12.addButton(self.radioButton_54)
        self.group_12.addButton(self.radioButton_59)
        self.group_12.addButton(self.radioButton_60)
        self.group_12.addButton(self.radioButton_61)
        self.group_12.addButton(self.radioButton_62)
        self.group_12.addButton(self.radioButton_67)
        self.group_12.addButton(self.radioButton_68)
        self.group_12.addButton(self.radioButton_69)
        self.group_12.addButton(self.radioButton_70)
        self.group_12.addButton(self.radioButton_75)
        self.group_12.addButton(self.radioButton_76)
        self.group_12.addButton(self.radioButton_77)
        self.group_12.addButton(self.radioButton_78)
        self.group_12.addButton(self.radioButton_84)
        self.group_12.addButton(self.radioButton_85)
        self.group_12.addButton(self.radioButton_86)
        self.group_12.addButton(self.radioButton_87)
        self.group_12.addButton(self.radioButton_88)
        self.group_12.addButton(self.radioButton_90)
        self.group_12.addButton(self.radioButton_100)
        self.group_12.addButton(self.radioButton_101)
        self.group_12.addButton(self.radioButton_102)
        self.group_12.addButton(self.radioButton_97)
        self.group_12.addButton(self.radioButton_98)
        self.group_12.addButton(self.radioButton_99)
        self.group_12.addButton(self.radioButton_108)
        self.group_12.addButton(self.radioButton_109)
        self.group_12.addButton(self.radioButton_110)
        self.group_12.addButton(self.radioButton_111)
        self.group_12.addButton(self.radioButton_112)
        self.group_21 = QButtonGroup()
        self.group_21.addButton(self.radioButton_9)
        self.group_21.addButton(self.radioButton_10)
        self.group_21.addButton(self.radioButton_11)
        self.group_21.addButton(self.radioButton_12)
        self.group_21.addButton(self.radioButton_13)
        self.group_21.addButton(self.radioButton_14)
        self.group_21.addButton(self.radioButton_15)
        self.group_21.addButton(self.radioButton_16)
        self.group_21.addButton(self.radioButton_17)
        self.group_21.addButton(self.radioButton_18)
        self.group_21.addButton(self.radioButton_19)
        self.group_21.addButton(self.radioButton_20)
        self.group_22 = QButtonGroup()
        self.group_22.addButton(self.radioButton_21)
        self.group_22.addButton(self.radioButton_22)
        self.group_22.addButton(self.radioButton_23)
        self.group_22.addButton(self.radioButton_24)
        self.group_22.addButton(self.radioButton_25)
        self.group_22.addButton(self.radioButton_26)
        self.group_22.addButton(self.radioButton_27)
        self.group_22.addButton(self.radioButton_28)
        self.group_22.addButton(self.radioButton_29)
        self.group_22.addButton(self.radioButton_30)
        self.group_22.addButton(self.radioButton_31)
        self.group_22.addButton(self.radioButton_32)

        # Блок кликов
        self.pushButton_4.clicked.connect(self.clear_1)
        self.pushButton_5.clicked.connect(self.clear_2)
        self.pushButton_2.clicked.connect(self.reset_o)
        self.pushButton_3.clicked.connect(self.reset_d)
        self.pushButton.clicked.connect(self.perevod)
        self.group_11.buttonClicked.connect(self.check_11)
        self.group_12.buttonClicked.connect(self.check_12)
        self.group_21.buttonClicked.connect(self.check_21)
        self.group_22.buttonClicked.connect(self.check_22)

    # Блок функций для кнопок

    # Блок присваивания коэффициентов
        
    # ko1
    def check_11(self):
        global ko1
        if self.radioButton.isChecked():
            ko1 = [1, 1]
        elif self.radioButton_2.isChecked():
            ko1 = [60, 1]
        elif self.radioButton_3.isChecked():
            ko1 = [3600, 1]
        elif self.radioButton_4.isChecked():
            ko1 = [0.0174532925, 1]
        elif self.radioButton_33.isChecked():
            ko1 = [1, 3]
        elif self.radioButton_34.isChecked():
            ko1 = [39.37, 3]
        elif self.radioButton_35.isChecked():
            ko1 = [3.28, 3]
        elif self.radioButton_36.isChecked():
            ko1 = [1.09, 3]
        elif self.radioButton_53.isChecked():
            ko1 = [0.000621, 3]
        elif self.radioButton_55.isChecked():
            ko1 = [1, 5]
        elif self.radioButton_56.isChecked():
            ko1 = [0.01, 5]
        elif self.radioButton_57.isChecked():
            ko1 = [0.0002471, 5]
        elif self.radioButton_58.isChecked():
            ko1 = [0.0001, 5]
        elif self.radioButton_63.isChecked():
            ko1 = [0.001, 7]
        elif self.radioButton_64.isChecked():
            ko1 = [1, 7]
        elif self.radioButton_65.isChecked():
            ko1 = [0.00629, 7]
        elif self.radioButton_66.isChecked():
            ko1 = [0.25, 7]
        elif self.radioButton_71.isChecked():
            ko1 = [1, 9]
        elif self.radioButton_72.isChecked():
            ko1 = [3.6, 9]
        elif self.radioButton_73.isChecked():
            ko1 = [2.237, 9]
        elif self.radioButton_74.isChecked():
            ko1 = [0.15, 9]
        elif self.radioButton_79.isChecked():
            ko1 = [1, 11]
        elif self.radioButton_80.isChecked():
            ko1 = [60 ** (- 1), 11]
        elif self.radioButton_81.isChecked():
            ko1 = [3600 ** (- 1), 11]
        elif self.radioButton_82.isChecked():
            ko1 = [86400 ** (- 1), 11]
        elif self.radioButton_83.isChecked():
            ko1 = [604800 ** (- 1), 11]
        elif self.radioButton_89.isChecked():
            ko1 = [220752000 ** (- 1), 11]
        elif self.radioButton_91.isChecked():
            ko1 = [1000, 13]
        elif self.radioButton_92.isChecked():
            ko1 = [1, 13]
        elif self.radioButton_93.isChecked():
            ko1 = [0.01, 13]
        elif self.radioButton_94.isChecked():
            ko1 = [0.001, 13]
        elif self.radioButton_95.isChecked():
            ko1 = [2.2, 13]
        elif self.radioButton_96.isChecked():
            ko1 = [35.273962, 13]
        elif self.radioButton_103.isChecked():
            ko1 = [1, 15]
        elif self.radioButton_104.isChecked():
            ko1 = [2, 15]
        elif self.radioButton_105.isChecked():
            ko1 = [3, 15]
        elif self.radioButton_106.isChecked():
            ko1 = [4, 15]
        elif self.radioButton_107.isChecked():
            ko1 = [5, 15]
            
    # ko2
    def check_12(self):
        global ko2
        if self.radioButton_5.isChecked():
            ko2 = [1, 2]
        elif self.radioButton_6.isChecked():
            ko2 = [60, 2]
        elif self.radioButton_7.isChecked():
            ko2 = [3600, 2]
        elif self.radioButton_8.isChecked():
            ko2 = [0.0174532925, 2]
        elif self.radioButton_49.isChecked():
            ko2 = [1, 4]
        elif self.radioButton_50.isChecked():
            ko2 = [39.37, 4]
        elif self.radioButton_51.isChecked():
            ko2 = [3.28, 4]
        elif self.radioButton_52.isChecked():
            ko2 = [1.09, 4]
        elif self.radioButton_54.isChecked():
            ko2 = [0.000621, 4]
        elif self.radioButton_59.isChecked():
            ko2 = [1, 6]
        elif self.radioButton_60.isChecked():
            ko2 = [0.01, 6]
        elif self.radioButton_61.isChecked():
            ko2 = [0.0002471, 6]
        elif self.radioButton_62.isChecked():
            ko2 = [0.0001, 6]
        elif self.radioButton_67.isChecked():
            ko2 = [0.001, 8]
        elif self.radioButton_68.isChecked():
            ko2 = [1, 8]
        elif self.radioButton_69.isChecked():
            ko2 = [0.00629, 8]
        elif self.radioButton_70.isChecked():
            ko2 = [0.25, 8]
        elif self.radioButton_75.isChecked():
            ko2 = [1, 10]
        elif self.radioButton_76.isChecked():
            ko2 = [3.6, 10]
        elif self.radioButton_77.isChecked():
            ko2 = [2.237, 10]
        elif self.radioButton_78.isChecked():
            ko2 = [0.15, 10]
        elif self.radioButton_84.isChecked():
            ko2 = [1, 12]
        elif self.radioButton_85.isChecked():
            ko2 = [60 ** (- 1), 12]
        elif self.radioButton_86.isChecked():
            ko2 = [3600 ** (- 1), 12]
        elif self.radioButton_87.isChecked():
            ko2 = [86400 ** (- 1), 12]
        elif self.radioButton_88.isChecked():
            ko2 = [604800 ** (- 1), 12]
        elif self.radioButton_90.isChecked():
            ko2 = [220752000 ** (- 1), 12]
        elif self.radioButton_100.isChecked():
            ko2 = [1000, 14]
        elif self.radioButton_101.isChecked():
            ko2 = [1, 14]
        elif self.radioButton_102.isChecked():
            ko2 = [0.01, 14]
        elif self.radioButton_97.isChecked():
            ko2 = [0.001, 14]
        elif self.radioButton_98.isChecked():
            ko2 = [2.2, 14]
        elif self.radioButton_99.isChecked():
            ko2 = [35.273962, 14]
        elif self.radioButton_108.isChecked():
            ko2 = [1, 16]
        elif self.radioButton_109.isChecked():
            ko2 = [2, 16]
        elif self.radioButton_110.isChecked():
            ko2 = [3, 16]
        elif self.radioButton_111.isChecked():
            ko2 = [4, 16]
        elif self.radioButton_112.isChecked():
            ko2 = [5, 16]

    # kd1
    def check_21(self):
        global kd1
        if self.radioButton_9.isChecked():
            kd1 = 10 ** (- 1)
        elif self.radioButton_10.isChecked():
            kd1 = 10 ** (- 2)
        elif self.radioButton_11.isChecked():
            kd1 = 10 ** (- 3)
        elif self.radioButton_12.isChecked():
            kd1 = 10 ** (- 6)
        elif self.radioButton_13.isChecked():
            kd1 = 10 ** (- 9)
        elif self.radioButton_14.isChecked():
            kd1 = 10 ** (- 12)
        elif self.radioButton_15.isChecked():
            kd1 = 10 ** 1
        elif self.radioButton_16.isChecked():
            kd1 = 10 ** 2
        elif self.radioButton_17.isChecked():
            kd1 = 10 ** 3
        elif self.radioButton_18.isChecked():
            kd1 = 10 ** 6
        elif self.radioButton_19.isChecked():
            kd1 = 10 ** 9
        elif self.radioButton_20.isChecked():
            kd1 = 10 ** 12
            
    # kd2
    def check_22(self):
        global kd2
        if self.radioButton_21.isChecked():
            kd2 = 10 ** (- 1)
        elif self.radioButton_26.isChecked():
            kd2 = 10 ** (- 2)
        elif self.radioButton_23.isChecked():
            kd2 = 10 ** (- 3)
        elif self.radioButton_24.isChecked():
            kd2 = 10 ** (- 6)
        elif self.radioButton_28.isChecked():
            kd2 = 10 ** (- 9)
        elif self.radioButton_27.isChecked():
            kd2 = 10 ** (- 12)
        elif self.radioButton_29.isChecked():
            kd2 = 10 ** 1
        elif self.radioButton_22.isChecked():
            kd2 = 10 ** 2
        elif self.radioButton_30.isChecked():
            kd2 = 10 ** 3
        elif self.radioButton_31.isChecked():
            kd2 = 10 ** 6
        elif self.radioButton_32.isChecked():
            kd2 = 10 ** 9
        elif self.radioButton_25.isChecked():
            kd2 = 10 ** 12

    # Конец блока присваивания коэффициентов

    # Функция очистки поля ввода
    def clear_1(self):
        self.lineEdit.clear()
        
    # Функция очистки поля вывода
    def clear_2(self):
        self.lineEdit_2.clear()
        
    # Функция сброса всех основных кнопок и коэффициентов
    def reset_o(self):
        global ko1
        global ko2
        ko1 = [0, 0]
        ko2 = [0, 0]
        self.group_11.setExclusive(False)
        self.group_12.setExclusive(False)
        self.radioButton.setChecked(False)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_4.setChecked(False)
        self.radioButton_5.setChecked(False)
        self.radioButton_6.setChecked(False)
        self.radioButton_7.setChecked(False)
        self.radioButton_8.setChecked(False)
        self.radioButton_33.setChecked(False)
        self.radioButton_34.setChecked(False)
        self.radioButton_35.setChecked(False)
        self.radioButton_36.setChecked(False)
        self.radioButton_49.setChecked(False)
        self.radioButton_50.setChecked(False)
        self.radioButton_51.setChecked(False)
        self.radioButton_52.setChecked(False)
        self.radioButton_53.setChecked(False)
        self.radioButton_54.setChecked(False)
        self.radioButton_55.setChecked(False)
        self.radioButton_56.setChecked(False)
        self.radioButton_57.setChecked(False)
        self.radioButton_58.setChecked(False)
        self.radioButton_59.setChecked(False)
        self.radioButton_60.setChecked(False)
        self.radioButton_61.setChecked(False)
        self.radioButton_62.setChecked(False)
        self.radioButton_63.setChecked(False)
        self.radioButton_64.setChecked(False)
        self.radioButton_65.setChecked(False)
        self.radioButton_66.setChecked(False)
        self.radioButton_67.setChecked(False)
        self.radioButton_68.setChecked(False)
        self.radioButton_69.setChecked(False)
        self.radioButton_70.setChecked(False)
        self.radioButton_71.setChecked(False)
        self.radioButton_72.setChecked(False)
        self.radioButton_73.setChecked(False)
        self.radioButton_74.setChecked(False)
        self.radioButton_75.setChecked(False)
        self.radioButton_76.setChecked(False)
        self.radioButton_77.setChecked(False)
        self.radioButton_78.setChecked(False)
        self.radioButton_79.setChecked(False)
        self.radioButton_80.setChecked(False)
        self.radioButton_81.setChecked(False)
        self.radioButton_82.setChecked(False)
        self.radioButton_83.setChecked(False)
        self.radioButton_84.setChecked(False)
        self.radioButton_85.setChecked(False)
        self.radioButton_86.setChecked(False)
        self.radioButton_87.setChecked(False)
        self.radioButton_88.setChecked(False)
        self.radioButton_89.setChecked(False)
        self.radioButton_90.setChecked(False)
        self.radioButton_91.setChecked(False)
        self.radioButton_92.setChecked(False)
        self.radioButton_93.setChecked(False)
        self.radioButton_94.setChecked(False)
        self.radioButton_95.setChecked(False)
        self.radioButton_96.setChecked(False)
        self.radioButton_97.setChecked(False)
        self.radioButton_98.setChecked(False)
        self.radioButton_99.setChecked(False)
        self.radioButton_100.setChecked(False)
        self.radioButton_101.setChecked(False)
        self.radioButton_102.setChecked(False)
        self.radioButton_103.setChecked(False)
        self.radioButton_104.setChecked(False)
        self.radioButton_105.setChecked(False)
        self.radioButton_106.setChecked(False)
        self.radioButton_107.setChecked(False)
        self.radioButton_108.setChecked(False)
        self.radioButton_109.setChecked(False)
        self.radioButton_110.setChecked(False)
        self.radioButton_111.setChecked(False)
        self.radioButton_112.setChecked(False)
        self.group_11.setExclusive(True)
        self.group_12.setExclusive(True)
        
    # Функция сброса всех дополнительных кнопок и коэффициентов
    def reset_d(self):
        global kd1
        global kd2
        kd1 = 1
        kd2 = 1
        self.group_21.setExclusive(False)
        self.group_22.setExclusive(False)
        self.radioButton_9.setChecked(False)
        self.radioButton_10.setChecked(False)
        self.radioButton_11.setChecked(False)
        self.radioButton_12.setChecked(False)
        self.radioButton_13.setChecked(False)
        self.radioButton_14.setChecked(False)
        self.radioButton_15.setChecked(False)
        self.radioButton_16.setChecked(False)
        self.radioButton_17.setChecked(False)
        self.radioButton_18.setChecked(False)
        self.radioButton_19.setChecked(False)
        self.radioButton_20.setChecked(False)
        self.radioButton_21.setChecked(False)
        self.radioButton_22.setChecked(False)
        self.radioButton_23.setChecked(False)
        self.radioButton_24.setChecked(False)
        self.radioButton_25.setChecked(False)
        self.radioButton_26.setChecked(False)
        self.radioButton_27.setChecked(False)
        self.radioButton_28.setChecked(False)
        self.radioButton_29.setChecked(False)
        self.radioButton_30.setChecked(False)
        self.radioButton_31.setChecked(False)
        self.radioButton_32.setChecked(False)
        self.group_21.setExclusive(True)
        self.group_22.setExclusive(True)
        
    # Функция перевода
    def perevod(self):
        global ko1
        global ko2
        global kd1
        global kd2
        global r
        if ko1[0] != 0 and ko2[0] != 0 and ko1[1] + 1 == ko2[1] and self.lineEdit.text() != '':
            f = 0
            if self.lineEdit.text().isdigit():
                f = 1
            elif '.' in self.lineEdit.text():
                if (self.lineEdit.text()[: self.lineEdit.text().find('.')] + self.lineEdit.text()[self.lineEdit.text().find('.') + 1 :]).isdigit():
                    f = 1
            if f:
                if ko1[1] != 15:
                    r = float(self.lineEdit.text()) * float('{:.15f}'.format(ko2[0] / ko1[0])) * (kd2 / kd1)
                    self.lineEdit_2.setText(str(float('{:.15f}'.format(r))))
                else:
                    if ko1[0] == 1:
                        s = float(self.lineEdit.text()) - 273.15
                    elif ko1[0] == 2:
                        s = float(self.lineEdit.text())
                    elif ko1[0] == 3:
                        s = (float(self.lineEdit.text()) - 32) * 5 / 9
                    elif ko1[0] == 4:
                        s = (float(self.lineEdit.text()) - 491.67) * 5 / 9
                    elif ko1[0] == 5:
                        s = float(self.lineEdit.text()) * 5 / 4
                    if ko2[0] == 1:
                        self.lineEdit_2.setText(str(float('{:.15f}'.format(s + 273.15))))
                    elif ko2[0] == 2:
                        self.lineEdit_2.setText(str(float('{:.15f}'.format(s))))
                    elif ko2[0] == 3:
                        self.lineEdit_2.setText(str(float('{:.15f}'.format(s * (9 / 5) + 32))))
                    elif ko2[0] == 4:
                        self.lineEdit_2.setText(str(float('{:.15f}'.format((s + 273.15) * (9 / 5)))))
                    elif ko2[0] == 5:
                        self.lineEdit_2.setText(str(float('{:.15f}'.format(s * 4 / 5))))
            else:
                self.lineEdit.setText('Ошибка! Попробуйте ещё раз.')
        else:
            self.lineEdit.setText('Ошибка! Попробуйте ещё раз.')

# Завершающий этап
if __name__ == "__main__":
    app = QApplication(sys.argv)
    res = Conv()
    res.show()
    sys.exit(app.exec())
