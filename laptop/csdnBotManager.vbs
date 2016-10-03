set obj=createobject("wscript.shell")
obj.CurrentDirectory = "E:\python file\CSDN_BOT\laptop\"
do
    obj.run "csdnBot.py"
    wscript.sleep 800000
loop