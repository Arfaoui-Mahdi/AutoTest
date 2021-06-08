/********************************************************************************
** Form generated from reading UI file 'dialog.ui'
**
** Created by: Qt User Interface Compiler version 5.15.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DIALOG_H
#define UI_DIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QPlainTextEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QScrollArea>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSplitter>
#include <QtWidgets/QStackedWidget>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Dialog
{
public:
    QVBoxLayout *verticalLayout_11;
    QHBoxLayout *horizontalLayout;
    QSpacerItem *horizontalSpacer_2;
    QLabel *label;
    QSpacerItem *horizontalSpacer_3;
    QStackedWidget *stackedWidget;
    QWidget *page;
    QVBoxLayout *verticalLayout_10;
    QHBoxLayout *horizontalLayout_10;
    QVBoxLayout *verticalLayout_8;
    QHBoxLayout *horizontalLayout_3;
    QLabel *label_4;
    QSpacerItem *horizontalSpacer_10;
    QLineEdit *srcPath;
    QPushButton *btnSrcPath;
    QFrame *line_3;
    QHBoxLayout *horizontalLayout_6;
    QLabel *label_5;
    QSpacerItem *horizontalSpacer_11;
    QLineEdit *cfgPath;
    QPushButton *btnCfgPath;
    QFrame *line_2;
    QHBoxLayout *horizontalLayout_9;
    QLabel *label_6;
    QSpacerItem *horizontalSpacer_12;
    QLineEdit *incPath;
    QPushButton *btnIncPath;
    QFrame *line;
    QVBoxLayout *verticalLayout;
    QSpacerItem *verticalSpacer;
    QPushButton *pushButton;
    QSpacerItem *verticalSpacer_2;
    QWidget *page_2;
    QPlainTextEdit *plainTextEdit;
    QWidget *layoutWidget;
    QHBoxLayout *horizontalLayout_4;
    QSpacerItem *horizontalSpacer_4;
    QPushButton *btnChsTests;
    QSpacerItem *horizontalSpacer_5;
    QWidget *page_3;
    QVBoxLayout *verticalLayout_3;
    QFrame *verticalFrame;
    QVBoxLayout *verticalLayout_2;
    QListWidget *listWidget;
    QPushButton *btnExcTests;
    QWidget *page_4;
    QVBoxLayout *verticalLayout_4;
    QHBoxLayout *horizontalLayout_7;
    QSpacerItem *horizontalSpacer_6;
    QLabel *label_2;
    QSpacerItem *horizontalSpacer_7;
    QHBoxLayout *horizontalLayout_8;
    QListWidget *chsTestListWidget;
    QWidget *page_5;
    QVBoxLayout *verticalLayout_5;
    QScrollArea *scrollArea;
    QWidget *scrollAreaWidgetContents;
    QVBoxLayout *verticalLayout_16;
    QVBoxLayout *VLayoutOfTests;
    QHBoxLayout *horizontalLayout_12;
    QSpacerItem *horizontalSpacer_13;
    QPushButton *btnProceedTests;
    QSpacerItem *horizontalSpacer_14;
    QWidget *page_6;
    QVBoxLayout *verticalLayout_7;
    QScrollArea *scrollArea_2;
    QWidget *scrollAreaWidgetContents_2;
    QVBoxLayout *verticalLayout_9;
    QVBoxLayout *VLayoutConfirmTests;
    QHBoxLayout *horizontalLayout_5;
    QSpacerItem *horizontalSpacer_8;
    QPushButton *btnExecuteTests;
    QSpacerItem *horizontalSpacer_9;
    QWidget *page_7;
    QVBoxLayout *verticalLayout_12;
    QPlainTextEdit *resPlaintext;
    QWidget *page_8;
    QVBoxLayout *verticalLayout_13;
    QLabel *label_3;
    QHBoxLayout *horizontalLayout_11;
    QSplitter *splitter;
    QPushButton *btnPrcdRC;
    QPushButton *btnPrcdRDBI;
    QPushButton *btnPrcdWDBI;
    QVBoxLayout *verticalLayout_15;
    QSpacerItem *verticalSpacer_3;
    QPushButton *btnServicePrcd;
    QSpacerItem *verticalSpacer_4;
    QWidget *page_9;
    QVBoxLayout *verticalLayout_14;
    QScrollArea *resScrollArea;
    QWidget *scrollAreaWidgetContents_3;
    QHBoxLayout *horizontalLayout_2;
    QToolButton *toolButton;
    QSpacerItem *horizontalSpacer;
    QPushButton *btnPrvs;

    void setupUi(QDialog *Dialog)
    {
        if (Dialog->objectName().isEmpty())
            Dialog->setObjectName(QString::fromUtf8("Dialog"));
        Dialog->resize(615, 450);
        verticalLayout_11 = new QVBoxLayout(Dialog);
        verticalLayout_11->setObjectName(QString::fromUtf8("verticalLayout_11"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer_2);

        label = new QLabel(Dialog);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout->addWidget(label);

        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer_3);


        verticalLayout_11->addLayout(horizontalLayout);

        stackedWidget = new QStackedWidget(Dialog);
        stackedWidget->setObjectName(QString::fromUtf8("stackedWidget"));
        stackedWidget->setEnabled(true);
        page = new QWidget();
        page->setObjectName(QString::fromUtf8("page"));
        verticalLayout_10 = new QVBoxLayout(page);
        verticalLayout_10->setObjectName(QString::fromUtf8("verticalLayout_10"));
        horizontalLayout_10 = new QHBoxLayout();
        horizontalLayout_10->setObjectName(QString::fromUtf8("horizontalLayout_10"));
        verticalLayout_8 = new QVBoxLayout();
        verticalLayout_8->setObjectName(QString::fromUtf8("verticalLayout_8"));
        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        label_4 = new QLabel(page);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setEnabled(true);
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(label_4->sizePolicy().hasHeightForWidth());
        label_4->setSizePolicy(sizePolicy);

        horizontalLayout_3->addWidget(label_4);

        horizontalSpacer_10 = new QSpacerItem(41, 18, QSizePolicy::Minimum, QSizePolicy::Minimum);

        horizontalLayout_3->addItem(horizontalSpacer_10);

        srcPath = new QLineEdit(page);
        srcPath->setObjectName(QString::fromUtf8("srcPath"));

        horizontalLayout_3->addWidget(srcPath);

        btnSrcPath = new QPushButton(page);
        btnSrcPath->setObjectName(QString::fromUtf8("btnSrcPath"));

        horizontalLayout_3->addWidget(btnSrcPath);


        verticalLayout_8->addLayout(horizontalLayout_3);

        line_3 = new QFrame(page);
        line_3->setObjectName(QString::fromUtf8("line_3"));
        line_3->setFrameShape(QFrame::HLine);
        line_3->setFrameShadow(QFrame::Sunken);

        verticalLayout_8->addWidget(line_3);

        horizontalLayout_6 = new QHBoxLayout();
        horizontalLayout_6->setObjectName(QString::fromUtf8("horizontalLayout_6"));
        label_5 = new QLabel(page);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        sizePolicy.setHeightForWidth(label_5->sizePolicy().hasHeightForWidth());
        label_5->setSizePolicy(sizePolicy);

        horizontalLayout_6->addWidget(label_5);

        horizontalSpacer_11 = new QSpacerItem(57, 20, QSizePolicy::Minimum, QSizePolicy::Minimum);

        horizontalLayout_6->addItem(horizontalSpacer_11);

        cfgPath = new QLineEdit(page);
        cfgPath->setObjectName(QString::fromUtf8("cfgPath"));
        QSizePolicy sizePolicy1(QSizePolicy::Expanding, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(cfgPath->sizePolicy().hasHeightForWidth());
        cfgPath->setSizePolicy(sizePolicy1);
        cfgPath->setBaseSize(QSize(10, 2));
        cfgPath->setFocusPolicy(Qt::StrongFocus);

        horizontalLayout_6->addWidget(cfgPath);

        btnCfgPath = new QPushButton(page);
        btnCfgPath->setObjectName(QString::fromUtf8("btnCfgPath"));

        horizontalLayout_6->addWidget(btnCfgPath);


        verticalLayout_8->addLayout(horizontalLayout_6);

        line_2 = new QFrame(page);
        line_2->setObjectName(QString::fromUtf8("line_2"));
        line_2->setFrameShape(QFrame::HLine);
        line_2->setFrameShadow(QFrame::Sunken);

        verticalLayout_8->addWidget(line_2);

        horizontalLayout_9 = new QHBoxLayout();
        horizontalLayout_9->setObjectName(QString::fromUtf8("horizontalLayout_9"));
        label_6 = new QLabel(page);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        sizePolicy.setHeightForWidth(label_6->sizePolicy().hasHeightForWidth());
        label_6->setSizePolicy(sizePolicy);
        label_6->setFrameShape(QFrame::NoFrame);
        label_6->setFrameShadow(QFrame::Sunken);

        horizontalLayout_9->addWidget(label_6);

        horizontalSpacer_12 = new QSpacerItem(25, 20, QSizePolicy::Minimum, QSizePolicy::Minimum);

        horizontalLayout_9->addItem(horizontalSpacer_12);

        incPath = new QLineEdit(page);
        incPath->setObjectName(QString::fromUtf8("incPath"));

        horizontalLayout_9->addWidget(incPath);

        btnIncPath = new QPushButton(page);
        btnIncPath->setObjectName(QString::fromUtf8("btnIncPath"));

        horizontalLayout_9->addWidget(btnIncPath);


        verticalLayout_8->addLayout(horizontalLayout_9);


        horizontalLayout_10->addLayout(verticalLayout_8);

        line = new QFrame(page);
        line->setObjectName(QString::fromUtf8("line"));
        line->setFrameShape(QFrame::VLine);
        line->setFrameShadow(QFrame::Sunken);

        horizontalLayout_10->addWidget(line);

        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer);

        pushButton = new QPushButton(page);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));

        verticalLayout->addWidget(pushButton);

        verticalSpacer_2 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer_2);


        horizontalLayout_10->addLayout(verticalLayout);


        verticalLayout_10->addLayout(horizontalLayout_10);

        stackedWidget->addWidget(page);
        page_2 = new QWidget();
        page_2->setObjectName(QString::fromUtf8("page_2"));
        page_2->setEnabled(false);
        plainTextEdit = new QPlainTextEdit(page_2);
        plainTextEdit->setObjectName(QString::fromUtf8("plainTextEdit"));
        plainTextEdit->setGeometry(QRect(9, 9, 591, 301));
        layoutWidget = new QWidget(page_2);
        layoutWidget->setObjectName(QString::fromUtf8("layoutWidget"));
        layoutWidget->setGeometry(QRect(10, 320, 601, 25));
        horizontalLayout_4 = new QHBoxLayout(layoutWidget);
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        horizontalLayout_4->setContentsMargins(0, 0, 0, 0);
        horizontalSpacer_4 = new QSpacerItem(178, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_4->addItem(horizontalSpacer_4);

        btnChsTests = new QPushButton(layoutWidget);
        btnChsTests->setObjectName(QString::fromUtf8("btnChsTests"));

        horizontalLayout_4->addWidget(btnChsTests);

        horizontalSpacer_5 = new QSpacerItem(188, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_4->addItem(horizontalSpacer_5);

        stackedWidget->addWidget(page_2);
        page_3 = new QWidget();
        page_3->setObjectName(QString::fromUtf8("page_3"));
        page_3->setEnabled(false);
        verticalLayout_3 = new QVBoxLayout(page_3);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        verticalFrame = new QFrame(page_3);
        verticalFrame->setObjectName(QString::fromUtf8("verticalFrame"));
        verticalLayout_2 = new QVBoxLayout(verticalFrame);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        listWidget = new QListWidget(verticalFrame);
        listWidget->setObjectName(QString::fromUtf8("listWidget"));
        listWidget->setSelectionMode(QAbstractItemView::MultiSelection);

        verticalLayout_2->addWidget(listWidget);


        verticalLayout_3->addWidget(verticalFrame);

        btnExcTests = new QPushButton(page_3);
        btnExcTests->setObjectName(QString::fromUtf8("btnExcTests"));

        verticalLayout_3->addWidget(btnExcTests);

        stackedWidget->addWidget(page_3);
        page_4 = new QWidget();
        page_4->setObjectName(QString::fromUtf8("page_4"));
        page_4->setEnabled(false);
        verticalLayout_4 = new QVBoxLayout(page_4);
        verticalLayout_4->setObjectName(QString::fromUtf8("verticalLayout_4"));
        horizontalLayout_7 = new QHBoxLayout();
        horizontalLayout_7->setObjectName(QString::fromUtf8("horizontalLayout_7"));
        horizontalSpacer_6 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_7->addItem(horizontalSpacer_6);

        label_2 = new QLabel(page_4);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        horizontalLayout_7->addWidget(label_2);

        horizontalSpacer_7 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_7->addItem(horizontalSpacer_7);


        verticalLayout_4->addLayout(horizontalLayout_7);

        horizontalLayout_8 = new QHBoxLayout();
        horizontalLayout_8->setObjectName(QString::fromUtf8("horizontalLayout_8"));
        chsTestListWidget = new QListWidget(page_4);
        chsTestListWidget->setObjectName(QString::fromUtf8("chsTestListWidget"));
        chsTestListWidget->setSelectionMode(QAbstractItemView::SingleSelection);

        horizontalLayout_8->addWidget(chsTestListWidget);


        verticalLayout_4->addLayout(horizontalLayout_8);

        stackedWidget->addWidget(page_4);
        page_5 = new QWidget();
        page_5->setObjectName(QString::fromUtf8("page_5"));
        verticalLayout_5 = new QVBoxLayout(page_5);
        verticalLayout_5->setObjectName(QString::fromUtf8("verticalLayout_5"));
        scrollArea = new QScrollArea(page_5);
        scrollArea->setObjectName(QString::fromUtf8("scrollArea"));
        scrollArea->setWidgetResizable(true);
        scrollAreaWidgetContents = new QWidget();
        scrollAreaWidgetContents->setObjectName(QString::fromUtf8("scrollAreaWidgetContents"));
        scrollAreaWidgetContents->setGeometry(QRect(0, 0, 577, 303));
        verticalLayout_16 = new QVBoxLayout(scrollAreaWidgetContents);
        verticalLayout_16->setObjectName(QString::fromUtf8("verticalLayout_16"));
        VLayoutOfTests = new QVBoxLayout();
        VLayoutOfTests->setObjectName(QString::fromUtf8("VLayoutOfTests"));

        verticalLayout_16->addLayout(VLayoutOfTests);

        scrollArea->setWidget(scrollAreaWidgetContents);

        verticalLayout_5->addWidget(scrollArea);

        horizontalLayout_12 = new QHBoxLayout();
        horizontalLayout_12->setObjectName(QString::fromUtf8("horizontalLayout_12"));
        horizontalSpacer_13 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_12->addItem(horizontalSpacer_13);

        btnProceedTests = new QPushButton(page_5);
        btnProceedTests->setObjectName(QString::fromUtf8("btnProceedTests"));

        horizontalLayout_12->addWidget(btnProceedTests);

        horizontalSpacer_14 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_12->addItem(horizontalSpacer_14);


        verticalLayout_5->addLayout(horizontalLayout_12);

        stackedWidget->addWidget(page_5);
        page_6 = new QWidget();
        page_6->setObjectName(QString::fromUtf8("page_6"));
        verticalLayout_7 = new QVBoxLayout(page_6);
        verticalLayout_7->setObjectName(QString::fromUtf8("verticalLayout_7"));
        scrollArea_2 = new QScrollArea(page_6);
        scrollArea_2->setObjectName(QString::fromUtf8("scrollArea_2"));
        scrollArea_2->setWidgetResizable(true);
        scrollAreaWidgetContents_2 = new QWidget();
        scrollAreaWidgetContents_2->setObjectName(QString::fromUtf8("scrollAreaWidgetContents_2"));
        scrollAreaWidgetContents_2->setGeometry(QRect(0, 0, 577, 303));
        verticalLayout_9 = new QVBoxLayout(scrollAreaWidgetContents_2);
        verticalLayout_9->setObjectName(QString::fromUtf8("verticalLayout_9"));
        VLayoutConfirmTests = new QVBoxLayout();
        VLayoutConfirmTests->setObjectName(QString::fromUtf8("VLayoutConfirmTests"));

        verticalLayout_9->addLayout(VLayoutConfirmTests);

        scrollArea_2->setWidget(scrollAreaWidgetContents_2);

        verticalLayout_7->addWidget(scrollArea_2);

        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        horizontalSpacer_8 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_5->addItem(horizontalSpacer_8);

        btnExecuteTests = new QPushButton(page_6);
        btnExecuteTests->setObjectName(QString::fromUtf8("btnExecuteTests"));

        horizontalLayout_5->addWidget(btnExecuteTests);

        horizontalSpacer_9 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_5->addItem(horizontalSpacer_9);


        verticalLayout_7->addLayout(horizontalLayout_5);

        stackedWidget->addWidget(page_6);
        page_7 = new QWidget();
        page_7->setObjectName(QString::fromUtf8("page_7"));
        verticalLayout_12 = new QVBoxLayout(page_7);
        verticalLayout_12->setObjectName(QString::fromUtf8("verticalLayout_12"));
        resPlaintext = new QPlainTextEdit(page_7);
        resPlaintext->setObjectName(QString::fromUtf8("resPlaintext"));

        verticalLayout_12->addWidget(resPlaintext);

        stackedWidget->addWidget(page_7);
        page_8 = new QWidget();
        page_8->setObjectName(QString::fromUtf8("page_8"));
        verticalLayout_13 = new QVBoxLayout(page_8);
        verticalLayout_13->setObjectName(QString::fromUtf8("verticalLayout_13"));
        label_3 = new QLabel(page_8);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        verticalLayout_13->addWidget(label_3);

        horizontalLayout_11 = new QHBoxLayout();
        horizontalLayout_11->setObjectName(QString::fromUtf8("horizontalLayout_11"));
        splitter = new QSplitter(page_8);
        splitter->setObjectName(QString::fromUtf8("splitter"));
        splitter->setOrientation(Qt::Vertical);
        btnPrcdRC = new QPushButton(splitter);
        btnPrcdRC->setObjectName(QString::fromUtf8("btnPrcdRC"));
        splitter->addWidget(btnPrcdRC);
        btnPrcdRDBI = new QPushButton(splitter);
        btnPrcdRDBI->setObjectName(QString::fromUtf8("btnPrcdRDBI"));
        splitter->addWidget(btnPrcdRDBI);
        btnPrcdWDBI = new QPushButton(splitter);
        btnPrcdWDBI->setObjectName(QString::fromUtf8("btnPrcdWDBI"));
        splitter->addWidget(btnPrcdWDBI);

        horizontalLayout_11->addWidget(splitter);

        verticalLayout_15 = new QVBoxLayout();
        verticalLayout_15->setObjectName(QString::fromUtf8("verticalLayout_15"));
        verticalSpacer_3 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_15->addItem(verticalSpacer_3);

        btnServicePrcd = new QPushButton(page_8);
        btnServicePrcd->setObjectName(QString::fromUtf8("btnServicePrcd"));

        verticalLayout_15->addWidget(btnServicePrcd);

        verticalSpacer_4 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_15->addItem(verticalSpacer_4);


        horizontalLayout_11->addLayout(verticalLayout_15);


        verticalLayout_13->addLayout(horizontalLayout_11);

        stackedWidget->addWidget(page_8);
        page_9 = new QWidget();
        page_9->setObjectName(QString::fromUtf8("page_9"));
        verticalLayout_14 = new QVBoxLayout(page_9);
        verticalLayout_14->setObjectName(QString::fromUtf8("verticalLayout_14"));
        resScrollArea = new QScrollArea(page_9);
        resScrollArea->setObjectName(QString::fromUtf8("resScrollArea"));
        resScrollArea->setWidgetResizable(true);
        scrollAreaWidgetContents_3 = new QWidget();
        scrollAreaWidgetContents_3->setObjectName(QString::fromUtf8("scrollAreaWidgetContents_3"));
        scrollAreaWidgetContents_3->setGeometry(QRect(0, 0, 98, 28));
        resScrollArea->setWidget(scrollAreaWidgetContents_3);

        verticalLayout_14->addWidget(resScrollArea);

        stackedWidget->addWidget(page_9);

        verticalLayout_11->addWidget(stackedWidget);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        toolButton = new QToolButton(Dialog);
        toolButton->setObjectName(QString::fromUtf8("toolButton"));

        horizontalLayout_2->addWidget(toolButton);

        horizontalSpacer = new QSpacerItem(258, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer);

        btnPrvs = new QPushButton(Dialog);
        btnPrvs->setObjectName(QString::fromUtf8("btnPrvs"));

        horizontalLayout_2->addWidget(btnPrvs);


        verticalLayout_11->addLayout(horizontalLayout_2);


        retranslateUi(Dialog);

        stackedWidget->setCurrentIndex(5);


        QMetaObject::connectSlotsByName(Dialog);
    } // setupUi

    void retranslateUi(QDialog *Dialog)
    {
        Dialog->setWindowTitle(QCoreApplication::translate("Dialog", "Dialog", nullptr));
        label->setText(QCoreApplication::translate("Dialog", "<html><head/><body><p><img src=\":/images/actiaLogoPng.png\"/></p></body></html>", nullptr));
        label_4->setText(QCoreApplication::translate("Dialog", "Choose Source File Path", nullptr));
        btnSrcPath->setText(QCoreApplication::translate("Dialog", "Choose", nullptr));
        label_5->setText(QCoreApplication::translate("Dialog", "Choose Cfg File Path", nullptr));
        btnCfgPath->setText(QCoreApplication::translate("Dialog", "Choose", nullptr));
        label_6->setText(QCoreApplication::translate("Dialog", "Choose Include Folder Path", nullptr));
        btnIncPath->setText(QCoreApplication::translate("Dialog", "Choose", nullptr));
        pushButton->setText(QCoreApplication::translate("Dialog", "Start Processing", nullptr));
        btnChsTests->setText(QCoreApplication::translate("Dialog", "View Tests List", nullptr));
        btnExcTests->setText(QCoreApplication::translate("Dialog", "Choose Tests", nullptr));
        label_2->setText(QCoreApplication::translate("Dialog", "Click twice on the test to configure it ", nullptr));
        btnProceedTests->setText(QCoreApplication::translate("Dialog", "Proceed", nullptr));
        btnExecuteTests->setText(QCoreApplication::translate("Dialog", "Execute", nullptr));
        label_3->setText(QCoreApplication::translate("Dialog", "Check services you want to test then click on \"Proceed\"", nullptr));
        btnPrcdRC->setText(QCoreApplication::translate("Dialog", "Proceed Routine Control Testing", nullptr));
        btnPrcdRDBI->setText(QCoreApplication::translate("Dialog", "Proceed RDBI Testing", nullptr));
        btnPrcdWDBI->setText(QCoreApplication::translate("Dialog", "Proceed WDBI Testting", nullptr));
        btnServicePrcd->setText(QCoreApplication::translate("Dialog", "Proceed", nullptr));
        toolButton->setText(QCoreApplication::translate("Dialog", "EXIT", nullptr));
        btnPrvs->setText(QCoreApplication::translate("Dialog", "Previous", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Dialog: public Ui_Dialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_DIALOG_H
