input_file=open('D:\\Program Files x86\\ProectsVS\\spirt\\input.txt', 'r')
line=input_file.readline().split()
print(line)
for i in range(len(line)):
    try:
        line[i]=int(line[i])
    except ValueError:
        print(line[i], 'Invalid data type, please input are number')
        line[i]=0
a=(line[0])
b=(line[1])
c=(line[2])
molecules=[a//2, b//6, c//1]
if a//2<1:
    print('There is not enough C, alcohol will not work')
elif b//6<1:
    print('There is not enough H, alcohol will not work')
elif c//1<1:
    print('There is not enough O, alcohol will not work')
else:
    print(molecules)
spirt=min(molecules)
print(spirt)
input_file.close
output_file=open('D:\\Program Files x86\\ProectsVS\\spirt\\output.txt', 'w')
output_file.write('The resulting amount of alcohol: '+ str(spirt))