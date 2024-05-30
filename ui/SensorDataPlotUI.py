# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SensorDataPlotUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(803, 81)
        Form.setMinimumSize(QSize(0, 20))
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cbxChangePlot = QComboBox(Form)
        self.cbxChangePlot.addItem("")
        self.cbxChangePlot.addItem("")
        self.cbxChangePlot.addItem("")
        self.cbxChangePlot.addItem("")
        self.cbxChangePlot.addItem("")
        self.cbxChangePlot.setObjectName(u"cbxChangePlot")
        self.cbxChangePlot.setMinimumSize(QSize(180, 30))
        self.cbxChangePlot.setMaximumSize(QSize(16777215, 16777215))
        self.cbxChangePlot.setStyleSheet(u"font: 75 9pt \"Arial\";")

        self.horizontalLayout.addWidget(self.cbxChangePlot)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnPullData = QPushButton(Form)
        self.btnPullData.setObjectName(u"btnPullData")
        self.btnPullData.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.btnPullData)

        self.btnUpdatePlot = QPushButton(Form)
        self.btnUpdatePlot.setObjectName(u"btnUpdatePlot")
        self.btnUpdatePlot.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.btnUpdatePlot)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.cbxChangePlot.setItemText(0, QCoreApplication.translate("Form", u"x:Date   y:AirTemp", None))
        self.cbxChangePlot.setItemText(1, QCoreApplication.translate("Form", u"x:Date   y:AirHum", None))
        self.cbxChangePlot.setItemText(2, QCoreApplication.translate("Form", u"x:Date   y:WaterTemp", None))
        self.cbxChangePlot.setItemText(3, QCoreApplication.translate("Form", u"x:Date   y:WaterDO", None))
        self.cbxChangePlot.setItemText(4, QCoreApplication.translate("Form", u"x:Date   y:WaterPH", None))

        self.btnPullData.setText(QCoreApplication.translate("Form", u"\u62c9\u53d6\u6578\u64da", None))
        self.btnUpdatePlot.setText(QCoreApplication.translate("Form", u"\u66f4\u65b0\u66f2\u7dda\u5716", None))
    # retranslateUi

