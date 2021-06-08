#include "maketest.h"
#include "ui_maketest.h"

MakeTest::MakeTest(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::MakeTest)
{
    ui->setupUi(this);


}

MakeTest::~MakeTest()
{
    delete ui;
}

void MakeTest::assignValues(trio temp)
{
    vbl.RoutineName = temp.RoutineName;
    vbl.Id = temp.Id;
    vbl.done = temp.done;
    vbl.params = temp.params;
    vbl.argsLbls = temp.argsLbls;



    QStringList srtList = vbl.argsLbls;
    srtList.removeDuplicates();
    vbl.argsLbls = srtList;



    int numArgs = vbl.argsLbls.size();

    ui->lineEditTName->setText(temp.RoutineName);
    ui->lineEditTId->setText(temp.Id);

    if(numArgs != 0){

        for(int i = 0 ; i < numArgs; i++){

           QHBoxLayout* hBox = new QHBoxLayout(ui->verticalLayout_2->widget());
           QLineEdit *tmpEdit = new QLineEdit(hBox->widget());
           QString strr = vbl.argsLbls[i] + " :";
           QLabel* tmpLbl = new QLabel(strr,hBox->widget());

           hBox->addWidget(tmpLbl);
           hBox->addWidget(tmpEdit);
           ui->verticalLayout_2->addLayout(hBox);
           lineLst.append(tmpEdit);

        }


    }



}

trio MakeTest::getTrio()
{
 return vbl;
}


void MakeTest::on_btnCancel_clicked()
{

    reject();
}

void MakeTest::on_btnPrcd_clicked() //Proceed Button
{


  if(checkArgs()) {

      for (int i =0; i < lineLst.size() ;i++ ) {
          vbl.Args.append(lineLst[i]->text());
          vbl.done = true;
          vbl.dataToSend.append(lineLst[i]->text());
      }
      accept();
  }

  else {
      QMessageBox::information(this,"Error","Enter All Args !!");
      vbl.done = false;
      update();

  }


}



bool MakeTest::checkArgs()
{


    for (int i = 0; i<lineLst.size() ; i++ ) {

       if(lineLst[i]->text().isEmpty()){
           return false;
       }


    }
    return true;
}
