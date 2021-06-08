#include "makewdbitest.h"
#include "ui_makewdbitest.h"

makewdbitest::makewdbitest(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::makewdbitest)
{
    ui->setupUi(this);
}

makewdbitest::~makewdbitest()
{
    delete ui;
}
