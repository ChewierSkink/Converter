# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(598, 410)
        MainWindow.setMinimumSize(QtCore.QSize(598, 410))
        MainWindow.setMaximumSize(QtCore.QSize(598, 410))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 130, 261, 161))
        self.tabWidget.setToolTipDuration(-3)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(0, 0, 131, 141))
        self.widget.setObjectName("widget")
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 70, 82, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.widget_2 = QtWidgets.QWidget(self.tab)
        self.widget_2.setGeometry(QtCore.QRect(130, 0, 131, 141))
        self.widget_2.setObjectName("widget_2")
        self.radioButton_5 = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_6.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_7.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_8.setGeometry(QtCore.QRect(10, 70, 82, 17))
        self.radioButton_8.setObjectName("radioButton_8")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget_3 = QtWidgets.QWidget(self.tab_2)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 131, 141))
        self.widget_3.setObjectName("widget_3")
        self.radioButton_33 = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton_33.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.radioButton_33.setObjectName("radioButton_33")
        self.radioButton_34 = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton_34.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.radioButton_34.setObjectName("radioButton_34")
        self.radioButton_35 = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton_35.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.radioButton_35.setObjectName("radioButton_35")
        self.radioButton_36 = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton_36.setGeometry(QtCore.QRect(10, 70, 82, 17))
        self.radioButton_36.setObjectName("radioButton_36")
        self.radioButton_53 = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton_53.setGeometry(QtCore.QRect(10, 90, 82, 17))
        self.radioButton_53.setObjectName("radioButton_53")
        self.widget_4 = QtWidgets.QWidget(self.tab_2)
        self.widget_4.setGeometry(QtCore.QRect(130, 0, 131, 141))
        self.widget_4.setObjectName("widget_4")
        self.radioButton_49 = QtWidgets.QRadioButton(self.widget_4)
        self.radioButton_49.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.radioButton_49.setObjectName("radioButton_49")
        self.radioButton_50 = QtWidgets.QRadioButton(self.widget_4)
        self.radioButton_50.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.radioButton_50.setObjectName("radioButton_50")
        self.radioButton_51 = QtWidgets.QRadioButton(self.widget_4)
        self.radioButton_51.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.radioButton_51.setObjectName("radioButton_51")
        self.radioButton_52 = QtWidgets.QRadioButton(self.widget_4)
        self.radioButton_52.setGeometry(QtCore.QRect(10, 70, 82, 17))
        self.radioButton_52.setObjectName("radioButton_52")
        self.radioButton_54 = QtWidgets.QRadioButton(self.widget_4)
        self.radioButton_54.setGeometry(QtCore.QRect(10, 90, 82, 17))
        self.radioButton_54.setObjectName("radioButton_54")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.widget_5 = QtWidgets.QWidget(self.tab_3)
        self.widget_5.setGeometry(QtCore.QRect(0, 0, 131, 141))
        self.widget_5.setObjectName("widget_5")
        self.radioButton_55 = QtWidgets.QRadioButton(self.widget_5)
        self.radioButton_55.setGeometry(QtCore.QRect(10, 10, 121, 17))
        self.radioButton_55.setObjectName("radioButton_55")
        self.radioButton_56 = QtWidgets.QRadioButton(self.widget_5)
        self.radioButton_56.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.radioButton_56.setObjectName("radioButton_56")
        self.radioButton_57 = QtWidgets.QRadioButton(self.widget_5)
        self.radioButton_57.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.radioButton_57.setObjectName("radioButton_57")
        self.radioButton_58 = QtWidgets.QRadioButton(self.widget_5)
        self.radioButton_58.setGeometry(QtCore.QRect(10, 70, 82, 17))
        self.radioButton_58.setObjectName("radioButton_58")
        self.widget_6 = QtWidgets.QWidget(self.tab_3)
        self.widget_6.setGeometry(QtCore.QRect(130, 0, 131, 141))
        self.widget_6.setObjectName("widget_6")
        self.radioButton_59 = QtWidgets.QRadioButton(self.widget_6)
        self.radioButton_59.setGeometry(QtCore.QRect(10, 10, 121, 17))
        self.radioButton_59.setObjectName("radioButton_59")
        self.radioButton_60 = QtWidgets.QRadioButton(self.widget_6)
        self.radioButton_60.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.radioButton_60.setObjectName("radioButton_60")
        self.radioButton_61 = QtWidgets.QRadioButton(self.widget_6)
        self.radioButton_61.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.radioButton_61.setObjectName("radioButton_61")
        self.radioButton_62 = QtWidgets.QRadioButton(self.widget_6)
        self.radioButton_62.setGeometry(QtCore.QRect(10, 70, 82, 17))
        self.radioButton_62.setObjectName("radioButton_62")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.widget_7 = QtWidgets.QWidget(self.tab_4)
        self.widget_7.setGeometry(QtCore.QRect(0, 0, 131, 141))
        self.widget_7.setObjectName("widget_7")
        self.radioButton_63 = QtWidgets.QRadioButton(self.widget_7)
        self.radioButton_63.setGeometry(QtCore.QRect(10, 10, 121, 17))
        self.radioButton_63.setObjectName("radioButton_63")
        self.radioButton_64 = QtWidgets.QRadioButton(self.widget_7)
        self.radioButton_64.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.radioButton_64.setObjectName("radioButton_64")
        self.radioButton_65 = QtWidgets.QRadioButton(self.widget_7)
        self.radioButton_65.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.radioButton_65.setObjectName("radioButton_65")
        self.radioButton_66 = QtWidgets.QRadioButton(self.widget_7)
        self.radioButton_66.setGeometry(QtCore.QRect(10, 70, 82, 17))
        self.radioButton_66.setObjectName("radioButton_66")
        self.widget_8 = QtWidgets.QWidget(self.tab_4)
        self.widget_8.setGeometry(QtCore.QRect(130, 0, 131, 141))
        self.widget_8.setObjectName("widget_8")
        self.radioButton_67 = QtWidgets.QRadioButton(self.widget_8)
        self.radioButton_67.setGeometry(QtCore.QRect(10, 10, 121, 17))
        self.radioButton_67.setObjectName("radioButton_67")
        self.radioButton_68 = QtWidgets.QRadioButton(self.widget_8)
        self.radioButton_68.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.radioButton_68.setObjectName("radioButton_68")
        self.radioButton_69 = QtWidgets.QRadioButton(self.widget_8)
        self.radioButton_69.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.radioButton_69.setObjectName("radioButton_69")
        self.radioButton_70 = QtWidgets.QRadioButton(self.widget_8)
        self.radioButton_70.setGeometry(QtCore.QRect(10, 70, 82, 17))
        self.radioButton_70.setObjectName("radioButton_70")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.widget_9 = QtWidgets.QWidget(self.tab_5)
        self.widget_9.setGeometry(QtCore.QRect(0, 0, 131, 141))
        self.widget_9.setObjectName("widget_9")
        self.radioButton_71 = QtWidgets.QRadioButton(self.widget_9)
        self.radioButton_71.setGeometry(QtCore.QRect(10, 10, 121, 17))
        self.radioButton_71.setObjectName("radioButton_71")
        self.radioButton_72 = QtWidgets.QRadioButton(self.widget_9)
        self.radioButton_72.setGeometry(QtCore.QRect(10, 30, 121, 17))
        self.radioButton_72.setObjectName("radioButton_72")
        self.radioButton_73 = QtWidgets.QRadioButton(self.widget_9)
        self.radioButton_73.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.radioButton_73.setObjectName("radioButton_73")
        self.radioButton_74 = QtWidgets.QRadioButton(self.widget_9)
        self.radioButton_74.setGeometry(QtCore.QRect(10, 70, 82, 17))
        self.radioButton_74.setObjectName("radioButton_74")
        self.widget_10 = QtWidgets.QWidget(self.tab_5)
        self.widget_10.setGeometry(QtCore.QRect(130, 0, 131, 141))
        self.widget_10.setObjectName("widget_10")
        self.radioButton_75 = QtWidgets.QRadioButton(self.widget_10)
        self.radioButton_75.setGeometry(QtCore.QRect(10, 10, 121, 17))
        self.radioButton_75.setObjectName("radioButton_75")
        self.radioButton_76 = QtWidgets.QRadioButton(self.widget_10)
        self.radioButton_76.setGeometry(QtCore.QRect(10, 30, 121, 17))
        self.radioButton_76.setObjectName("radioButton_76")
        self.radioButton_77 = QtWidgets.QRadioButton(self.widget_10)
        self.radioButton_77.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.radioButton_77.setObjectName("radioButton_77")
        self.radioButton_78 = QtWidgets.QRadioButton(self.widget_10)
        self.radioButton_78.setGeometry(QtCore.QRect(10, 70, 82, 17))
        self.radioButton_78.setObjectName("radioButton_78")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.widget_11 = QtWidgets.QWidget(self.tab_6)
        self.widget_11.setGeometry(QtCore.QRect(0, 0, 131, 141))
        self.widget_11.setObjectName("widget_11")
        self.radioButton_79 = QtWidgets.QRadioButton(self.widget_11)
        self.radioButton_79.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.radioButton_79.setObjectName("radioButton_79")
        self.radioButton_80 = QtWidgets.QRadioButton(self.widget_11)
        self.radioButton_80.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.radioButton_80.setObjectName("radioButton_80")
        self.radioButton_81 = QtWidgets.QRadioButton(self.widget_11)
        self.radioButton_81.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.radioButton_81.setObjectName("radioButton_81")
        self.radioButton_82 = QtWidgets.QRadioButton(self.widget_11)
        self.radioButton_82.setGeometry(QtCore.QRect(10, 70, 82, 17))
        self.radioButton_82.setObjectName("radioButton_82")
        self.radioButton_83 = QtWidgets.QRadioButton(self.widget_11)
        self.radioButton_83.setGeometry(QtCore.QRect(10, 90, 82, 17))
        self.radioButton_83.setObjectName("radioButton_83")
        self.radioButton_89 = QtWidgets.QRadioButton(self.widget_11)
        self.radioButton_89.setGeometry(QtCore.QRect(10, 110, 82, 17))
        self.radioButton_89.setObjectName("radioButton_89")
        self.widget_12 = QtWidgets.QWidget(self.tab_6)
        self.widget_12.setGeometry(QtCore.QRect(130, 0, 131, 141))
        self.widget_12.setObjectName("widget_12")
        self.radioButton_84 = QtWidgets.QRadioButton(self.widget_12)
        self.radioButton_84.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.radioButton_84.setObjectName("radioButton_84")
        self.radioButton_85 = QtWidgets.QRadioButton(self.widget_12)
        self.radioButton_85.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.radioButton_85.setObjectName("radioButton_85")
        self.radioButton_86 = QtWidgets.QRadioButton(self.widget_12)
        self.radioButton_86.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.radioButton_86.setObjectName("radioButton_86")
        self.radioButton_87 = QtWidgets.QRadioButton(self.widget_12)
        self.radioButton_87.setGeometry(QtCore.QRect(10, 70, 82, 17))
        self.radioButton_87.setObjectName("radioButton_87")
        self.radioButton_88 = QtWidgets.QRadioButton(self.widget_12)
        self.radioButton_88.setGeometry(QtCore.QRect(10, 90, 82, 17))
        self.radioButton_88.setObjectName("radioButton_88")
        self.radioButton_90 = QtWidgets.QRadioButton(self.widget_12)
        self.radioButton_90.setGeometry(QtCore.QRect(10, 110, 82, 17))
        self.radioButton_90.setObjectName("radioButton_90")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.widget_13 = QtWidgets.QWidget(self.tab_7)
        self.widget_13.setGeometry(QtCore.QRect(0, 0, 131, 141))
        self.widget_13.setObjectName("widget_13")
        self.radioButton_91 = QtWidgets.QRadioButton(self.widget_13)
        self.radioButton_91.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.radioButton_91.setObjectName("radioButton_91")
        self.radioButton_92 = QtWidgets.QRadioButton(self.widget_13)
        self.radioButton_92.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.radioButton_92.setObjectName("radioButton_92")
        self.radioButton_93 = QtWidgets.QRadioButton(self.widget_13)
        self.radioButton_93.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.radioButton_93.setObjectName("radioButton_93")
        self.radioButton_94 = QtWidgets.QRadioButton(self.widget_13)
        self.radioButton_94.setGeometry(QtCore.QRect(10, 70, 82, 17))
        self.radioButton_94.setObjectName("radioButton_94")
        self.radioButton_95 = QtWidgets.QRadioButton(self.widget_13)
        self.radioButton_95.setGeometry(QtCore.QRect(10, 90, 82, 17))
        self.radioButton_95.setObjectName("radioButton_95")
        self.radioButton_96 = QtWidgets.QRadioButton(self.widget_13)
        self.radioButton_96.setGeometry(QtCore.QRect(10, 110, 82, 17))
        self.radioButton_96.setObjectName("radioButton_96")
        self.widget_14 = QtWidgets.QWidget(self.tab_7)
        self.widget_14.setGeometry(QtCore.QRect(130, 0, 131, 141))
        self.widget_14.setObjectName("widget_14")
        self.radioButton_97 = QtWidgets.QRadioButton(self.widget_14)
        self.radioButton_97.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.radioButton_97.setObjectName("radioButton_97")
        self.radioButton_98 = QtWidgets.QRadioButton(self.widget_14)
        self.radioButton_98.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.radioButton_98.setObjectName("radioButton_98")
        self.radioButton_99 = QtWidgets.QRadioButton(self.widget_14)
        self.radioButton_99.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.radioButton_99.setObjectName("radioButton_99")
        self.radioButton_100 = QtWidgets.QRadioButton(self.widget_14)
        self.radioButton_100.setGeometry(QtCore.QRect(10, 70, 82, 17))
        self.radioButton_100.setObjectName("radioButton_100")
        self.radioButton_101 = QtWidgets.QRadioButton(self.widget_14)
        self.radioButton_101.setGeometry(QtCore.QRect(10, 90, 82, 17))
        self.radioButton_101.setObjectName("radioButton_101")
        self.radioButton_102 = QtWidgets.QRadioButton(self.widget_14)
        self.radioButton_102.setGeometry(QtCore.QRect(10, 110, 82, 17))
        self.radioButton_102.setObjectName("radioButton_102")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.widget_15 = QtWidgets.QWidget(self.tab_8)
        self.widget_15.setGeometry(QtCore.QRect(0, 0, 131, 141))
        self.widget_15.setObjectName("widget_15")
        self.radioButton_103 = QtWidgets.QRadioButton(self.widget_15)
        self.radioButton_103.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.radioButton_103.setObjectName("radioButton_103")
        self.radioButton_104 = QtWidgets.QRadioButton(self.widget_15)
        self.radioButton_104.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.radioButton_104.setObjectName("radioButton_104")
        self.radioButton_105 = QtWidgets.QRadioButton(self.widget_15)
        self.radioButton_105.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.radioButton_105.setObjectName("radioButton_105")
        self.radioButton_106 = QtWidgets.QRadioButton(self.widget_15)
        self.radioButton_106.setGeometry(QtCore.QRect(10, 70, 82, 17))
        self.radioButton_106.setObjectName("radioButton_106")
        self.radioButton_107 = QtWidgets.QRadioButton(self.widget_15)
        self.radioButton_107.setGeometry(QtCore.QRect(10, 90, 82, 17))
        self.radioButton_107.setObjectName("radioButton_107")
        self.widget_16 = QtWidgets.QWidget(self.tab_8)
        self.widget_16.setGeometry(QtCore.QRect(130, 0, 131, 141))
        self.widget_16.setObjectName("widget_16")
        self.radioButton_108 = QtWidgets.QRadioButton(self.widget_16)
        self.radioButton_108.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.radioButton_108.setObjectName("radioButton_108")
        self.radioButton_109 = QtWidgets.QRadioButton(self.widget_16)
        self.radioButton_109.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.radioButton_109.setObjectName("radioButton_109")
        self.radioButton_110 = QtWidgets.QRadioButton(self.widget_16)
        self.radioButton_110.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.radioButton_110.setObjectName("radioButton_110")
        self.radioButton_111 = QtWidgets.QRadioButton(self.widget_16)
        self.radioButton_111.setGeometry(QtCore.QRect(10, 70, 82, 17))
        self.radioButton_111.setObjectName("radioButton_111")
        self.radioButton_112 = QtWidgets.QRadioButton(self.widget_16)
        self.radioButton_112.setGeometry(QtCore.QRect(10, 90, 82, 17))
        self.radioButton_112.setObjectName("radioButton_112")
        self.tabWidget.addTab(self.tab_8, "")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 360, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 290, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 290, 101, 16))
        self.label_2.setObjectName("label_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(320, 130, 261, 161))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.radioButton_9 = QtWidgets.QRadioButton(self.tab_11)
        self.radioButton_9.setGeometry(QtCore.QRect(10, 10, 91, 17))
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioButton_10 = QtWidgets.QRadioButton(self.tab_11)
        self.radioButton_10.setGeometry(QtCore.QRect(10, 30, 91, 17))
        self.radioButton_10.setObjectName("radioButton_10")
        self.radioButton_11 = QtWidgets.QRadioButton(self.tab_11)
        self.radioButton_11.setGeometry(QtCore.QRect(10, 50, 91, 17))
        self.radioButton_11.setObjectName("radioButton_11")
        self.radioButton_12 = QtWidgets.QRadioButton(self.tab_11)
        self.radioButton_12.setGeometry(QtCore.QRect(10, 70, 91, 17))
        self.radioButton_12.setObjectName("radioButton_12")
        self.radioButton_13 = QtWidgets.QRadioButton(self.tab_11)
        self.radioButton_13.setGeometry(QtCore.QRect(10, 90, 91, 17))
        self.radioButton_13.setObjectName("radioButton_13")
        self.radioButton_14 = QtWidgets.QRadioButton(self.tab_11)
        self.radioButton_14.setGeometry(QtCore.QRect(10, 110, 91, 17))
        self.radioButton_14.setObjectName("radioButton_14")
        self.radioButton_15 = QtWidgets.QRadioButton(self.tab_11)
        self.radioButton_15.setGeometry(QtCore.QRect(140, 10, 101, 17))
        self.radioButton_15.setObjectName("radioButton_15")
        self.radioButton_16 = QtWidgets.QRadioButton(self.tab_11)
        self.radioButton_16.setGeometry(QtCore.QRect(140, 30, 101, 17))
        self.radioButton_16.setObjectName("radioButton_16")
        self.radioButton_17 = QtWidgets.QRadioButton(self.tab_11)
        self.radioButton_17.setGeometry(QtCore.QRect(140, 50, 101, 17))
        self.radioButton_17.setObjectName("radioButton_17")
        self.radioButton_18 = QtWidgets.QRadioButton(self.tab_11)
        self.radioButton_18.setGeometry(QtCore.QRect(140, 70, 101, 17))
        self.radioButton_18.setObjectName("radioButton_18")
        self.radioButton_19 = QtWidgets.QRadioButton(self.tab_11)
        self.radioButton_19.setGeometry(QtCore.QRect(140, 90, 101, 17))
        self.radioButton_19.setObjectName("radioButton_19")
        self.radioButton_20 = QtWidgets.QRadioButton(self.tab_11)
        self.radioButton_20.setGeometry(QtCore.QRect(140, 110, 101, 17))
        self.radioButton_20.setObjectName("radioButton_20")
        self.tabWidget_2.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.radioButton_21 = QtWidgets.QRadioButton(self.tab_12)
        self.radioButton_21.setGeometry(QtCore.QRect(10, 10, 91, 17))
        self.radioButton_21.setObjectName("radioButton_21")
        self.radioButton_22 = QtWidgets.QRadioButton(self.tab_12)
        self.radioButton_22.setGeometry(QtCore.QRect(140, 30, 101, 17))
        self.radioButton_22.setObjectName("radioButton_22")
        self.radioButton_23 = QtWidgets.QRadioButton(self.tab_12)
        self.radioButton_23.setGeometry(QtCore.QRect(10, 50, 91, 17))
        self.radioButton_23.setObjectName("radioButton_23")
        self.radioButton_24 = QtWidgets.QRadioButton(self.tab_12)
        self.radioButton_24.setGeometry(QtCore.QRect(10, 70, 91, 17))
        self.radioButton_24.setObjectName("radioButton_24")
        self.radioButton_25 = QtWidgets.QRadioButton(self.tab_12)
        self.radioButton_25.setGeometry(QtCore.QRect(140, 110, 101, 17))
        self.radioButton_25.setObjectName("radioButton_25")
        self.radioButton_26 = QtWidgets.QRadioButton(self.tab_12)
        self.radioButton_26.setGeometry(QtCore.QRect(10, 30, 91, 17))
        self.radioButton_26.setObjectName("radioButton_26")
        self.radioButton_27 = QtWidgets.QRadioButton(self.tab_12)
        self.radioButton_27.setGeometry(QtCore.QRect(10, 110, 91, 17))
        self.radioButton_27.setObjectName("radioButton_27")
        self.radioButton_28 = QtWidgets.QRadioButton(self.tab_12)
        self.radioButton_28.setGeometry(QtCore.QRect(10, 90, 91, 17))
        self.radioButton_28.setObjectName("radioButton_28")
        self.radioButton_29 = QtWidgets.QRadioButton(self.tab_12)
        self.radioButton_29.setGeometry(QtCore.QRect(140, 10, 101, 17))
        self.radioButton_29.setObjectName("radioButton_29")
        self.radioButton_30 = QtWidgets.QRadioButton(self.tab_12)
        self.radioButton_30.setGeometry(QtCore.QRect(140, 50, 101, 17))
        self.radioButton_30.setObjectName("radioButton_30")
        self.radioButton_31 = QtWidgets.QRadioButton(self.tab_12)
        self.radioButton_31.setGeometry(QtCore.QRect(140, 70, 101, 17))
        self.radioButton_31.setObjectName("radioButton_31")
        self.radioButton_32 = QtWidgets.QRadioButton(self.tab_12)
        self.radioButton_32.setGeometry(QtCore.QRect(140, 90, 101, 17))
        self.radioButton_32.setObjectName("radioButton_32")
        self.tabWidget_2.addTab(self.tab_12, "")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 320, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 10, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 320, 181, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 90, 261, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(306, 290, 291, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(320, 90, 261, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Конвертер"))
        self.radioButton.setText(_translate("MainWindow", "Градус"))
        self.radioButton_2.setText(_translate("MainWindow", "Минуты"))
        self.radioButton_3.setText(_translate("MainWindow", "Секунды"))
        self.radioButton_4.setText(_translate("MainWindow", "Радианы"))
        self.radioButton_5.setText(_translate("MainWindow", "Градус"))
        self.radioButton_6.setText(_translate("MainWindow", "Минуты"))
        self.radioButton_7.setText(_translate("MainWindow", "Секунды"))
        self.radioButton_8.setText(_translate("MainWindow", "Радианы"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Угол"))
        self.radioButton_33.setText(_translate("MainWindow", "Метр"))
        self.radioButton_34.setText(_translate("MainWindow", "Дюйм"))
        self.radioButton_35.setText(_translate("MainWindow", "Фут"))
        self.radioButton_36.setText(_translate("MainWindow", "Ярд"))
        self.radioButton_53.setText(_translate("MainWindow", "Миля"))
        self.radioButton_49.setText(_translate("MainWindow", "Метр"))
        self.radioButton_50.setText(_translate("MainWindow", "Дюйм"))
        self.radioButton_51.setText(_translate("MainWindow", "Фут"))
        self.radioButton_52.setText(_translate("MainWindow", "Ярд"))
        self.radioButton_54.setText(_translate("MainWindow", "Миля"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Длина"))
        self.radioButton_55.setText(_translate("MainWindow", "Метр квадратный"))
        self.radioButton_56.setText(_translate("MainWindow", "Ар"))
        self.radioButton_57.setText(_translate("MainWindow", "Акр"))
        self.radioButton_58.setText(_translate("MainWindow", "Гектар"))
        self.radioButton_59.setText(_translate("MainWindow", "Метр квадратный"))
        self.radioButton_60.setText(_translate("MainWindow", "Ар"))
        self.radioButton_61.setText(_translate("MainWindow", "Акр"))
        self.radioButton_62.setText(_translate("MainWindow", "Гектар"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Площадь"))
        self.radioButton_63.setText(_translate("MainWindow", "Метр кубический"))
        self.radioButton_64.setText(_translate("MainWindow", "Литр"))
        self.radioButton_65.setText(_translate("MainWindow", "Баррель"))
        self.radioButton_66.setText(_translate("MainWindow", "Галлон"))
        self.radioButton_67.setText(_translate("MainWindow", "Метр кубический"))
        self.radioButton_68.setText(_translate("MainWindow", "Литр"))
        self.radioButton_69.setText(_translate("MainWindow", "Баррель"))
        self.radioButton_70.setText(_translate("MainWindow", "Галлон"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Объём"))
        self.radioButton_71.setText(_translate("MainWindow", "Метры в секунду"))
        self.radioButton_72.setText(_translate("MainWindow", "Километры в час"))
        self.radioButton_73.setText(_translate("MainWindow", "Миль в час"))
        self.radioButton_74.setText(_translate("MainWindow", "Узел"))
        self.radioButton_75.setText(_translate("MainWindow", "Метры в секунду"))
        self.radioButton_76.setText(_translate("MainWindow", "Километры в час"))
        self.radioButton_77.setText(_translate("MainWindow", "Миль в час"))
        self.radioButton_78.setText(_translate("MainWindow", "Узел"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Скорость"))
        self.radioButton_79.setText(_translate("MainWindow", "Секунда"))
        self.radioButton_80.setText(_translate("MainWindow", "Минута"))
        self.radioButton_81.setText(_translate("MainWindow", "Час"))
        self.radioButton_82.setText(_translate("MainWindow", "День"))
        self.radioButton_83.setText(_translate("MainWindow", "Неделя"))
        self.radioButton_89.setText(_translate("MainWindow", "Год"))
        self.radioButton_84.setText(_translate("MainWindow", "Секунда"))
        self.radioButton_85.setText(_translate("MainWindow", "Минута"))
        self.radioButton_86.setText(_translate("MainWindow", "Час"))
        self.radioButton_87.setText(_translate("MainWindow", "День"))
        self.radioButton_88.setText(_translate("MainWindow", "Неделя"))
        self.radioButton_90.setText(_translate("MainWindow", "Год"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Время"))
        self.radioButton_91.setText(_translate("MainWindow", "Грамм"))
        self.radioButton_92.setText(_translate("MainWindow", "Килограмм"))
        self.radioButton_93.setText(_translate("MainWindow", "Центнер"))
        self.radioButton_94.setText(_translate("MainWindow", "Тонна"))
        self.radioButton_95.setText(_translate("MainWindow", "Фунт"))
        self.radioButton_96.setText(_translate("MainWindow", "Унция"))
        self.radioButton_97.setText(_translate("MainWindow", "Грамм"))
        self.radioButton_98.setText(_translate("MainWindow", "Килограмм"))
        self.radioButton_99.setText(_translate("MainWindow", "Центнер"))
        self.radioButton_100.setText(_translate("MainWindow", "Тонна"))
        self.radioButton_101.setText(_translate("MainWindow", "Фунт"))
        self.radioButton_102.setText(_translate("MainWindow", "Унция"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Вес"))
        self.radioButton_103.setText(_translate("MainWindow", "Кельвин"))
        self.radioButton_104.setText(_translate("MainWindow", "Цельсия"))
        self.radioButton_105.setText(_translate("MainWindow", "Фаренгейт"))
        self.radioButton_106.setText(_translate("MainWindow", "Ранкин"))
        self.radioButton_107.setText(_translate("MainWindow", "Реомюр"))
        self.radioButton_108.setText(_translate("MainWindow", "Кельвин"))
        self.radioButton_109.setText(_translate("MainWindow", "Цельсия"))
        self.radioButton_110.setText(_translate("MainWindow", "Фаренгейт"))
        self.radioButton_111.setText(_translate("MainWindow", "Ранкин"))
        self.radioButton_112.setText(_translate("MainWindow", "Реомюр"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "Температура"))
        self.pushButton.setText(_translate("MainWindow", "Перевод"))
        self.label.setText(_translate("MainWindow", "Что переводить"))
        self.label_2.setText(_translate("MainWindow", "Во что переводить"))
        self.radioButton_9.setText(_translate("MainWindow", "Дека (10^1)"))
        self.radioButton_10.setText(_translate("MainWindow", "Гекто (10^2)"))
        self.radioButton_11.setText(_translate("MainWindow", "Кило (10^3)"))
        self.radioButton_12.setText(_translate("MainWindow", "Мега (10^6)"))
        self.radioButton_13.setText(_translate("MainWindow", "Гига (10^9)"))
        self.radioButton_14.setText(_translate("MainWindow", "Тера (10^12)"))
        self.radioButton_15.setText(_translate("MainWindow", "Деци (10^-1)"))
        self.radioButton_16.setText(_translate("MainWindow", "Санти (10^-2)"))
        self.radioButton_17.setText(_translate("MainWindow", "Мили (10^-3)"))
        self.radioButton_18.setText(_translate("MainWindow", "Микро (10^-6)"))
        self.radioButton_19.setText(_translate("MainWindow", "Нано (10^-9)"))
        self.radioButton_20.setText(_translate("MainWindow", "Пико (10^-12)"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_11), _translate("MainWindow", "Начальный доп. коэффициент"))
        self.radioButton_21.setText(_translate("MainWindow", "Дека (10^1)"))
        self.radioButton_22.setText(_translate("MainWindow", "Санти (10^-2)"))
        self.radioButton_23.setText(_translate("MainWindow", "Кило (10^3)"))
        self.radioButton_24.setText(_translate("MainWindow", "Мега (10^6)"))
        self.radioButton_25.setText(_translate("MainWindow", "Пико (10^-12)"))
        self.radioButton_26.setText(_translate("MainWindow", "Гекто (10^2)"))
        self.radioButton_27.setText(_translate("MainWindow", "Тера (10^12)"))
        self.radioButton_28.setText(_translate("MainWindow", "Гига (10^9)"))
        self.radioButton_29.setText(_translate("MainWindow", "Деци (10^-1)"))
        self.radioButton_30.setText(_translate("MainWindow", "Мили (10^-3)"))
        self.radioButton_31.setText(_translate("MainWindow", "Микро (10^-6)"))
        self.radioButton_32.setText(_translate("MainWindow", "Нано (10^-9)"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_12), _translate("MainWindow", "Конечный доп. коэффициент"))
        self.pushButton_2.setText(_translate("MainWindow", "Сбросить"))
        self.pushButton_3.setText(_translate("MainWindow", "Сбросить доп. коэффициенты"))
        self.pushButton_4.setText(_translate("MainWindow", "Очистить поле"))
        self.label_3.setText(_translate("MainWindow", "Дополнительные коэффициенты (вначале оба равны 1)"))
        self.pushButton_5.setText(_translate("MainWindow", "Очистить поле"))

