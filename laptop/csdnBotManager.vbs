set obj=createobject("wscript.shell")
obj.CurrentDirectory = "E:\python file\CSDN_BOT\laptop\"
do
    obj.run "csdnBot.pyw"
    wscript.sleep 800000
loop