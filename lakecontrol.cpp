#include "lakecontrol.h"
#include "ni488.h"
#include "windows.h"

LakeControl::LakeControl(QWidget *parent) : QWidget(parent)
{
    setupUi(this);
    connect(exitButton, SIGNAL(clicked()),this, SLOT(close()));
    connect(getButton,SIGNAL(clicked()),this,SLOT(onGetState()));
    connect(scanButton,SIGNAL(clicked()),this,SLOT(onScan()));
    connect(pointButton,SIGNAL(clicked()),this,SLOT(onSetpoint()));
    connect(hoffButton,SIGNAL(clicked()),this,SLOT(onHeaterOff()));
    connect(heaterButton,SIGNAL(clicked()),this,SLOT(onSetRange()));
    connect(resButton,SIGNAL(clicked()),this,SLOT(onSetResistance()));
    connect(rateButton,SIGNAL(clicked()),this,SLOT(onRamp()));
    connect(rampCheck,SIGNAL(stateChanged(int)),this,SLOT(onRampCheck(int)));
    connect(powerCheck,SIGNAL(stateChanged(int)),this,SLOT(onPowerCheck(int)));
    connect(enCheck,SIGNAL(stateChanged(int)),this,SLOT(onEnableCheck(int)));
    connect(instrList,SIGNAL(currentIndexChanged(int)),this,SLOT(onGetState()));
    gboard board();
    pointButton->setEnabled(false);
    hoffButton->setEnabled(false);
    heaterButton->setEnabled(false);
    resButton->setEnabled(false);
    rateButton->setEnabled(false);
    rampCheck->setEnabled(false);
    powerCheck->setEnabled(false);
    }

void LakeControl::onGetState()
{
// ANALOG?<output> - <bipolar enable>,<mode>,<input>,<source>,<high value>,
    //<low value>,<manual value>, format: n,n,ann,n,+-nnn.nnnE+-n,+-nnn.nnnE+-n,+-nnn.n[term]
//HTR? - heater output - nnn.nn[term]
//RAMP?<loop> - ramp settings - <off/on>,<rate value>, format:nnn.n[term]
//RAMPST?<loop> - ramp status, format:n[term]
//SETP?<loop> - current setpoint, format: +-nnn.nnE+-n[term]
//RANGE? - heater range, format: n[term]
//CDISP?
    //CLIMI?
    if(instrList->currentText()==NULL)
    {
        stateEdit->setText("No instrument selected!");
        return;
    }
    gdevice dev(comboBox->currentText().toInt(),extractAdress(instrList->currentText()),
                extractType(instrList->currentText()));
//    board.writeCommand(dev, "HTRST?");
//    QString data=board.receiveData(dev);
    stateEdit->clear();
//    if(data=="05")
//    {
//        stateEdit->append("Open Heater Load!!! "+data);
//    }
//    if(data=="06")
//    {
//        stateEdit->append("Heater Load is less than 10 Ohm!!! "+data);
//    }
    board.writeCommand(dev, "ANALOG?1");
    QString data=board.receiveData(dev);
    stateEdit->append("Analog output 1: "+data);
    board.writeCommand(dev, "ANALOG?2");
    data=board.receiveData(dev);
    stateEdit->append("Analog output 2: "+data);
    board.writeCommand(dev, "AOUT?1");
    data=board.receiveData(dev);
    stateEdit->append("Analog output 1 value: "+data);
    board.writeCommand(dev, "AOUT?2");
    data=board.receiveData(dev);
    stateEdit->append("Analog output 2 value: "+data);
    board.writeCommand(dev, "HTR?");
    data=board.receiveData(dev);
    stateEdit->append("Heater output: "+data);
    board.writeCommand(dev, "RAMP?1");
    data=board.receiveData(dev);
    if(data.section(',',0,0).toShort())
            rampCheck->setChecked(true);
    else
        rampCheck->setChecked(false);
    rampSpin->setValue(data.section(',',1,1).toDouble());
    stateEdit->append("Ramp settings: "+data);
    board.writeCommand(dev, "RAMPST?1");
    data=board.receiveData(dev);
    stateEdit->append("Ramp status: "+data);
    board.writeCommand(dev, "CSET?1");
    data=board.receiveData(dev);
    if(data.section(',',3,3).toShort())
            powerCheck->setChecked(true);
    else
        powerCheck->setChecked(false);
    if(data.section(',',2,2).toShort())
            enCheck->setChecked(true);
    else
        enCheck->setChecked(false);
    board.writeCommand(dev, "SETP?1");
    data=board.receiveData(dev);
    stateEdit->append("Current setpoint: "+data);
    pointSpin->setValue(data.toDouble());
    board.writeCommand(dev, "RANGE?");
    data=board.receiveData(dev);
    stateEdit->append("Heater range: "+data);
    if(data.toShort())
       hoffButton->setEnabled(true);
    else
        hoffButton->setEnabled(false);
    board.writeCommand(dev, "CSET?1");
    data=board.receiveData(dev);
    stateEdit->append("Loop 1 settings: "+data);
    board.writeCommand(dev, "CDISP?1");
    data=board.receiveData(dev);
    stateEdit->append("Heater resistance: "+data.section(',',1,1));
    hSpin->setValue(data.section(',',1,1).toDouble());
    board.writeCommand(dev, "CLIMI?");
    data=board.receiveData(dev);
    double range=data.toDouble();
    range=range*range*hSpin->value();
    rangeList->clear();
    rangeList->addItem(QString("5:%1W").arg(range));
    rangeList->addItem(QString("4:%1W").arg(range/10));
    rangeList->addItem(QString("3:%1mW").arg(range*10));
    rangeList->addItem(QString("2:%1mW").arg(range));
    rangeList->addItem(QString("1:%1mW").arg(range/10));
    pointButton->setEnabled(true);
    heaterButton->setEnabled(true);
    resButton->setEnabled(true);
    rateButton->setEnabled(true);
    rampCheck->setEnabled(true);
    powerCheck->setEnabled(true);
}
void LakeControl::onRamp()
{
    if(instrList->currentText()==NULL)
    {
        stateEdit->setText("No instrument selected!\n");
        return;
    }
    gdevice dev(comboBox->currentText().toInt(),extractAdress(instrList->currentText()),
                extractType(instrList->currentText()));
    board.writeCommand(dev, QString("RAMP 1,,%1").arg(rampSpin->value()));
    mBox->append(QString("%1::Ramp rate is set to %2K/min").arg(dev.getAdress()).arg(rampSpin->value()));
}
void LakeControl::onRampCheck(int state)
{
    gdevice dev(comboBox->currentText().toInt(),extractAdress(instrList->currentText()),
               extractType(instrList->currentText()));
    if(state)
    {
        if(instrList->currentText()==NULL)
        {
            stateEdit->setText("No instrument selected!\n");
            return;
        }
        board.writeCommand(dev, "RAMP 1,1");
        mBox->append(QString("%1::Ramp is ON").arg(dev.getAdress()));
    }
    else
    {
        board.writeCommand(dev, "RAMP 1,0");
        mBox->append(QString("%1::Ramp is OFF").arg(dev.getAdress()));
    }
}
void LakeControl::onEnableCheck(int state)
{
    gdevice dev(comboBox->currentText().toInt(),extractAdress(instrList->currentText()),
               extractType(instrList->currentText()));
    if(state)
    {
        if(instrList->currentText()==NULL)
        {
            stateEdit->setText("No instrument selected!\n");
            return;
        }
        board.writeCommand(dev, "CSET 1,,,1");
        mBox->append(QString("%1::Loop 1 control is enabled").arg(dev.getAdress()));
    }
    else
    {
        board.writeCommand(dev, "CSET 1,,,0");
        mBox->append(QString("%1::Loop 1 control is disabled").arg(dev.getAdress()));
    }
}
void LakeControl::onPowerCheck(int state)
{
    gdevice dev(comboBox->currentText().toInt(),extractAdress(instrList->currentText()),
               extractType(instrList->currentText()));
    if(state)
    {
        if(instrList->currentText()==NULL)
        {
            stateEdit->setText("No instrument selected!\n");
            return;
        }
        board.writeCommand(dev, "CSET 1,,,,1");
        mBox->append(QString("%1::Loop 1 powerup is ON").arg(dev.getAdress()));
    }
    else
    {
        board.writeCommand(dev, "CSET 1,,,,0");
        mBox->append(QString("%1::Loop 1 powerup is OFF").arg(dev.getAdress()));
    }
}
void LakeControl::onScan()
{
    board.setId(comboBox->currentText().toInt());
    devList=board.scanForInstruments();
    for(int i=0;i<devList.count();++i)
    {
        if(devList[i].getType().contains("MODEL340"))
        {
            instrList->addItem(QString("%1").arg(devList[i].getAdress())+": "+devList[i].getType());
        }
    }
}
void LakeControl::onSetpoint()
{
    if(instrList->currentText()==NULL)
    {
        stateEdit->setText("No instrument selected!");
        return;
    }
    gdevice dev(comboBox->currentText().toInt(),extractAdress(instrList->currentText()),
                extractType(instrList->currentText()));
    board.writeCommand(dev, QString("SETP 1,%1").arg(pointSpin->value()));
    mBox->append(QString("%1::Setpoint is set to %2").arg(dev.getAdress()).arg(pointSpin->value()));
}
void LakeControl::onHeaterOff()
{
    if(instrList->currentText()==NULL)
    {
        stateEdit->setText("No instrument selected!\n");
        return;
    }
    gdevice dev(comboBox->currentText().toInt(),extractAdress(instrList->currentText()),
                extractType(instrList->currentText()));
    board.writeCommand(dev, "RANGE 0");
    mBox->append(QString("%1::Heater is OFF").arg(dev.getAdress()));
    hoffButton->setEnabled(false);
}
void LakeControl::onSetRange()
{
    if(instrList->currentText()==NULL)
    {
        stateEdit->setText("No instrument selected!\n");
        return;
    }
    gdevice dev(comboBox->currentText().toInt(),extractAdress(instrList->currentText()),
                extractType(instrList->currentText()));
    board.writeCommand(dev, QString("RANGE %1").arg(5-rangeList->currentIndex()));
    mBox->append(QString("%1::Heater range is set to ").arg(dev.getAdress())+rangeList->currentText());
    onGetState();
}
void LakeControl::onSetResistance()
{
    if(instrList->currentText()==NULL)
    {
        stateEdit->setText("No instrument selected!\n");
        return;
    }
    gdevice dev(comboBox->currentText().toInt(),extractAdress(instrList->currentText()),
                extractType(instrList->currentText()));
    board.writeCommand(dev, QString("CDISP 1,,%1").arg(hSpin->value()));
    mBox->append(QString("%1::Heater resistance is set to %2 Ohm").arg(dev.getAdress()).arg(hSpin->value()));
}
int LakeControl::extractAdress(QString line)
{
    int first=line.indexOf(":");
    return line.left(first).toInt();

}
QString LakeControl::extractType(QString line)
{
    int first=line.indexOf(":");
    return line.right(line.size()-first-1);
}



