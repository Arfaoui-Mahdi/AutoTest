#include "loading.h"
#include "ui_loading.h"

Loading::Loading(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Loading)
{
    ui->setupUi(this);
    showLoading();
}

Loading::~Loading()
{
    delete ui;
}

void Loading::showLoading()
{
    lbl = new QLabel;
    movie = new QMovie("C:\\Users\\Mahdi\\Downloads\\ajax-loader.gif");
    lbl->setMovie(movie);
    lbl->show();
    movie->start();
}

void Loading::terminateAll()
{
    movie->stop();
    lbl->close();
}


