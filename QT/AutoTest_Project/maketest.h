#ifndef MAKETEST_H
#define MAKETEST_H

#include <QDialog>
#include <QAbstractButton>
#include <QPushButton>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QLineEdit>
#include <QLabel>
#include <string.h>
#include <QDebug>
#include <QMessageBox>
#include <QCheckBox>
#include <QSet>
#include <QStringList>




#ifndef STRUCTS //defining the data structure to hold each test info
#define STRUCTS
struct trio {
    QString RoutineName;
    QString Id;
    int params;
    bool done = false;
    QList<QString> Args;
    QList<QString> argsLbls;
    QCheckBox* chkBx;
    QPushButton* btn;
    QString dataToSend;
    QLineEdit* rep; // to hold how many times a test should be repeated

};


struct duo{

    QString RoutineName;
    QString Id;
    bool done = false;
    QCheckBox* chkBx;
    QPushButton* btn;
    QString dataToSend;
    QLineEdit* dataLine;
    QLineEdit* rep; // to hold how many times a test should be repeated
};

#endif



namespace Ui {
class MakeTest;
}

class MakeTest : public QDialog
{
    Q_OBJECT

public:
    explicit MakeTest(QWidget *parent = nullptr);
    ~MakeTest();

    void assignValues(trio temp);
    trio getTrio();



private slots:

    void on_btnCancel_clicked();

    void on_btnPrcd_clicked();

private:
    Ui::MakeTest *ui;
    QList<QLineEdit*> lineLst;
    trio vbl;
    bool checkArgs();
};

#endif // MAKETEST_H
