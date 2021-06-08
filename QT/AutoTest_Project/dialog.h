#ifndef DIALOG_H
#define DIALOG_H

#include <QDialog>
#include <maketest.h>


#include <loading.h>
#include <QProcess>
#include <QString>
#include <QResource>
#include <QMessageBox>
#include <QDebug>
#include <QDir>
#include <QFile>
#include <QTextStream>
#include <QPushButton>
#include <QPlainTextEdit>
#include <QFileDialog>
#include <QJsonArray>
#include <QJsonDocument>
#include <QJsonObject>
#include <QJsonValue>
#include <QVariant>
#include <QList>
#include <QGroupBox>
#include <QCheckBox>
#include <QListWidgetItem>
#include <QVariant>
#include <QVariantList>
#include <QFrame>
#include <QLayoutItem>
#include <QLayout>
#include <QTimer>
#include <QProgressDialog>
#include <QTemporaryDir>
#include <QWebEngineView>
#include <QUrl>
#include <QWebEngineSettings>



struct activeServices{
    bool RC = false;
    bool RDBI = false;
    bool WDBI = false;
};





QT_BEGIN_NAMESPACE
namespace Ui { class Dialog; }
QT_END_NAMESPACE

class Dialog : public QDialog
{
    Q_OBJECT

public:
    Dialog(QWidget *parent = nullptr);
    ~Dialog();

    trio getTrio();

signals :
    void changeL(QLayout* layout);
    void changeSA();
    void changeLWidg(QWidget* widget);


private slots:
    void on_pushButton_clicked();

    void on_btnPrvs_clicked();

    void on_toolButton_clicked();

    void on_btnProceedTests_clicked();

    void executeCurrentTest();

    void on_btnExecuteTests_clicked();

    void on_btnSrcPath_clicked();

    void on_btnCfgPath_clicked();

    void on_btnIncPath_clicked();

    void on_btnPrcdRC_clicked();

    void on_btnPrcdRDBI_clicked();

    void on_btnPrcdWDBI_clicked();

    void on_pushButtonRDBI_clicked();

    void on_btnExecuteTestsRDBI_clicked();

    void on_btnProceedTestsWDBI_clicked();

    void on_btnExecuteTestsWDBI_clicked();



    void on_btnServicePrcd_clicked();

private:
    Ui::Dialog *ui;
    QString pathName;

    QList<trio> testsList;
    QList<trio> testsChosnList;
    trio toSend;

    QList<duo> testsListDuo;
    QList<duo> testsChosnListDuo;

    QList<duo> testsListDuoW;
    QList<duo> testsChosnListDuoW;


    QString lclPath;
    QString srcPath;
    QString cfgPath;
    QString incPath;
    int timmer;
    int count = 0;

    activeServices servicesChosen;
};
#endif // DIALOG_H
