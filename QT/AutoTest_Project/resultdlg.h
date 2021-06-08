#ifndef RESULTDLG_H
#define RESULTDLG_H

#include <QDialog>

namespace Ui {
class resultDlg;
}

class resultDlg : public QDialog
{
    Q_OBJECT

public:
    explicit resultDlg(QWidget *parent = nullptr);
    ~resultDlg();

private:
    Ui::resultDlg *ui;
};

#endif // RESULTDLG_H
