#include "waitdialog.h"
#include "ui_waitdialog.h"

waitDialog::waitDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::waitDialog)
{
    ui->setupUi(this);

    this->setWindowTitle("Testing...");

    QMovie* movie = new QMovie(":/images/ajax-loader.gif");
    movie->setParent(this);
    ui->label_2->setMovie(movie);
    movie->start();
}

waitDialog::~waitDialog()
{
    delete ui;
}
