#ifndef MAKEWDBITEST_H
#define MAKEWDBITEST_H

#include <QDialog>

namespace Ui {
class makewdbitest;
}

class makewdbitest : public QDialog
{
    Q_OBJECT

public:
    explicit makewdbitest(QWidget *parent = nullptr);
    ~makewdbitest();

private:
    Ui::makewdbitest *ui;
};

#endif // MAKEWDBITEST_H
