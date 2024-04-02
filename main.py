from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QShortcut
from PyQt5.QtGui import QPixmap
import sys
from PyQt5 import QtWidgets
from ui import Ui_MainWindow
from PyQt5.QtCore import QThreadPool, pyqtSignal, Qt
from TranslateManga import Translate
from PIL import ImageQt
import img2pdf
from Image import Image
from FileHandling import FileHandler
from Configure import Settings
from settingsGUI import Ui_Form
from manga_ocr import MangaOcr
from PyQt5.QtGui import QPixmap, QTextOption, QFont, QPen
from loguru import logger
from loguru import logger
from pprint import pprint

class interact(QtWidgets.QMainWindow, Ui_MainWindow):
    active = pyqtSignal()
    def __init__(self):
        super(interact, self).__init__()
        self.setupUi(self)
        self.resize(970, 940)
        self.appMod()
        self.stylesheet1()
        self.buttonConnections()
        self.setting = Settings()
        self.handling = FileHandler()
        self.thread = QThreadPool()
        self.index = 0
        self.newIndex = 0
        self.translatedFiles = []
        self.files = []
        self.isClicked = False
        self.shownSetting = False
        self.progressBar.setValue(0)
        self.progressBar.setFormat("Translating....")
        self.progressBar.setGeometry(self.width()//2-65, self.height()//2, 200, 30)
        self.progressBar.setVisible(False)
        self.progressBar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.translator = "DeepL"
        self.translateOptions.setCurrentIndex(2)
        self.range = 0
        self.combineN = False
        self.rangeSlider.setEnabled(False)
        self.combineO = True
        self.changeTranslation = []
        self.checkthing = []
        self.ocr = MangaOcr()
        self.orgLanguage = None
        self.clearButton.hide()
        self.saveButton.hide()
        self.clearButton.clicked.connect(self.clear)
        self.im.adjustSize()
        self.shownWidget = False
        self.recycle = {}
        self.num = -1
        self.isSort = False
        self.AutoWidget.hide()
        self.settings_widget.hide()
        self.advanceSettings1()
        self.side_menu.hide()
        self.ISPCode = {
            "Japanese": "ja",
            "Korean": "ko",
            "Chinese": "zh"
        }
        self.originalLang =  "ja"
    def appMod(self):
        self.setWindowTitle("MangaTranslator")
        self.setWindowIcon(QtGui.QIcon(":/Icons/translation.png"))
        self.comboBox_3.addItem("None")
        self.comboBox_3.removeItem(3)
        self.translateOptions.removeItem(0)
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.setAttribute(Qt.WA_DeleteOnClose)
        self.Form.setMinimumSize(QtCore.QSize(720, 415))
        self.im = Image(self.imageWidget)
        self.im.setScaledContents(True)
        self.on1 = False
        self.on2 = False
        QShortcut(QtCore.Qt.Key_Right, self, self.moveRight)
        QShortcut(QtCore.Qt.Key_Left, self, self.moveLeft)
    def widgetSizes(self):
        self.imageWidget.setMaximumSize(QtCore.QSize(900,800))
        self.translate.setMinimumSize(QtCore.QSize(130, 40))
        self.upload.setMinimumSize(QtCore.QSize(130, 40))
        self.saveButton.setMinimumSize(QtCore.QSize(130, 40))
        self.ui.saveSet.setMinimumSize(QtCore.QSize(100, 30))
        self.header.setMinimumSize(QtCore.QSize(0, 100))
        self.header.setMaximumSize(QtCore.QSize(16777215, 100))
        self.Settings_button.setIconSize(QtCore.QSize(60, 60))
        self.menuButton.setIconSize(QtCore.QSize(50, 50))
        self.side_menu.setMinimumWidth(255)
    def buttonConnections(self):
        self.upload.clicked.connect(self.upload1)
        self.rightArrow.clicked.connect(self.moveRight)
        self.leftArrow.clicked.connect(self.moveLeft)
        self.translate.clicked.connect(self.translate1)
        self.translate.clicked.connect(self.showProgress)
        self.Settings_button.clicked.connect(self.showSet)
        self.Advance_setting_button.clicked.connect(self.advanceSettings)
        self.ui.saveSet.clicked.connect(self.getInfo)
        self.translateOptions.currentTextChanged.connect(self.choosenTranslator)
        self.rangeSlider.valueChanged.connect(self.chooseRange)
        self.combN_box.stateChanged.connect(self.showCombN)
        self.combO_box.stateChanged.connect(self.showCombO)
        self.saveButton.clicked.connect(self.saveImages)
        self.horizontalLayout_5.addWidget(self.im)
        self.Automatic_button.clicked.connect(self.changeToAutomatic)
        self.sort_box.stateChanged.connect(self.sortFile)
        self.menuButton.clicked.connect(self.showMenu)
        self.comboBox_3.currentTextChanged.connect(self.langOption) # Language option
    def stylesheet1(self):
        self.progressBar.setStyleSheet(
                          """ QProgressBar {
                                border: 2px solid #3F51B5;
                                border-radius: 5px;
                                text-align: center;
                                font-weight: bold;
                            }

                            QProgressBar::chunk {
                                background-color: #3F51B5;
                                width: 10px;
                                margin: 0.5px;
                                border-radius:1px;
                            }""")
        font = QFont()
        font.setFamily("Comic Sans MS")
        self.progressBar.setFont(font)
    def changeToAutomatic(self):
        self.im.flag = False
        self.AutoWidget.show()
        self.settings_widget.hide()
        if self.on1:
            self.AutoWidget.hide()
            self.on1= False
        else:
            self.on1 = True
            self.on2 = False
        self.Automatic_button.setStyleSheet("QPushButton{\n"
                                            "background-color: QLinearGradient( x1: 0, y1: 0,\n"
                                        "                             x2: 1, y2: 0, \n"
                                        "                          stop: 0 #c471f5, \n"
                                        "                          stop: 1 #fa71cd );\n"
                                            "}\n"
                                            "QPushButton:hover:!pressed\n"
                                            "{\n"
                                            "background-color: QLinearGradient( x1: 0, y1: 0,\n"
                                            "                             x2: 1, y2: 0, \n"
                                            "                          stop: 0 #c471f5, \n"
                                            "                          stop: 1 #fa71cd );\n"
                                            "}")

        if self.files != []:
            self.showImage()
    
    def showSet(self):
        self.settings_widget.show()
        self.AutoWidget.hide()
        if self.on2:
            self.settings_widget.hide()
            self.on2 = False
        else:
            self.on2 = True
            self.on1 = False
    def advanceSettings(self):
        self.ui.lineEdit.setText(str(self.setting.Translated)) # Translated folder
        self.ui.cropline.setText(str(self.setting.cropText)) # Cropped text folder
        self.Form.show()

    def advanceSettings1(self):
        self.ui.lineEdit.setText(str(self.setting.Translated)) # Translated folder
        self.ui.cropline.setText(str(self.setting.cropText)) # Cropped text folder
    def getInfo(self):
        save = self.ui.lineEdit.text()
        crop = self.ui.cropline.text()
        if save != self.setting.Translated:
            self.setting.updateSetting("Paths", "Translated", save)
            self.ui.lineEdit.setText(save)
        if crop != self.setting.cropText:
            self.setting.updateSetting("Paths", "cropText", crop)
            self.ui.cropline.setText(crop)
    def sortFile(self, n):
        if n and self.files != []:
            self.fileSorting()
            self.showImage()
        self.isSort = True
    
    def fileSorting(self):
        nd = {}
        conn = {}
        sortedFiles = []
        temp = []
        for file in self.files:
            sp = file.split("/")
            nd[sp[-1].split(".")[0]] = file
        # pprint(nd)
        for n in nd.keys():
            if n.isdigit():
                temp.append(int(n))
                conn[int(n)] = n
            else:
                conn[n] = n
                temp.append(n)
        temp.sort()
        for x in temp:
            sortedFiles.append(nd[conn[x]])
        self.files = sortedFiles
    def changeTrans(self, n):
        if n != None or n != []:
            self.changeTranslation = n
    
    def changeCheckThing(self, n):
        if n != None or n != []:
            self.checkthing = n
    def showMenu(self):
        self.side_menu.show()
        if self.shownSetting:
            self.side_menu.hide()
            self.shownSetting= False
        else:
            self.shownSetting = True
    def choosenTranslator(self, i):
        self.translator = i
        
    def orgLang(self, i):
        self.orgLanguage = i

    def langOption(self, i):
        self.originalLang = self.ISPCode[i]

    def chooseRange(self, i):
        self.range = i
        self.range_label.setText(f"Range: {self.range}px")

    def showCombN (self, i):
        if i == 0:
            self.combineN = False
            self.rangeSlider.setEnabled(False)
        else:
            self.combineN = True
            self.rangeSlider.setEnabled(True)

    def showCombO (self, i):
        if i == 0:
            self.combineO = False
        else:
            self.combineO = True
    def clear(self):
        self.im.pages.clear()
        self.im.connectDict.clear()
        self.im.translated.clear()
        self.im.japanese.clear()
        self.files.clear()
        self.recycle.clear()
        self.num = -1
        self.index = 0
        self.im.img = None
        self.im.setPixmap(QPixmap(":/Icons/whiteBG.jpg"))

    def upload1(self):
        filenames, _ =  QFileDialog.getOpenFileNames(
            None,
            "QFileDialog.getOpenFileNames()",
            "",
            "Image files (*.jpg *.png)"
        )
        if filenames != []:
            if self.files != [] and self.isClicked:
                self.files.clear()
                self.index = 0
                self.isClicked = False
                self.im.pages.clear()
                self.im.japanese.clear()
                self.im.translated.clear()
                self.im.connectDict.clear()
                self.recycle.clear()
                self.num = -1
                self.handling.deleteFiles(self.setting.Translated)
            for file in filenames:
                self.files.append(file)
            if self.files != []:
                self.im.img = self.files[0]
                if self.isSort:
                    self.fileSorting()
                self.showImage()
            if self.isClicked == False:
                self.translatedFiles.clear()
                self.saveButton.hide()
                self.changeTranslation.clear()
                self.newIndex = 0
        
    def saveImages(self):
        if self.translatedFiles == [] and not self.im.flag:
            pass
        elif self.translatedFiles != [] and not self.im.flag:
            filename = QFileDialog.getSaveFileName(self, 'Save File')
            imgDirectory = []
            num = 0
            for img in self.translatedFiles:
                image = ImageQt.fromqimage(img)
                imgName = f"Translated\img{num}.jpg"
                imgDirectory.append(imgName)
                image.save(imgName)
                num += 1
            with open((filename[0]+".pdf"), "wb") as f:
                f.write(img2pdf.convert(imgDirectory))
        else:
            filename = QFileDialog.getSaveFileName(self, 'Save File')
            imgDirectory = []
            pageCopy = self.im.scaledDict
            nums = 0
            for img in pageCopy:
                try:
                    num = 0
                    pix = QPixmap(img)
                    qp = QtGui.QPainter(pix)
                    qp.setPen(QPen(self.im.color[self.im.textColor], 2, Qt.SolidLine))
                    qp.drawPixmap(pix.rect(), pix)
                    if self.im.rect:
                        qp.drawRects(self.im.scaledDict[img])
                    for index, words in enumerate(self.im.translated[self.im.connectDict[img]]):
                        if self.im.bg != "None":
                            qp.fillRect(self.im.scaledDict[img][index], self.im.color[self.im.bg])
                        qp.setFont(QFont("Comic Sans MS",self.im.fontNum * 2))
                        option = QTextOption()
                        option.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                        qp.drawText(self.im.scaledDict[img][index], words, option)
                    imName = f"Translated\Truetrans{nums}.jpg"
                    imgDirectory.append(imName)
                    pix.save(imName)
                    nums += 1
                    qp.end()
                except:
                    logger.exception("Something went wrong!")
            with open((filename[0]+".pdf"), "wb") as f:
                f.write(img2pdf.convert(imgDirectory))
    
    def moveRight(self):
        if self.isClicked and not self.im.flag:
            if self.newIndex >= len(self.translatedFiles)-1:
                self.newIndex = len(self.translatedFiles)-1
            else:
                self.newIndex += 1
        else:
            if self.index >= len(self.files)-1:
                self.index = len(self.files)-1
            else:
                self.index += 1
        if self.files != []:
            self.showImage()
            self.drawOnPages()
        
    def moveLeft(self):
        if self.isClicked and not self.im.flag:
            if self.newIndex <= 0:
                self.newIndex = 0
            else:
                self.newIndex -= 1
        else:
            if self.index <= 0:
                self.index = 0
            else:
                self.index -= 1
        if self.files != []:
            self.showImage()
            self.drawOnPages()
    
    def drawOnPages(self):
        if self.im.flag and self.files != []:
            for img in self.files:
                if img not in self.im.pages:
                    self.im.pages[img] = []
            currentP = self.files[self.index]
            self.im.img = currentP
    
    @logger.catch
    def showImage(self):
        if self.isClicked and not self.im.flag and self.translatedFiles != []:
            self.saveButton.show()
            im = self.translatedFiles[self.newIndex]
            pix = QPixmap(im)
            self.im.setPixmap(pix)
        elif self.isClicked and self.im.flag:
            self.drawOnPages()
            im = self.files[self.index]
            pix = QPixmap(im)
            self.im.image = pix
            self.saveButton.show()
        else:
            pix = QPixmap(self.files[self.index])
            self.im.image = pix
            size = pix.size()
            self.clearButton.show()
            if size.width() > size.height():
                self.imageWidget.setMaximumSize(QtCore.QSize(990,680))
            else:
                self.imageWidget.setMaximumSize(QtCore.QSize(700,800))
            if not self.im.flag:
                self.im.setPixmap(self.im.image)
            self.drawOnPages()

    def afterThread(self, translated):
        if translated != None or translated != []:
            self.isClicked = True
            self.translatedFiles = translated
            self.index = 0
            self.newIndex = 0
            QtCore.QTimer.singleShot(0, self.showImage)
            print("THREAD COMPLETE!")

    def changeProgress(self, status):
        self.progressBar.setValue(status)

    def showProgress(self):
        if self.files != []:
            self.progressBar.setVisible(True)
            self.translate.setEnabled(False)

    def hideProgress(self):
        self.progressBar.setVisible(False)
        self.progressBar.setValue(0)
        self.translate.setEnabled(True)

    def translate1(self):
        self.clearButton.hide()
        if self.files == []:
            pass
        else:
            logger.info("Manga Translation")
            self.worker = Translate(self.files, self.ocr, self.translator, self.originalLang, self.combineN, self.combineO, self.range)
            self.worker.signals.result.connect(self.afterThread)
            self.worker.signals.stored.connect(self.changeTrans)
            self.worker.signals.booleans.connect(self.changeCheckThing)
            self.worker.signals.finished.connect(self.hideProgress)
            self.worker.signals.progress.connect(self.changeProgress)
            self.worker.signals.lang.connect(self.orgLang)
            self.thread.start(self.worker)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = interact()
    w.show()
    sys.exit(app.exec())