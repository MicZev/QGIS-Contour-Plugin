# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmContour.ui'
#
# Created: Thu Sep 11 10:51:28 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ContourDialog(object):
    def setupUi(self, ContourDialog):
        ContourDialog.setObjectName(_fromUtf8("ContourDialog"))
        ContourDialog.setWindowModality(QtCore.Qt.NonModal)
        ContourDialog.resize(506, 532)
        ContourDialog.setSizeGripEnabled(True)
        self.gridLayout_3 = QtGui.QGridLayout(ContourDialog)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox_2 = QtGui.QGroupBox(ContourDialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.uThinPoints = QtGui.QCheckBox(self.groupBox_2)
        self.uThinPoints.setText(_fromUtf8(""))
        self.uThinPoints.setObjectName(_fromUtf8("uThinPoints"))
        self.horizontalLayout.addWidget(self.uThinPoints)
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout.addWidget(self.label_11)
        self.uThinRadius = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.uThinRadius.setDecimals(6)
        self.uThinRadius.setSingleStep(1e-06)
        self.uThinRadius.setObjectName(_fromUtf8("uThinRadius"))
        self.horizontalLayout.addWidget(self.uThinRadius)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.uLayerDescription = QtGui.QLabel(self.groupBox_2)
        self.uLayerDescription.setText(_fromUtf8(""))
        self.uLayerDescription.setObjectName(_fromUtf8("uLayerDescription"))
        self.gridLayout.addWidget(self.uLayerDescription, 1, 0, 1, 1)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.uLayerName = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uLayerName.sizePolicy().hasHeightForWidth())
        self.uLayerName.setSizePolicy(sizePolicy)
        self.uLayerName.setStatusTip(_fromUtf8(""))
        self.uLayerName.setObjectName(_fromUtf8("uLayerName"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.uLayerName)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.uFieldName = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uFieldName.sizePolicy().hasHeightForWidth())
        self.uFieldName.setSizePolicy(sizePolicy)
        self.uFieldName.setObjectName(_fromUtf8("uFieldName"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.uFieldName)
        self.gridLayout.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 2)
        self.groupBox = QtGui.QGroupBox(ContourDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.uLinesContours = QtGui.QRadioButton(self.groupBox)
        self.uLinesContours.setObjectName(_fromUtf8("uLinesContours"))
        self.horizontalLayout_7.addWidget(self.uLinesContours)
        self.uFilledContours = QtGui.QRadioButton(self.groupBox)
        self.uFilledContours.setObjectName(_fromUtf8("uFilledContours"))
        self.horizontalLayout_7.addWidget(self.uFilledContours)
        self.uBoth = QtGui.QRadioButton(self.groupBox)
        self.uBoth.setObjectName(_fromUtf8("uBoth"))
        self.horizontalLayout_7.addWidget(self.uBoth)
        self.uLayerContours = QtGui.QRadioButton(self.groupBox)
        self.uLayerContours.setObjectName(_fromUtf8("uLayerContours"))
        self.horizontalLayout_7.addWidget(self.uLayerContours)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 0, 0, 1, 3)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.uLevelsNumber = QtGui.QSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uLevelsNumber.sizePolicy().hasHeightForWidth())
        self.uLevelsNumber.setSizePolicy(sizePolicy)
        self.uLevelsNumber.setMinimum(1)
        self.uLevelsNumber.setMaximum(999)
        self.uLevelsNumber.setObjectName(_fromUtf8("uLevelsNumber"))
        self.gridLayout_2.addWidget(self.uLevelsNumber, 1, 1, 1, 1)
        self.uLevelsList = QtGui.QListWidget(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uLevelsList.sizePolicy().hasHeightForWidth())
        self.uLevelsList.setSizePolicy(sizePolicy)
        self.uLevelsList.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.uLevelsList.setObjectName(_fromUtf8("uLevelsList"))
        self.gridLayout_2.addWidget(self.uLevelsList, 1, 2, 5, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.uMinContour = QtGui.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uMinContour.sizePolicy().hasHeightForWidth())
        self.uMinContour.setSizePolicy(sizePolicy)
        self.uMinContour.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.uMinContour.setDecimals(4)
        self.uMinContour.setMinimum(-999999999.0)
        self.uMinContour.setMaximum(999999999.0)
        self.uMinContour.setObjectName(_fromUtf8("uMinContour"))
        self.gridLayout_2.addWidget(self.uMinContour, 2, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.uMaxContour = QtGui.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uMaxContour.sizePolicy().hasHeightForWidth())
        self.uMaxContour.setSizePolicy(sizePolicy)
        self.uMaxContour.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.uMaxContour.setDecimals(4)
        self.uMaxContour.setMinimum(-999999999.0)
        self.uMaxContour.setMaximum(999999999.0)
        self.uMaxContour.setObjectName(_fromUtf8("uMaxContour"))
        self.gridLayout_2.addWidget(self.uMaxContour, 3, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 4, 0, 1, 1)
        self.uExtend = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uExtend.sizePolicy().hasHeightForWidth())
        self.uExtend.setSizePolicy(sizePolicy)
        self.uExtend.setObjectName(_fromUtf8("uExtend"))
        self.uExtend.addItem(_fromUtf8(""))
        self.uExtend.addItem(_fromUtf8(""))
        self.uExtend.addItem(_fromUtf8(""))
        self.uExtend.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.uExtend, 4, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 5, 0, 1, 1)
        self.uMethod = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uMethod.sizePolicy().hasHeightForWidth())
        self.uMethod.setSizePolicy(sizePolicy)
        self.uMethod.setObjectName(_fromUtf8("uMethod"))
        self.uMethod.addItem(_fromUtf8(""))
        self.uMethod.addItem(_fromUtf8(""))
        self.uMethod.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.uMethod, 5, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 2)
        self.groupBox_3 = QtGui.QGroupBox(ContourDialog)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_8)
        self.uOutputName = QtGui.QLineEdit(self.groupBox_3)
        self.uOutputName.setObjectName(_fromUtf8("uOutputName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.uOutputName)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.uPrecision = QtGui.QSpinBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uPrecision.sizePolicy().hasHeightForWidth())
        self.uPrecision.setSizePolicy(sizePolicy)
        self.uPrecision.setMinimum(0)
        self.uPrecision.setMaximum(4)
        self.uPrecision.setProperty("value", 4)
        self.uPrecision.setObjectName(_fromUtf8("uPrecision"))
        self.horizontalLayout_2.addWidget(self.uPrecision)
        self.label_12 = QtGui.QLabel(self.groupBox_3)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_2.addWidget(self.label_12)
        self.uLabelUnits = QtGui.QLineEdit(self.groupBox_3)
        self.uLabelUnits.setObjectName(_fromUtf8("uLabelUnits"))
        self.horizontalLayout_2.addWidget(self.uLabelUnits)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_9)
        self.gridLayout_4.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_3, 2, 0, 1, 2)
        self.progressBar = QtGui.QProgressBar(ContourDialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout_3.addWidget(self.progressBar, 3, 0, 1, 1)
        self.uButtonBox = QtGui.QDialogButtonBox(ContourDialog)
        self.uButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.uButtonBox.setObjectName(_fromUtf8("uButtonBox"))
        self.gridLayout_3.addWidget(self.uButtonBox, 3, 1, 1, 1)
        self.label_2.setBuddy(self.uThinPoints)
        self.label_11.setBuddy(self.uThinRadius)
        self.label_3.setBuddy(self.uLayerName)
        self.label_4.setBuddy(self.uFieldName)
        self.label.setBuddy(self.uLevelsNumber)
        self.label_5.setBuddy(self.uMinContour)
        self.label_6.setBuddy(self.uMaxContour)
        self.label_10.setBuddy(self.uExtend)
        self.label_7.setBuddy(self.uMethod)
        self.label_8.setBuddy(self.uOutputName)
        self.label_12.setBuddy(self.uLabelUnits)
        self.label_9.setBuddy(self.uPrecision)

        self.retranslateUi(ContourDialog)
        QtCore.QObject.connect(self.uButtonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ContourDialog.accept)
        QtCore.QObject.connect(self.uButtonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ContourDialog.close)
        QtCore.QMetaObject.connectSlotsByName(ContourDialog)
        ContourDialog.setTabOrder(self.uLayerName, self.uFieldName)
        ContourDialog.setTabOrder(self.uFieldName, self.uThinPoints)
        ContourDialog.setTabOrder(self.uThinPoints, self.uThinRadius)
        ContourDialog.setTabOrder(self.uThinRadius, self.uLinesContours)
        ContourDialog.setTabOrder(self.uLinesContours, self.uFilledContours)
        ContourDialog.setTabOrder(self.uFilledContours, self.uBoth)
        ContourDialog.setTabOrder(self.uBoth, self.uLayerContours)
        ContourDialog.setTabOrder(self.uLayerContours, self.uLevelsNumber)
        ContourDialog.setTabOrder(self.uLevelsNumber, self.uLevelsList)
        ContourDialog.setTabOrder(self.uLevelsList, self.uMinContour)
        ContourDialog.setTabOrder(self.uMinContour, self.uMaxContour)
        ContourDialog.setTabOrder(self.uMaxContour, self.uExtend)
        ContourDialog.setTabOrder(self.uExtend, self.uMethod)
        ContourDialog.setTabOrder(self.uMethod, self.uOutputName)
        ContourDialog.setTabOrder(self.uOutputName, self.uPrecision)
        ContourDialog.setTabOrder(self.uPrecision, self.uLabelUnits)
        ContourDialog.setTabOrder(self.uLabelUnits, self.uButtonBox)

    def retranslateUi(self, ContourDialog):
        ContourDialog.setWindowTitle(_translate("ContourDialog", "Contour", None))
        self.groupBox_2.setTitle(_translate("ContourDialog", "Input", None))
        self.label_2.setText(_translate("ContourDialog", "Apply point thinning", None))
        self.label_11.setText(_translate("ContourDialog", "Radius", None))
        self.label_3.setText(_translate("ContourDialog", "Vector layer", None))
        self.uLayerName.setToolTip(_translate("ContourDialog", "WHere to take the input datas. Select a point shapefile in the list...", None))
        self.label_4.setText(_translate("ContourDialog", "Data field   ", None))
        self.uFieldName.setToolTip(_translate("ContourDialog", "Which attribute stores the input datas?", None))
        self.groupBox.setTitle(_translate("ContourDialog", "Contouring", None))
        self.uLinesContours.setText(_translate("ContourDialog", "contour lines", None))
        self.uFilledContours.setText(_translate("ContourDialog", "filled contours", None))
        self.uBoth.setText(_translate("ContourDialog", "both", None))
        self.uLayerContours.setText(_translate("ContourDialog", "filled layers", None))
        self.label.setText(_translate("ContourDialog", "Number", None))
        self.uLevelsNumber.setStatusTip(_translate("ContourDialog", "Number of levels between min and max value (from data field)", None))
        self.label_5.setText(_translate("ContourDialog", "Min", None))
        self.label_6.setText(_translate("ContourDialog", "Max", None))
        self.label_10.setText(_translate("ContourDialog", "Extend", None))
        self.uExtend.setItemText(0, _translate("ContourDialog", "neither", None))
        self.uExtend.setItemText(1, _translate("ContourDialog", "min", None))
        self.uExtend.setItemText(2, _translate("ContourDialog", "max", None))
        self.uExtend.setItemText(3, _translate("ContourDialog", "both", None))
        self.label_7.setText(_translate("ContourDialog", "Method", None))
        self.uMethod.setItemText(0, _translate("ContourDialog", "Equal", None))
        self.uMethod.setItemText(1, _translate("ContourDialog", "Quantile", None))
        self.uMethod.setItemText(2, _translate("ContourDialog", "Manual", None))
        self.groupBox_3.setTitle(_translate("ContourDialog", "Output", None))
        self.label_8.setText(_translate("ContourDialog", "Layer name", None))
        self.uPrecision.setStatusTip(_translate("ContourDialog", "Number of levels between min and max value (from data field)", None))
        self.label_12.setText(_translate("ContourDialog", "Label units text ", None))
        self.label_9.setText(_translate("ContourDialog", "Label precision", None))

