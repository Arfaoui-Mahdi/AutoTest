/********************************************************************************
** Form generated from reading UI file 'maketest.ui'
**
** Created by: Qt User Interface Compiler version 5.15.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAKETEST_H
#define UI_MAKETEST_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSplitter>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MakeTest
{
public:
    QVBoxLayout *verticalLayout;
    QSplitter *splitter;
    QFrame *frame;
    QVBoxLayout *verticalLayout_3;
    QSplitter *splitter_3;
    QWidget *widget;
    QFormLayout *formLayout;
    QLabel *label;
    QLineEdit *lineEditTName;
    QLabel *label_2;
    QLineEdit *lineEditTId;
    QSplitter *splitter_2;
    QLabel *label_3;
    QWidget *verticalLayoutWidget;
    QVBoxLayout *verticalLayout_2;
    QWidget *widget1;
    QHBoxLayout *horizontalLayout;
    QSpacerItem *horizontalSpacer;
    QPushButton *btnCancel;
    QPushButton *btnPrcd;

    void setupUi(QDialog *MakeTest)
    {
        if (MakeTest->objectName().isEmpty())
            MakeTest->setObjectName(QString::fromUtf8("MakeTest"));
        MakeTest->resize(502, 325);
        verticalLayout = new QVBoxLayout(MakeTest);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        splitter = new QSplitter(MakeTest);
        splitter->setObjectName(QString::fromUtf8("splitter"));
        splitter->setOrientation(Qt::Vertical);
        frame = new QFrame(splitter);
        frame->setObjectName(QString::fromUtf8("frame"));
        frame->setFrameShape(QFrame::Box);
        frame->setFrameShadow(QFrame::Raised);
        verticalLayout_3 = new QVBoxLayout(frame);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        splitter_3 = new QSplitter(frame);
        splitter_3->setObjectName(QString::fromUtf8("splitter_3"));
        splitter_3->setOrientation(Qt::Vertical);
        widget = new QWidget(splitter_3);
        widget->setObjectName(QString::fromUtf8("widget"));
        formLayout = new QFormLayout(widget);
        formLayout->setObjectName(QString::fromUtf8("formLayout"));
        formLayout->setContentsMargins(0, 0, 0, 0);
        label = new QLabel(widget);
        label->setObjectName(QString::fromUtf8("label"));

        formLayout->setWidget(0, QFormLayout::LabelRole, label);

        lineEditTName = new QLineEdit(widget);
        lineEditTName->setObjectName(QString::fromUtf8("lineEditTName"));
        lineEditTName->setReadOnly(true);

        formLayout->setWidget(0, QFormLayout::FieldRole, lineEditTName);

        label_2 = new QLabel(widget);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        formLayout->setWidget(1, QFormLayout::LabelRole, label_2);

        lineEditTId = new QLineEdit(widget);
        lineEditTId->setObjectName(QString::fromUtf8("lineEditTId"));
        lineEditTId->setReadOnly(true);

        formLayout->setWidget(1, QFormLayout::FieldRole, lineEditTId);

        splitter_3->addWidget(widget);
        splitter_2 = new QSplitter(splitter_3);
        splitter_2->setObjectName(QString::fromUtf8("splitter_2"));
        splitter_2->setOrientation(Qt::Horizontal);
        label_3 = new QLabel(splitter_2);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        splitter_2->addWidget(label_3);
        verticalLayoutWidget = new QWidget(splitter_2);
        verticalLayoutWidget->setObjectName(QString::fromUtf8("verticalLayoutWidget"));
        verticalLayout_2 = new QVBoxLayout(verticalLayoutWidget);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        verticalLayout_2->setContentsMargins(0, 0, 0, 0);
        splitter_2->addWidget(verticalLayoutWidget);
        splitter_3->addWidget(splitter_2);

        verticalLayout_3->addWidget(splitter_3);

        splitter->addWidget(frame);
        widget1 = new QWidget(splitter);
        widget1->setObjectName(QString::fromUtf8("widget1"));
        horizontalLayout = new QHBoxLayout(widget1);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        horizontalLayout->setContentsMargins(0, 0, 0, 0);
        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer);

        btnCancel = new QPushButton(widget1);
        btnCancel->setObjectName(QString::fromUtf8("btnCancel"));

        horizontalLayout->addWidget(btnCancel);

        btnPrcd = new QPushButton(widget1);
        btnPrcd->setObjectName(QString::fromUtf8("btnPrcd"));

        horizontalLayout->addWidget(btnPrcd);

        splitter->addWidget(widget1);

        verticalLayout->addWidget(splitter);


        retranslateUi(MakeTest);

        QMetaObject::connectSlotsByName(MakeTest);
    } // setupUi

    void retranslateUi(QDialog *MakeTest)
    {
        MakeTest->setWindowTitle(QCoreApplication::translate("MakeTest", "Dialog", nullptr));
        label->setText(QCoreApplication::translate("MakeTest", "Test Name : ", nullptr));
        lineEditTName->setInputMask(QString());
        lineEditTName->setText(QString());
        lineEditTName->setPlaceholderText(QString());
        label_2->setText(QCoreApplication::translate("MakeTest", "Test ID :", nullptr));
        label_3->setText(QCoreApplication::translate("MakeTest", "Args :", nullptr));
        btnCancel->setText(QCoreApplication::translate("MakeTest", "Cancel", nullptr));
        btnPrcd->setText(QCoreApplication::translate("MakeTest", "Proceed", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MakeTest: public Ui_MakeTest {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAKETEST_H
