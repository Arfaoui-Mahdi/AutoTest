#include "dialog.h"
#include "ui_dialog.h"

Dialog::Dialog(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::Dialog)
{
    ui->setupUi(this);
    this->setWindowTitle("AutoTest");
    this->setWindowIcon(QIcon("C:\\Users\\Mahdi\\Desktop\\FIN_Project\\logo_transparent.ico"));



    //Allow resize
    Qt::WindowFlags flags = 0;
    flags |= Qt::WindowMinMaxButtonsHint;
    flags |= Qt::WindowContextHelpButtonHint;
    setWindowFlags(flags);


    ui->btnPrvs->setEnabled(false);
    ui->stackedWidget->setCurrentIndex(0);

}

Dialog::~Dialog()
{
    delete ui;
}

trio Dialog::getTrio()
{
    return toSend;
}

void removeL ( QLayout* layout ) // function to clean layout childs
{
    QLayoutItem* child;
    while ( layout->count() != 0 ) {
        child = layout->takeAt ( 0 );
        if ( child->layout() != 0 ) {
            removeL ( child->layout() );
        } else if ( child->widget() != 0 ) {
            delete child->widget();
        }

        delete child;
    }
}




void Dialog::on_pushButton_clicked() // the Start Processing button
{




    if(ui->srcPath->text() == NULL){
        QMessageBox::critical(this,"Error", "Please Select The Source File ! ");
        return;
    }

    if(ui->cfgPath->text() == NULL){
        QMessageBox::critical(this,"Error", "Please Select The Cfg File ! ");
        return;
    }

    if(ui->incPath->text() == NULL){
        QMessageBox::critical(this,"Error", "Please Select The Include Directory !");
        return;
    }

    /*
    QLabel* lbl = new QLabel;
    QMovie* movie = new QMovie("C:\\Users\\Mahdi\\Downloads\\ajax-loader.gif");
    lbl->setMovie(movie);
    lbl->show();
    movie->start();
    */

    //Handling the progress bar

    QTimer* timm = new QTimer(this);
    QProgressDialog* pDlg = new QProgressDialog(this);
    int randomNumber = (rand() % 500) + 1;
    bool flag = true;

    QTemporaryDir* tempDir = new QTemporaryDir();
    if (tempDir->isValid()) {
        //qDebug()<< tempDir.path()+"/file"; //returns the unique directory path
        lclPath = tempDir->path()+"/file";
    }
    qDebug()<<lclPath;
    qDebug()<<srcPath;


    QProcess* pyFile = new QProcess(this);
    pyFile->start("python.exe",
                  QStringList("C:\\Users\\Mahdi\\Desktop\\FIN_Project\\Global.py")
                  << lclPath
                  << srcPath
                  << cfgPath
                  << incPath);



    //connect(pyFile, &QProcess::finished,loadDlg, &Loading::terminateAll);



    connect(pyFile, QOverload<int, QProcess::ExitStatus>::of(&QProcess::finished),
            [=](int exitCode, QProcess::ExitStatus exitStatus) mutable{

        ;
        pDlg->setValue(100);
        pDlg->close();
        flag = false;
        timm->stop();

        ui->pushButton->setEnabled(false);
        ui->cfgPath->setEnabled(false);
        ui->incPath->setEnabled(false);
        ui->srcPath->setEnabled(false);

        ui->stackedWidget->setCurrentIndex(7); // to choose which Service to Proceed
    });


    pDlg->open();
    pDlg->setMinimum(0);
    pDlg->setMaximum(100);
    pDlg->setLabelText("Please Wait");
    connect(timm, &QTimer::timeout, this, [=,&randomNumber]{
        if(count == 97){
            timm->stop();
            return;
        }
        pDlg->setValue(count)  ;
        count ++;
        //qDebug()<<count;
        randomNumber = (rand() % 500) + 1;
        timm->start(randomNumber);



    });



    timm->start(randomNumber);







}




void Dialog::on_btnPrvs_clicked()
{


    if(ui->stackedWidget->currentIndex() == 4){

        ui->btnPrcdRC->setChecked(Qt::CheckState::Unchecked);
        ui->btnPrcdRDBI->setChecked(Qt::CheckState::Unchecked);
        ui->btnPrcdWDBI->setChecked(Qt::CheckState::Unchecked);

        ui->btnPrcdRC->setCheckable(true);
        ui->btnPrcdRDBI->setCheckable(true);
        ui->btnPrcdWDBI->setCheckable(true);

        ui->btnPrcdRDBI->setEnabled(true);
        ui->btnPrcdWDBI->setEnabled(true);
        ui->btnPrcdRC->setEnabled(true);


        removeL(ui->VLayoutOfTests);
        removeL(ui->VLayoutConfirmTests);


        servicesChosen.RC = false ;
        servicesChosen.RDBI = false;
        servicesChosen.WDBI = false;

        testsList.clear();
        testsListDuo.clear();
        testsListDuoW.clear();
        testsChosnList.clear();
        testsChosnListDuo.clear();
        testsChosnListDuoW.clear();

        ui->btnPrvs->setEnabled(false);

        ui->stackedWidget->setCurrentIndex(7);



    }

    else if(ui->stackedWidget->currentIndex() == 5){

        testsChosnList.clear();
        testsChosnListDuo.clear();
        testsChosnListDuoW.clear();
        ui->stackedWidget->setCurrentIndex(4);
        ui->btnPrvs->setEnabled(true);



    }
    else if(ui->stackedWidget->currentIndex() == 6){

        ui->stackedWidget->setCurrentIndex(5);
        ui->btnPrvs->setEnabled(true);
    }

    else if (ui->stackedWidget->currentIndex() == 8){

        ui->stackedWidget->setCurrentIndex(5);
        ui->btnPrvs->setEnabled(true);
    }


}


void Dialog::on_toolButton_clicked() // the EXIT button
{   QFile file(lclPath+".txt");
    if(!file.exists()) reject();
    file.remove();
    file.close();
    QFile fileJ(lclPath+"-RC.json");
    if(!fileJ.exists()) reject();
    fileJ.remove();
    fileJ.close();
    QFile fileJW(lclPath+"-WDBI.json");
    if(!fileJW.exists()) reject();
    fileJW.remove();
    fileJW.close();
    QFile fileJR(lclPath+"-RDBI.json");
    if(!fileJR.exists()) reject();
    fileJR.remove();
    fileJR.close();
    reject();

}


/*
 *
void Dialog::on_btnExcTests_clicked() //Button "Choose Tests"
{
    QList<QListWidgetItem*> items = ui->listWidget->selectedItems();
    foreach (QListWidgetItem* item, items){

        foreach (trio thing, testsList){

            QString nameT = item->text();
            if(thing.RoutineName == nameT){
                testsChosnList.append(thing);
            }

        }
    }

    if(testsChosnList.isEmpty()) qCritical()<< "Please choose Test(s) to execute !!! ";

    foreach(trio item, testsChosnList){
        ui->chsTestListWidget->addItem(item.RoutineName);
    }




    ui->stackedWidget->setCurrentIndex(3);
}
*/







/*

void Dialog::on_chsTestListWidget_itemDoubleClicked(QListWidgetItem *item) //double click on item widget
{
  MakeTest* dlgTest = new MakeTest(this);
  QString testName = item->text();

  foreach (trio item, testsChosnList){
      if(item.RoutineName == testName) toSend = item;
  }
  dlgTest->assignValues(toSend);
  dlgTest->exec();

  trio tmp = dlgTest->getTrio();
  int i = 0;
  for( i = 0; i<testsChosnList.size(); i ++){
      if(testsChosnList[i].RoutineName == tmp.RoutineName){
          testsChosnList[i]=tmp;
          break;
      }
  }


     TESING
  qDebug()<<testsChosnList[i].RoutineName;
  qDebug()<<testsChosnList[i].Id;
  qDebug()<<testsChosnList[i].params;
  qDebug()<<testsChosnList[i].Args;
  qDebug()<<testsChosnList[i].done;



}
*/



void Dialog::on_btnProceedTests_clicked()
{

    ui->btnPrvs->setEnabled(true);



    removeL(ui->VLayoutConfirmTests);

    if(servicesChosen.RC == true){        // Handling RC rendering
        qDebug()<<"i'm here RC";
        //********* Add a line separator **********
        QFrame *line1 = new QFrame(ui ->VLayoutConfirmTests->widget());
        line1->setFrameShape(QFrame::HLine); // Horizontal line
        line1->setFrameShadow(QFrame::Sunken);
        line1->setLineWidth(1);

        ui ->VLayoutConfirmTests->addWidget(line1);
        //***************************//
        QLabel* serviceNa = new QLabel("Routine Control Service",ui ->VLayoutConfirmTests->widget());
        QFont font("Exo 2", 10, QFont::Bold, true);
        font.setPointSize(20);
        serviceNa->setFont(font);
        serviceNa->setAlignment(Qt::AlignHCenter);
        ui ->VLayoutConfirmTests->addWidget(serviceNa);
        //********* Add a line separator **********
        QFrame *line2 = new QFrame(ui ->VLayoutConfirmTests->widget());
        line2->setFrameShape(QFrame::HLine); // Horizontal line
        line2->setFrameShadow(QFrame::Sunken);
        line2->setLineWidth(1);

        ui ->VLayoutConfirmTests->addWidget(line2);
        //***************************//




        QString alert("These routine are not configured :\n");

        QHBoxLayout* topHBox = new QHBoxLayout(ui ->VLayoutConfirmTests->widget());
        QLabel* name = new QLabel("Name", topHBox->widget());
        QLabel* id = new QLabel("ID", topHBox->widget());
        QLabel* args = new QLabel("Args", topHBox->widget());
        QLabel* count = new QLabel("Coutn", topHBox->widget());
        topHBox->addWidget(name, 4 );
        topHBox->addWidget(id, 2);
        topHBox->addWidget(args, 4);
        topHBox->addWidget(count, 2);
        ui->VLayoutConfirmTests->addLayout(topHBox);

        //********* Add a line separator **********
        QFrame *line = new QFrame(ui ->VLayoutConfirmTests->widget());
        line->setFrameShape(QFrame::HLine); // Horizontal line
        line->setFrameShadow(QFrame::Sunken);
        line->setLineWidth(1);


        ui->VLayoutConfirmTests->addWidget(line);
        //***************************//
        // bool flag = true;

        if(testsChosnList.isEmpty()){


            for (int i = 0 ; i < testsList.size() ; i++ ) {

                if(testsList[i].chkBx->isChecked()){
                    if(testsList[i].done == false){
                        alert= alert + testsList[i].RoutineName + "\n";
                        testsList[i].chkBx->setCheckState(Qt::CheckState::Unchecked);
                        //flag = false;
                    }

                    else {

                        testsChosnList.append(testsList[i]);

                    }


                }
            }
            if(alert != "These routine are not configured :\n") QMessageBox::information(this, "Please, finish configuration", alert);

        }
        else{ // In the case the List is not empty : the user already saw a confirmed list
            QList<QString> namesChosen ;
            for (int i = 0; i< testsChosnList.size()  ;i++ ) {
                namesChosen.append(testsChosnList[i].RoutineName);
            }


            for (int i = 0 ; i < testsList.size() ; i++ ) {

                if(testsList[i].chkBx->isChecked()){ // to add a checked test
                    if(testsList[i].done == true){

                        QString name = testsList[i].RoutineName;
                        if(!namesChosen.contains(name)){
                            testsChosnList.append(testsList[i]);
                        }

                    }
                    else{
                        alert= alert + testsList[i].RoutineName + "\n";
                        testsList[i].chkBx->setCheckState(Qt::CheckState::Unchecked);
                    }


                }

                else{ // in case the user unchecked a test

                    QString name = testsList[i].RoutineName;
                    testsList[i].done = false;
                    testsList[i].chkBx->setCheckState(Qt::CheckState::Unchecked);

                    //testsChosnList.removeOne(testsList[i]);
                    for (int k = 0; k < testsChosnList.size() ; k++ ) {
                        if(name == testsChosnList[k].RoutineName){
                            testsChosnList.removeAt(k);

                        }
                    }
                }
            }
            if(alert != "These routine are not configured :\n") QMessageBox::information(this, "Please, finish configuration", alert);

        }


        for (int i = 0; i < testsChosnList.size() ; i++ ) {
            qDebug()<< testsChosnList[i].RoutineName;
            QHBoxLayout* hBox = new QHBoxLayout(ui ->VLayoutConfirmTests->widget());
            QVBoxLayout* sVBox = new QVBoxLayout(hBox->widget());
            QLabel* rName = new QLabel(testsChosnList[i].RoutineName, hBox->widget());
            QLabel* rId = new QLabel(testsChosnList[i].Id, hBox->widget());
            QLabel* rCount = new QLabel(testsChosnList[i].rep->text(), this);


            hBox->addWidget(rName,4);
            hBox->addWidget(rId,2);

            QHBoxLayout* lHBox;
            QLabel* argLbl;
            QLabel* argN;
            for (int j = 0 ; j < testsChosnList[i].Args.size() ; j++ ) { //preparing list of args
                lHBox = new QHBoxLayout(sVBox->widget());
                argLbl = new QLabel(testsChosnList[i].argsLbls[j] + ":", lHBox->widget());
                argN = new QLabel(testsChosnList[i].Args[j], lHBox->widget());


                lHBox->addWidget(argLbl);
                lHBox->addWidget(argN);
                sVBox->addLayout(lHBox);
            }


            QFrame* frame = new QFrame(ui->VLayoutConfirmTests->widget());
            frame->setFrameShape(QFrame::StyledPanel);
            frame->setFrameShadow(QFrame::Plain);

            hBox->addLayout(sVBox,4);

            hBox->addWidget(rCount,2);

            frame->setLayout(hBox);

            ui->VLayoutConfirmTests->addWidget(frame);
            ui->scrollArea_2->setWidget(ui->VLayoutConfirmTests->widget());


        }




        //********* Add a line separator **********
        QFrame *line3 = new QFrame(ui ->VLayoutConfirmTests->widget());
        line3->setFrameShape(QFrame::HLine); // Horizontal line
        line3->setFrameShadow(QFrame::Sunken);
        line3->setLineWidth(1);

        ui ->VLayoutConfirmTests->addWidget(line3);
        //***************************//

    }

    if(servicesChosen.RDBI == true){ //Handling RDBI rendering


        //removeL(ui->VLayoutConfirmTests);


        //********* Add a line separator **********
        QFrame *line1 = new QFrame(ui ->VLayoutConfirmTests->widget());
        line1->setFrameShape(QFrame::HLine); // Horizontal line
        line1->setFrameShadow(QFrame::Sunken);
        line1->setLineWidth(1);

        ui ->VLayoutConfirmTests->addWidget(line1);
        //***************************//
        QLabel* serviceNa = new QLabel("Read Data By Identifier Service",ui ->VLayoutOfTests->widget());
        QFont font("Exo 2", 10, QFont::Bold, true);
        font.setPointSize(20);
        serviceNa->setFont(font);
        serviceNa->setAlignment(Qt::AlignHCenter);
        ui ->VLayoutConfirmTests->addWidget(serviceNa);
        //********* Add a line separator **********
        QFrame *line2 = new QFrame(ui ->VLayoutOfTests->widget());
        line2->setFrameShape(QFrame::HLine); // Horizontal line
        line2->setFrameShadow(QFrame::Sunken);
        line2->setLineWidth(1);

        ui ->VLayoutConfirmTests->addWidget(line2);
        //***************************//



        QHBoxLayout* topHBox = new QHBoxLayout(ui->VLayoutConfirmTests->widget());
        QLabel* name = new QLabel("Name", topHBox->widget());
        QLabel* id = new QLabel("ID", topHBox->widget());
        topHBox->addWidget(name,4);
        topHBox->addWidget(id,2);

        QLabel* count = new QLabel("Count", topHBox->widget());
        topHBox->addWidget(count,2);

        ui->VLayoutConfirmTests->addLayout(topHBox);

        //********* Add a line separator **********
        QFrame *line = new QFrame(ui->VLayoutConfirmTests->widget());
        line->setFrameShape(QFrame::HLine); // Horizontal line
        line->setFrameShadow(QFrame::Sunken);
        line->setLineWidth(1);

        ui->VLayoutConfirmTests->addWidget(line);
        //***************************//

        //Filtering accepted tests to do

        if(testsChosnListDuo.isEmpty()){


            for (int i = 0 ; i < testsListDuo.size() ; i++ ) {

                if(testsListDuo[i].chkBx->isChecked()){

                    testsChosnListDuo.append(testsListDuo[i]);

                }
            }
        }
        else{ // In the case the List is not empty : the user already saw a confirmed list
            QList<QString> namesChosen ;
            for (int i = 0; i< testsChosnListDuo.size()  ;i++ ) {
                namesChosen.append(testsChosnListDuo[i].RoutineName);
            }


            for (int i = 0 ; i < testsListDuo.size() ; i++ ) {

                if(testsListDuo[i].chkBx->isChecked()){ // to add a checked test

                    QString name = testsListDuo[i].RoutineName;
                    if(!namesChosen.contains(name)){
                        testsChosnListDuo.append(testsListDuo[i]);
                    }
                }
                else{ // in case the user unchecked a test

                    QString name = testsListDuo[i].RoutineName;

                    //testsChosnListDuo.removeOne(testsListDuo[i]);
                    for (int k = 0; k < testsChosnListDuo.size() ; k++ ) {
                        if(name == testsChosnListDuo[k].RoutineName){
                            testsChosnListDuo.removeAt(k);
                        }
                    }
                }
            }
        }


        for (int i = 0; i < testsChosnListDuo.size() ; i++ ) {

            QFrame* frame = new QFrame(ui->VLayoutConfirmTests->widget());
            QHBoxLayout* hBox = new QHBoxLayout(frame);
            QVBoxLayout* sVBox = new QVBoxLayout(hBox->widget());
            QLabel* rName = new QLabel(testsChosnListDuo[i].RoutineName, hBox->widget());
            QLabel* rId = new QLabel(testsChosnListDuo[i].Id, hBox->widget());



            hBox->addWidget(rName,4);
            hBox->addWidget(rId,2);

            QLabel* rCount = new QLabel(testsChosnListDuo[i].rep->text(), hBox->widget());
            hBox->addWidget(rCount,2);


            frame->setFrameShape(QFrame::StyledPanel);
            frame->setFrameShadow(QFrame::Plain);

            hBox->addLayout(sVBox);
            frame->setLayout(hBox);

            ui->VLayoutConfirmTests->addWidget(frame);
            ui->scrollArea_2->setWidget(ui->VLayoutConfirmTests->widget());


        }






        //********* Add a line separator **********
        QFrame *line3 = new QFrame(ui ->VLayoutConfirmTests->widget());
        line3->setFrameShape(QFrame::HLine); // Horizontal line
        line3->setFrameShadow(QFrame::Sunken);
        line3->setLineWidth(1);

        ui ->VLayoutConfirmTests->addWidget(line3);
        //***************************//


    }

    if(servicesChosen.WDBI == true){
        //Handling WDBI rendering

        //removeL(ui->VLayoutConfirmTests);


        //********* Add a line separator **********
        QFrame *line1 = new QFrame(ui ->VLayoutConfirmTests->widget());
        line1->setFrameShape(QFrame::HLine); // Horizontal line
        line1->setFrameShadow(QFrame::Sunken);
        line1->setLineWidth(1);

        ui ->VLayoutConfirmTests->addWidget(line1);
        //***************************//
        QLabel* serviceNa = new QLabel("Write Data By Identifier Service",ui ->VLayoutConfirmTests->widget());
        QFont font("Exo 2", 10, QFont::Bold, true);
        font.setPointSize(20);
        serviceNa->setFont(font);
        serviceNa->setAlignment(Qt::AlignHCenter);
        ui ->VLayoutConfirmTests->addWidget(serviceNa);
        //********* Add a line separator **********
        QFrame *line2 = new QFrame(ui ->VLayoutConfirmTests->widget());
        line2->setFrameShape(QFrame::HLine); // Horizontal line
        line2->setFrameShadow(QFrame::Sunken);
        line2->setLineWidth(1);

        ui ->VLayoutConfirmTests->addWidget(line2);
        //***************************//



        QHBoxLayout* topHBox = new QHBoxLayout( ui->VLayoutConfirmTests->widget());
        QLabel* name = new QLabel("Name", topHBox->widget());
        QLabel* id = new QLabel("ID", topHBox->widget());
        QLabel* dataLbl = new QLabel("Data", topHBox->widget());
        topHBox->addWidget(name,3);
        topHBox->addWidget(id,2);
        topHBox->addWidget(dataLbl,5);

        QLabel* count = new QLabel("Count", topHBox->widget());
        topHBox->addWidget(count,2);

        ui->VLayoutConfirmTests->addLayout(topHBox);

        //********* Add a line separator **********

        QFrame *line = new QFrame(ui->VLayoutConfirmTests->widget());
        line->setFrameShape(QFrame::HLine); // Horizontal line
        line->setFrameShadow(QFrame::Sunken);
        line->setLineWidth(1);

        ui->VLayoutConfirmTests->addWidget(line);
        //***************************//


        if(testsChosnListDuoW.isEmpty()){


            for (int i = 0 ; i < testsListDuoW.size() ; i++ ) {

                if(testsListDuoW[i].chkBx->isChecked()){
                    if(testsListDuoW[i].dataLine->text().size() != 0){ // If the Data field is not empty

                        testsChosnListDuoW.append(testsListDuoW[i]);
                    }

                }
            }
        }
        else{ // In the case the List is not empty : the user already saw a confirmed list
            QList<QString> namesChosen ;
            for (int i = 0; i< testsChosnListDuoW.size()  ;i++ ) {
                namesChosen.append(testsChosnListDuoW[i].RoutineName);
            }


            for (int i = 0 ; i < testsListDuoW.size() ; i++ ) {

                if(testsListDuoW[i].chkBx->isChecked()){ // to add a checked test
                    if(testsListDuoW[i].dataLine->text().size() != 0){ // If the Data field is not empty


                        QString name = testsListDuoW[i].RoutineName;
                        if(!namesChosen.contains(name)){
                            testsChosnListDuoW.append(testsListDuoW[i]);
                        }
                    }
                }
                else{ // in case the user unchecked a test

                    QString name = testsListDuoW[i].RoutineName;

                    //testsChosnListDuo.removeOne(testsListDuo[i]);
                    for (int k = 0; k < testsChosnListDuoW.size() ; k++ ) {
                        if(name == testsChosnListDuoW[k].RoutineName){
                            testsChosnListDuoW.removeAt(k);
                        }
                    }
                }
            }
        }


        for (int i = 0; i < testsChosnListDuoW.size() ; i++ ) {


            testsChosnListDuoW[i].dataToSend = testsChosnListDuoW[i].dataLine->text();

            QFrame* frame = new QFrame(ui->VLayoutConfirmTests->widget());

            QHBoxLayout* hBox = new QHBoxLayout(frame);
            QVBoxLayout* sVBox = new QVBoxLayout(hBox->widget());
            QLabel* rName = new QLabel(testsChosnListDuoW[i].RoutineName, hBox->widget());
            QLabel* rId = new QLabel(testsChosnListDuoW[i].Id, hBox->widget());
            QLabel* rData = new QLabel(testsChosnListDuoW[i].dataToSend, hBox->widget());



            hBox->addWidget(rName,3);
            hBox->addWidget(rId,2);
            hBox->addWidget(rData,5);



            frame->setFrameShape(QFrame::StyledPanel);
            frame->setFrameShadow(QFrame::Plain);

            hBox->addLayout(sVBox);
            QLabel* rCount = new QLabel(testsChosnListDuoW[i].rep->text(), hBox->widget());
            hBox->addWidget(rCount,2);

            frame->setLayout(hBox);

            ui->VLayoutConfirmTests->addWidget(frame);
            ui->scrollArea_2->setWidget(ui->VLayoutConfirmTests->widget());


        }



        //********* Add a line separator **********
        QFrame *line3 = new QFrame(ui ->VLayoutConfirmTests->widget());
        line3->setFrameShape(QFrame::HLine); // Horizontal line
        line3->setFrameShadow(QFrame::Sunken);
        line3->setLineWidth(1);

        ui ->VLayoutConfirmTests->addWidget(line3);
        //***************************//





    }

    ui->stackedWidget->setCurrentIndex(5);

}






void Dialog::executeCurrentTest()
{
    // qDebug()<< "================"<<testsList.size()<<"==========" ;
    trio temp;
    for (int j = 0; j< testsList.size() ; j++ ) {

        // qDebug() << testsList[j].RoutineName<<" "<< testsList[j].Id <<" "<< testsList[j].params << testsList[j].argsLbls <<
        //  testsList[j].btn->isChecked()<<"\n";
        // qDebug() << j << "\n";
        if(testsList[j].btn->isChecked()){

            testsList[j].btn->setChecked(false);

            if(testsList[j].argsLbls.isEmpty()){

                QMessageBox::information(this,"Error","This -TEST- is deficient due to some Technical Difficulties.");
                testsList[j].chkBx->setEnabled(false);
                testsList[j].rep->setEnabled(false);
                testsList[j].btn->setEnabled(false);
                return;
                break;
            }
            if(testsList[j].argsLbls[0]=="None"){

                testsList[j].done = true;
                testsList[j].chkBx->setCheckState(Qt::CheckState::Checked);
                break;
            }
            else{



                // qDebug()<< testsList[j].RoutineName;
                temp = testsList[j];

                //qDebug()<<"========================================================================";

                MakeTest* dlgTest = new MakeTest(ui->VLayoutOfTests->widget());
                dlgTest->assignValues(temp);
                dlgTest->exec();

                trio tmp = dlgTest->getTrio();
                testsList[j].Args = tmp.Args;
                testsList[j].done = tmp.done;
                testsList[j].dataToSend = tmp.dataToSend;
                testsList[j].argsLbls = tmp.argsLbls;
                if(testsList[j].done == true){
                    testsList[j].chkBx->setCheckState(Qt::CheckState::Checked);
                }
                break;

            }


        break;
        }

    }

/*
    for (int i = 0 ; i < testsList.size() ; i++ ) {
        if(testsList[i].done){
            testsList[i].chkBx->setCheckState(Qt::CheckState::Checked);
        }
    }




    MakeTest* dlgTest = new MakeTest(this);
    dlgTest->assignValues(temp);
    dlgTest->exec();

    trio tmp = dlgTest->getTrio();
    int i = 0;
    for( i = 0; i<testsList.size(); i ++){
        if(testsList[i].RoutineName == tmp.RoutineName){
            testsList[i]=tmp;
            break;
        }
    }



    qDebug()<<testsList[i].RoutineName;
    qDebug()<<testsList[i].Id;
    qDebug()<<testsList[i].params;
    qDebug()<<testsList[i].Args;
    qDebug()<<testsList[i].done;

*/


}
/*
void Dialog::goToTests()
{
    ui->stackedWidget->setCurrentIndex(4);
    ui->btnPrvs->setEnabled(true);
}

*/




void Dialog::on_btnExecuteTests_clicked()
{
    QString pyProccessingPath = "C:\\Users\\Mahdi\\Desktop\\FIN_Project\\Tester_and_Report_Generator\\HTMLTestRunner.py";

    QStringList rcList;
    QStringList rdbiList;
    QStringList wdbiList;
    int NOS = 0;
    QStringList servicesNames;
    QStringList numberOfServicesTests;
    QStringList listOFArgs (pyProccessingPath);

    if(servicesChosen.RC == true){
        NOS += 1 ;
       // QStringList listOFArgs (pyProccessingPath);
       // listOFArgs<<"RC";
        servicesNames.append("RC");
       //listOFArgs << QString::number(testsChosnList.length());
        numberOfServicesTests.append(QString::number(testsChosnList.length()));


        for (int i = 0; i < testsChosnList.size() ; i++ ) {
            rcList<<testsChosnList[i].RoutineName;
            rcList<<testsChosnList[i].Id;
            rcList<<testsChosnList[i].dataToSend;
            rcList<<testsChosnList[i].rep->text();
            rcList<< QString::number(i);


        }





    }


    if(servicesChosen.RDBI == true){
        NOS += 1 ;
        //QStringList listOFArgs (pyProccessingPath);
       // listOFArgs<<"RDBI";
        servicesNames.append("RDBI");
        //listOFArgs << QString::number(testsChosnListDuo.length());
        numberOfServicesTests.append(QString::number(testsChosnListDuo.length()));


        for (int i = 0; i < testsChosnListDuo.size() ; i++ ) {
            rdbiList<<testsChosnListDuo[i].RoutineName;
            rdbiList<<testsChosnListDuo[i].Id;
            rdbiList<<testsChosnListDuo[i].dataToSend;
            rdbiList<<testsChosnListDuo[i].rep->text();
            rdbiList  << QString::number(i);


        }



    }



     if(servicesChosen.WDBI == true){
         NOS += 1 ;
       // QStringList listOFArgs (pyProccessingPath);
       // listOFArgs<<"WDBI";
        servicesNames.append("WDBI");
       // listOFArgs << QString::number(testsChosnListDuoW.length());
        numberOfServicesTests.append(QString::number(testsChosnListDuoW.length()));

        for (int i = 0; i<testsChosnListDuoW.size() ; i++ ) {
            //qDebug()<<testsChosnListDuo[i].RoutineName;

            for (int i = 0; i < testsChosnListDuoW.size() ; i++ ) {
                wdbiList<<testsChosnListDuoW[i].RoutineName;
                wdbiList<<testsChosnListDuoW[i].Id;
                wdbiList<<testsChosnListDuoW[i].dataToSend;
                wdbiList<<testsChosnListDuoW[i].rep->text();
                wdbiList  << QString::number(i);
            }


        }


    }


    //*********************Preparing the Data to send***********

     listOFArgs << QString::number(NOS);
     foreach(QString item, servicesNames){
         listOFArgs << item;
     }

     foreach(QString item, numberOfServicesTests){
         listOFArgs  << item;
     }

     foreach(QString item, servicesNames){
         if(item == "RC"){
             foreach(QString obj, rcList){
                 listOFArgs << obj;
             }
         }

         else if(item == "RDBI"){
             foreach(QString obj, rdbiList){
                 listOFArgs << obj;
             }
         }

         else if(item == "WDBI"){
             foreach(QString obj, wdbiList){
                 listOFArgs << obj;
             }
         }
     }


     //foreach(QString item, listOFArgs){
         //qDebug() << item;
    // }



    foreach(QString item, listOFArgs) qDebug()<< item + "\n";

    //***************************************
     QProcess* pyFile = new QProcess(this);

     pyFile->start("python.exe", listOFArgs);

     //qDebug()<< testsChosnList[i].RoutineName << testsChosnList[i].Id << testsChosnList[i].Args << testsChosnList[i].dataToSend ;
     pyFile->waitForFinished(-1);

     QString filePath = "C:\\Users\\Mahdi\\Desktop\\FIN_Project\\Tester_and_Report_Generator\\templates\\TEESSSSSEEEETOO_report.html";
     QWebEngineView *view = new QWebEngineView(this);
     QWebEngineSettings* sett = view->settings();
     sett->setAttribute(QWebEngineSettings::PluginsEnabled, true);

     sett->setAttribute(QWebEngineSettings::WebGLEnabled, true);

     view->load(QUrl::fromLocalFile(filePath));
     ui->resScrollArea->setWidget(view);
     view->showFullScreen();
     ui->stackedWidget->setCurrentIndex(8);



}








void Dialog::on_btnSrcPath_clicked()
{
    srcPath = QFileDialog::getOpenFileName(this,"Select the Source File");
    ui->srcPath->setText(srcPath);
    qDebug()<< srcPath;
}

void Dialog::on_btnCfgPath_clicked()
{
    cfgPath = QFileDialog::getOpenFileName(this,"Select the Cfg File");
    ui->cfgPath->setText(cfgPath);
    qDebug()<< cfgPath;
}

void Dialog::on_btnIncPath_clicked()
{
    incPath = QFileDialog::getExistingDirectory(this, "Select the Inlude Directory");
    ui->incPath->setText(incPath);
    qDebug()<< incPath;
}




void Dialog::on_btnPrcdRC_clicked()
{   //qDebug()<< "RC Cliked";
    servicesChosen.RC = true;

    ui->btnPrcdRC->setCheckable(true);
    ui->btnPrcdRC->setChecked(Qt::CheckState::Checked);
    ui->btnPrcdRC->setEnabled(false);

    //********* Add a line separator **********
    QFrame *line1 = new QFrame(ui ->VLayoutOfTests->widget());
    line1->setFrameShape(QFrame::HLine); // Horizontal line
    line1->setFrameShadow(QFrame::Sunken);
    line1->setLineWidth(1);

    ui ->VLayoutOfTests->addWidget(line1);
    //***************************//
    QLabel* serviceNa = new QLabel("Routine Control Service",ui ->VLayoutOfTests->widget());
    QFont font("Exo 2", 10, QFont::Bold, true);
    font.setPointSize(20);
    serviceNa->setFont(font);
    serviceNa->setAlignment(Qt::AlignHCenter);
    ui ->VLayoutOfTests->addWidget(serviceNa);
    //********* Add a line separator **********
    QFrame *line2 = new QFrame(ui ->VLayoutOfTests->widget());
    line2->setFrameShape(QFrame::HLine); // Horizontal line
    line2->setFrameShadow(QFrame::Sunken);
    line2->setLineWidth(1);

    ui ->VLayoutOfTests->addWidget(line2);
    //***************************//



    //QScrollArea* scrollArea = new QScrollArea(ui->tabWidget);

    //VLayoutOfTests = new QVBoxLayout(ui->scrollArea);
    QHBoxLayout* topHLayout = new QHBoxLayout(ui->VLayoutOfTests->widget());
    QLabel* name = new QLabel("Name", topHLayout->widget());
    QLabel* id = new QLabel("Configure Test", topHLayout->widget());
    QLabel* dataLbl = new QLabel("Check Tests", topHLayout->widget());
    QLabel* countLbl = new QLabel("Count", topHLayout->widget());

    topHLayout->addWidget(name,4);
    topHLayout->addWidget(id,2);
    topHLayout->addWidget(dataLbl,2);
    topHLayout->addWidget(countLbl,3);

    ui ->VLayoutOfTests->addLayout(topHLayout);
    //emit(changeL(topHLayout));

    //********* Add a line separator **********
    QFrame *line = new QFrame(ui ->VLayoutOfTests->widget());
    line->setFrameShape(QFrame::HLine); // Horizontal line
    line->setFrameShadow(QFrame::Sunken);
    line->setLineWidth(1);

    ui ->VLayoutOfTests->addWidget(line);
    //***************************//


    //Handling the RC JSON

    QFile myFile(lclPath + "-RC" + ".json");
    myFile.open(QIODevice::ReadOnly|QIODevice::Text);
    QByteArray val = myFile.readAll();
    myFile.close();

    QJsonDocument d = QJsonDocument::fromJson(val);
    QJsonObject jObj = d.object();
    QJsonArray arr = d.array();



    QList<QVariant> lst ;
    QList<trio> globlLst;



    for (int i = 0 ; i < arr.size(); i++){
        trio tmp;
        lst.clear();
        lst = arr[i].toVariant().toList();

        tmp.RoutineName = lst[0].toString();
        tmp.Id =lst[1].toString();
        tmp.params = lst[2].toInt();
        QVariantList tempLst = lst[3].toList();
        foreach(QVariant item, tempLst){
            tmp.argsLbls.append(item.toString());
        }




        globlLst.append(tmp);


    }
    testsList = globlLst;

    for (int i = 0 ; i < globlLst.size(); i++){

       // qDebug() << globlLst[i].RoutineName<<" "<< globlLst[i].Id <<" "<< globlLst[i].params << globlLst[i].argsLbls<<"\n";
        //ui->listWidget->addItem(testsList[i].RoutineName);

        // ****** TRYING the new way on displaying the tests ******//
        QHBoxLayout* hBox = new QHBoxLayout(ui->VLayoutOfTests->widget());
        testsList[i].chkBx = new QCheckBox(hBox->widget());
        testsList[i].chkBx->setCheckState(Qt::CheckState::Unchecked);
        QLabel* rName = new QLabel(testsList[i].RoutineName, hBox->widget());
        //QLabel* rId = new QLabel(globlLst[i].Id, this);
        testsList[i].btn = new QPushButton("Configure this Test", hBox->widget());
        testsList[i].btn->setCheckable(true);
        testsList[i].btn->setChecked(false);



        QObject::connect(testsList[i].btn, &QPushButton::clicked, this ,&Dialog::executeCurrentTest);


        testsList[i].rep = new QLineEdit("1", hBox->widget());


        hBox->addWidget(rName,4);
        hBox->addWidget(testsList[i].btn,2);
        hBox->addWidget(testsList[i].chkBx,2);
        hBox->addWidget(testsList[i].rep,3);

        ui -> VLayoutOfTests->addLayout(hBox);
        //emit(changeL(hBox));





    }

    //scrollArea->setWidget(VLayoutOfTests->widget());



    //********* Add a line separator **********
    QFrame *line3 = new QFrame(ui ->VLayoutOfTests->widget());
    line3->setFrameShape(QFrame::HLine); // Horizontal line
    line3->setFrameShadow(QFrame::Sunken);
    line3->setLineWidth(1);

    ui ->VLayoutOfTests->addWidget(line3);
    //***************************//


    /*
    rcTab->modifieScrollArea();
    ui->tabWidget->insertTab(2, rcTab, "RC");
*/

    // ui->stackedWidget->setCurrentIndex(4); // page 4 : to see all the tests list

}






void Dialog::on_btnPrcdRDBI_clicked()
{
    servicesChosen.RDBI = true;

    ui->btnPrcdRDBI->setCheckable(true);
    ui->btnPrcdRDBI->setChecked(Qt::CheckState::Checked);
    ui->btnPrcdRDBI->setEnabled(false);

    //********* Add a line separator **********
    QFrame *line1 = new QFrame(ui ->VLayoutOfTests->widget());
    line1->setFrameShape(QFrame::HLine); // Horizontal line
    line1->setFrameShadow(QFrame::Sunken);
    line1->setLineWidth(1);

    ui ->VLayoutOfTests->addWidget(line1);
    //***************************//
    QLabel* serviceNa = new QLabel("Read Data By Identifier Service",ui ->VLayoutOfTests->widget());
    QFont font("Exo 2", 10, QFont::Bold, true);
    font.setPointSize(20);
    serviceNa->setFont(font);
    serviceNa->setAlignment(Qt::AlignHCenter);
    ui ->VLayoutOfTests->addWidget(serviceNa);
    //********* Add a line separator **********
    QFrame *line2 = new QFrame(ui ->VLayoutOfTests->widget());
    line2->setFrameShape(QFrame::HLine); // Horizontal line
    line2->setFrameShadow(QFrame::Sunken);
    line2->setLineWidth(1);

    ui ->VLayoutOfTests->addWidget(line2);
    //***************************//


    //Handling the RDBI JSON

    QFile myFile(lclPath + "-RDBI" + ".json");
    myFile.open(QIODevice::ReadOnly|QIODevice::Text);
    QByteArray val = myFile.readAll();
    myFile.close();

    QJsonDocument d = QJsonDocument::fromJson(val);
    QJsonObject jObj = d.object();
    QJsonArray arr = d.array();





    QList<QVariant> lst ;
    QList<duo> globlLst;

    //QVBoxLayout* VLayoutOfTests = new QVBoxLayout(this);
    QHBoxLayout* topHLayout = new QHBoxLayout(ui->VLayoutOfTests->widget());
    QLabel* name = new QLabel("Name", topHLayout->widget());
    QLabel* id = new QLabel("ID", topHLayout->widget());
    QLabel* dataLbl = new QLabel("Choose Tests", topHLayout->widget());
    QLabel* countLbl = new QLabel("Count", topHLayout->widget());

    topHLayout->addWidget(name,4);
    topHLayout->addWidget(id,2);
    topHLayout->addWidget(dataLbl,2);
    topHLayout->addWidget(countLbl,3);

    ui->VLayoutOfTests->addLayout(topHLayout);
    // emit(changeL(topHLayout));

    //********* Add a line separator **********
    QFrame *line = new QFrame(ui->VLayoutOfTests->widget());
    line->setFrameShape(QFrame::HLine); // Horizontal line
    line->setFrameShadow(QFrame::Sunken);
    line->setLineWidth(1);

    ui->VLayoutOfTests->addWidget(line);
    //emit(changeLWidg(line));
    //***************************//


    for (int i = 0 ; i < arr.size(); i++){
        duo tmp;
        lst.clear();
        lst = arr[i].toVariant().toList();

        tmp.RoutineName = lst[0].toString();
        tmp.Id =lst[1].toString();
        globlLst.append(tmp);


    }
    testsListDuo = globlLst;

    for (int i = 0 ; i < globlLst.size(); i++){

        //qDebug() << globlLst[i].RoutineName<<" "<< globlLst[i].Id <<" "<< globlLst[i].params << globlLst[i].argsLbls<<"\n";
        ui->listWidget->addItem(testsListDuo[i].RoutineName);

        // TRYING the new way on displaying the tests
        QHBoxLayout* hBox = new QHBoxLayout(ui->VLayoutOfTests->widget());

        testsListDuo[i].chkBx = new QCheckBox(ui->VLayoutOfTests->widget());
        testsListDuo[i].chkBx->setCheckState(Qt::CheckState::Unchecked);
        QLabel* rName = new QLabel(testsListDuo[i].RoutineName, hBox->widget());
        QLabel* rId = new QLabel(globlLst[i].Id, hBox->widget());

        //testsListDuo[i].btn = new QPushButton("Configure this Test", this);
        //testsListDuo[i].btn->setCheckable(true);
        //testsListDuo[i].btn->setChecked(false);
        // QObject::connect(testsListDuo[i].btn, &QPushButton::clicked, this ,&Dialog::executeCurrentTest);



        testsListDuo[i].rep = new QLineEdit("1", ui->VLayoutOfTests->widget());

        hBox->addWidget(rName,4);
        hBox->addWidget(rId,2);
        //hBox->addWidget(testsListDuo[i].btn);
        hBox->addWidget(testsListDuo[i].chkBx , 2);
        hBox->addWidget(testsListDuo[i].rep, 3);

        ui->VLayoutOfTests->addLayout(hBox);
        // emit(changeL(hBox));


    }
    //********* Add a line separator **********
    QFrame *line3 = new QFrame(ui ->VLayoutOfTests->widget());
    line3->setFrameShape(QFrame::HLine); // Horizontal line
    line3->setFrameShadow(QFrame::Sunken);
    line3->setLineWidth(1);

    ui ->VLayoutOfTests->addWidget(line3);
    //***************************//
    /*
    QScrollArea* scrollArea = new QScrollArea(this);

    scrollArea->setWidget(VLayoutOfTests->widget());
    ui->tabWidget->addTab(scrollArea,"RDBI");

*/



    //rdbiTab->modifieScrollArea();
    //ui->tabWidget->insertTab(0, rdbiTab, "RDBI");

    //ui->stackedWidget->setCurrentIndex(4); // page 4 : to see all the tests list


}





void Dialog::on_btnPrcdWDBI_clicked()
{

    servicesChosen.WDBI = true;

    ui->btnPrcdWDBI->setCheckable(true);
    ui->btnPrcdWDBI->setChecked(Qt::CheckState::Checked);
    ui->btnPrcdWDBI->setEnabled(false);



    //********* Add a line separator **********
    QFrame *line1 = new QFrame(ui ->VLayoutOfTests->widget());
    line1->setFrameShape(QFrame::HLine); // Horizontal line
    line1->setFrameShadow(QFrame::Sunken);
    line1->setLineWidth(1);

    ui ->VLayoutOfTests->addWidget(line1);
    //***************************//
    QLabel* serviceNa = new QLabel("Write Data By Identifier Service",ui ->VLayoutOfTests->widget());
    QFont font("Exo 2", 10, QFont::Bold, true);
    font.setPointSize(20);
    serviceNa->setFont(font);
    serviceNa->setAlignment(Qt::AlignHCenter);
    ui ->VLayoutOfTests->addWidget(serviceNa);
    //********* Add a line separator **********
    QFrame *line2 = new QFrame(ui ->VLayoutOfTests->widget());
    line2->setFrameShape(QFrame::HLine); // Horizontal line
    line2->setFrameShadow(QFrame::Sunken);
    line2->setLineWidth(1);

    ui ->VLayoutOfTests->addWidget(line2);
    //***************************//


    //Handling the WDBI JSON

    QFile myFile(lclPath + "-WDBI" + ".json");
    myFile.open(QIODevice::ReadOnly|QIODevice::Text);
    QByteArray val = myFile.readAll();
    myFile.close();

    QJsonDocument d = QJsonDocument::fromJson(val);
    QJsonObject jObj = d.object();
    QJsonArray arr = d.array();



    QList<QVariant> lst ;
    QList<duo> globlLst;



    for (int i = 0 ; i < arr.size(); i++){
        duo tmp;
        lst.clear();
        lst = arr[i].toVariant().toList();

        tmp.RoutineName = lst[0].toString();
        tmp.Id =lst[1].toString();
        globlLst.append(tmp);


    }
    testsListDuoW = globlLst;


    //QVBoxLayout* VLayoutOfTests = new QVBoxLayout(this);
    QHBoxLayout* topHLayout = new QHBoxLayout(ui->VLayoutOfTests->widget());
    QLabel* name = new QLabel("Name", topHLayout->widget());
    QLabel* id = new QLabel("ID", topHLayout->widget());
    QLabel* dataLbl = new QLabel("Data", topHLayout->widget());
    QLabel* countLbl = new QLabel("Count", topHLayout->widget());

    topHLayout->addWidget(name,3);
    topHLayout->addWidget(id,2);
    topHLayout->addWidget(dataLbl,5);
    topHLayout->addWidget(countLbl,3);

    ui->VLayoutOfTests->addLayout(topHLayout);
    //emit(changeL(topHLayout));

    //********* Add a line separator **********
    QFrame *line = new QFrame(ui->VLayoutOfTests->widget());
    line->setFrameShape(QFrame::HLine); // Horizontal line
    line->setFrameShadow(QFrame::Sunken);
    line->setLineWidth(1);

    ui->VLayoutOfTests->addWidget(line);
    //emit(changeLWidg(line));
    //***************************//



    for (int i = 0 ; i < globlLst.size(); i++){

        //qDebug() << globlLst[i].RoutineName<<" "<< globlLst[i].Id <<" "<< globlLst[i].params << globlLst[i].argsLbls<<"\n";
        ui->listWidget->addItem(testsListDuoW[i].RoutineName);

        // TRYING the new way on displaying the tests

        QHBoxLayout* hBox = new QHBoxLayout(ui->VLayoutOfTests->widget());
        testsListDuoW[i].chkBx = new QCheckBox(ui->VLayoutOfTests->widget());
        testsListDuoW[i].chkBx->setCheckState(Qt::CheckState::Unchecked);
        QLabel* rName = new QLabel(testsListDuoW[i].RoutineName, hBox->widget() );
        QLabel* rId = new QLabel(globlLst[i].Id, hBox->widget());

        testsListDuoW[i].dataLine = new QLineEdit(hBox->widget());
        testsListDuoW[i].dataLine->setPlaceholderText("Enter Data");


        testsListDuoW[i].rep = new QLineEdit("1", hBox->widget());

        hBox->addWidget(rName,3);
        hBox->addWidget(rId,2);
        hBox->addWidget(testsListDuoW[i].dataLine,5);
        hBox->addWidget(testsListDuoW[i].chkBx);
        hBox->addWidget(testsListDuoW[i].rep);


        ui ->VLayoutOfTests->addLayout(hBox);
        //emit(changeL(hBox));


    }


    //********* Add a line separator **********
    QFrame *line3 = new QFrame(ui ->VLayoutOfTests->widget());
    line3->setFrameShape(QFrame::HLine); // Horizontal line
    line3->setFrameShadow(QFrame::Sunken);
    line3->setLineWidth(1);

    ui ->VLayoutOfTests->addWidget(line3);
    //***************************//
    /*
    QScrollArea* scrollArea = new QScrollArea(this);

    scrollArea->setWidget(VLayoutOfTests->widget());
    ui->tabWidget->addTab(scrollArea,"WDBI");
*/


    //emit(changeSA());
    //wdbiTab->modifieScrollArea();
    //ui->tabWidget->insertTab(1, wdbiTab, "WDBI");


    //ui->stackedWidget->setCurrentIndex(4); // page 4 : to see all the tests list

}






void Dialog::on_pushButtonRDBI_clicked()
{

}

void Dialog::on_btnExecuteTestsRDBI_clicked()
{

}

void Dialog::on_btnProceedTestsWDBI_clicked()
{

}

void Dialog::on_btnExecuteTestsWDBI_clicked()
{

}

void Dialog::on_btnServicePrcd_clicked() // Choose services to TEST !!
{


    ui->scrollArea->setWidget(this->ui->VLayoutOfTests->widget());
    ui->btnPrvs->setEnabled(true);
    ui->stackedWidget->setCurrentIndex(4); // page 4 : to see all the tests list
}
