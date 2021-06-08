#ifndef LOADING_H
#define LOADING_H

#include <QDialog>

#include <QLabel>
#include <QMovie>

namespace Ui {
class Loading;
}

class Loading : public QDialog
{
    Q_OBJECT

public:
    explicit Loading(QWidget *parent = nullptr);
    ~Loading();

    void showLoading();
public slots:
    void terminateAll();



private:
    Ui::Loading *ui;
    QLabel *lbl;
    QMovie *movie;

};

#endif // LOADING_H
