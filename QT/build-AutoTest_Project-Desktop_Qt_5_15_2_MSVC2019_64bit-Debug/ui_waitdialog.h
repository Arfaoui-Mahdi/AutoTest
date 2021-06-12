/********************************************************************************
** Form generated from reading UI file 'waitdialog.ui'
**
** Created by: Qt User Interface Compiler version 5.15.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_WAITDIALOG_H
#define UI_WAITDIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>

QT_BEGIN_NAMESPACE

class Ui_waitDialog
{
public:
    QHBoxLayout *horizontalLayout;
    QLabel *label;
    QLabel *label_2;

    void setupUi(QDialog *waitDialog)
    {
        if (waitDialog->objectName().isEmpty())
            waitDialog->setObjectName(QString::fromUtf8("waitDialog"));
        waitDialog->resize(275, 119);
        horizontalLayout = new QHBoxLayout(waitDialog);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        label = new QLabel(waitDialog);
        label->setObjectName(QString::fromUtf8("label"));
        QFont font;
        font.setFamily(QString::fromUtf8("Rockwell"));
        font.setPointSize(14);
        label->setFont(font);

        horizontalLayout->addWidget(label);

        label_2 = new QLabel(waitDialog);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        horizontalLayout->addWidget(label_2);


        retranslateUi(waitDialog);

        QMetaObject::connectSlotsByName(waitDialog);
    } // setupUi

    void retranslateUi(QDialog *waitDialog)
    {
        waitDialog->setWindowTitle(QCoreApplication::translate("waitDialog", "Dialog", nullptr));
        label->setText(QCoreApplication::translate("waitDialog", "Please wait! Testing...", nullptr));
        label_2->setText(QCoreApplication::translate("waitDialog", "<html>\n"
"<head>\n"
"<style type=\"text/css\" media=\"screen\">\n"
".lds-roller {\n"
"  display: inline-block;\n"
"  position: relative;\n"
"  width: 80px;\n"
"  height: 80px;\n"
"}\n"
".lds-roller div {\n"
"  animation: lds-roller 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;\n"
"  transform-origin: 40px 40px;\n"
"}\n"
".lds-roller div:after {\n"
"  content: \" \";\n"
"  display: block;\n"
"  position: absolute;\n"
"  width: 7px;\n"
"  height: 7px;\n"
"  border-radius: 50%;\n"
"  background: #fff;\n"
"  margin: -4px 0 0 -4px;\n"
"}\n"
".lds-roller div:nth-child(1) {\n"
"  animation-delay: -0.036s;\n"
"}\n"
".lds-roller div:nth-child(1):after {\n"
"  top: 63px;\n"
"  left: 63px;\n"
"}\n"
".lds-roller div:nth-child(2) {\n"
"  animation-delay: -0.072s;\n"
"}\n"
".lds-roller div:nth-child(2):after {\n"
"  top: 68px;\n"
"  left: 56px;\n"
"}\n"
".lds-roller div:nth-child(3) {\n"
"  animation-delay: -0.108s;\n"
"}\n"
".lds-roller div:nth-child(3):after {\n"
"  top: 71px;\n"
"  left: 48px;\n"
"}\n"
".lds-roller div:nt"
                        "h-child(4) {\n"
"  animation-delay: -0.144s;\n"
"}\n"
".lds-roller div:nth-child(4):after {\n"
"  top: 72px;\n"
"  left: 40px;\n"
"}\n"
".lds-roller div:nth-child(5) {\n"
"  animation-delay: -0.18s;\n"
"}\n"
".lds-roller div:nth-child(5):after {\n"
"  top: 71px;\n"
"  left: 32px;\n"
"}\n"
".lds-roller div:nth-child(6) {\n"
"  animation-delay: -0.216s;\n"
"}\n"
".lds-roller div:nth-child(6):after {\n"
"  top: 68px;\n"
"  left: 24px;\n"
"}\n"
".lds-roller div:nth-child(7) {\n"
"  animation-delay: -0.252s;\n"
"}\n"
".lds-roller div:nth-child(7):after {\n"
"  top: 63px;\n"
"  left: 17px;\n"
"}\n"
".lds-roller div:nth-child(8) {\n"
"  animation-delay: -0.288s;\n"
"}\n"
".lds-roller div:nth-child(8):after {\n"
"  top: 56px;\n"
"  left: 12px;\n"
"}\n"
"@keyframes lds-roller {\n"
"  0% {\n"
"    transform: rotate(0deg);\n"
"  }\n"
"  100% {\n"
"    transform: rotate(360deg);\n"
"  }\n"
"}\n"
"\n"
"</style>\n"
"<head/>\n"
"<body>\n"
"      <div align=\"center\"><div class=\"lds-roller\"><div></div><div></div><div></div"
                        "><div></div><div></div><div></div><div></div><div></div></div></div>\n"
"</body>\n"
"</html>", nullptr));
    } // retranslateUi

};

namespace Ui {
    class waitDialog: public Ui_waitDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_WAITDIALOG_H
