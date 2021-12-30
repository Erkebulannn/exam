try:
    file=open('matrix.txt')
except:
    print('File cannot be opened')   
    exit()

ff=open('sum_row_1.txt')
lines=ff.readlines()

for line in lines:    
     print(line)

file.close()
ff.close()
