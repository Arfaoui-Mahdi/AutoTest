#include "makerdbitest.h"
#include "ui_makerdbitest.h"

makeRDBITest::makeRDBITest(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::makeRDBITest)
{
    ui->setupUi(this);
}

makeRDBITest::~makeRDBITest()
{
    delete ui;
}
