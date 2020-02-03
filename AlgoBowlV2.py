def readfile(filename):
    with open(filename) as f:
        size = next(f)
        array = []
        for line in f:
            array += [int(x) for x in line.split()]
        return array

def figureitout(array):
    count = 0
    f = open("output_group83.txt","w")
    f.write("")
    numsused = [1]
    for num in array:
        #print(num,"!!!")
        num_found = False
        temp_num = 0
        while numsused[-1]*2<num:
            #print('Doubling: ', numsused[-1],"*2 =",numsused[-1]*2)
            f.write('{0} {0}\n'.format(numsused[-1]))
            numsused.append(numsused[-1]*2)
            count += 1
        last_num2=0
        while not num_found:
            last_num=0
            temp_num = numsused[-1]
            for num_u in numsused:
                if numsused[-1]+num_u+last_num2 == num:
                    num_found=True
                    last_num = num_u
                    break
                if numsused[-1]+num_u+last_num2>num:
                    break
                last_num=num_u
            if last_num2==0:
                last_num2=last_num
            else:
                #print(last_num,'+', last_num2, '=', last_num+last_num2)
                f.write('{0} {1}\n'.format(last_num,last_num2))
                count += 1
                last_num += last_num2
                numsused.append(last_num)
                last_num2=0
                numsused.sort()
            if num_found:
                #print("Woohoo!!!   ", last_num, "+", temp_num)
                f.write('{0} {1}\n'.format(last_num,temp_num))
                count += 1
                numsused.append(temp_num + last_num)            
    print(numsused)
    print(count)
    f.close()
    f_r = open("output_group83.txt","r")
    oline = f_r.readlines()
    oline.insert(0,str(count)+'\n')
    f_r.close()

    f_w = open("output_group83.txt","w")
    f_w.writelines(oline)
    f_w.close()


array = readfile('inputs/input_group83.txt')
figureitout(array)

