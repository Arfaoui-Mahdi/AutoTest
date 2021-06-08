#ifndef MAKERDBITEST_H
#define MAKERDBITEST_H

#include <QDialog>

namespace Ui {
class makeRDBITest;
}

class makeRDBITest : public QDialog
{
    Q_OBJECT

public:
    explicit makeRDBITest(QWidget *parent = nullptr);
    ~makeRDBITest();

private:
    Ui::makeRDBITest *ui;
};

#endif // MAKERDBITEST_H
