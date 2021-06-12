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
        waitDialog->resize(309, 126);
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
        label_2->setText(QCoreApplication::translate("waitDialog", "<html><head/><body><p align=\"center\"><img src=\":/images/ajax-loader.gif\"/></p></body></html>", nullptr));
    } // retranslateUi

};

namespace Ui {
    class waitDialog: public Ui_waitDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_WAITDIALOG_H
