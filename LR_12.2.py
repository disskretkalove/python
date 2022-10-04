fin=open("marks.txt",'r')
fname=input("Введите название файла:")
fout=open(fname,'w')
data = []
data = [str(i) for i in fin.read().split()]
for i in range(len(data)):
    if data[i].isdigit():
        if int(data[i]) == 2:
            fout.write("fall\n")
        elif int(data[i]) == 3:
            fout.write("bad\n")
        elif int(data[i]) == 4:
            fout.write("good\n")
        elif int(data[i]) == 5:
            fout.write("nice\n")
    elif str(data[i]) == "fall":
        fout.write(str(2)+"\n")
    elif str(data[i])=="bad":
        fout.write(str(3)+"\n")
    elif str(data[i])=="good":
        fout.write(str(4)+"\n")
    elif str(data[i]) == "nice":
        fout.write(str(5)+"\n")
    else: fout.write("Not mark")
line = fin.readline()
fout.close()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
