def readfile(filename):
    with open(filename) as f:
        size = next(f)
        array = []
        for line in f:
            array += [int(x) for x in line.split()]
        return array

def figureitout(array):
    numsused = [1]
    for num in array:
        #print(num,"!!!")
        num_found = False
        temp_num = 0
        while numsused[-1]*2<num:
            #print('Doubling: ', numsused[-1],"*2 =",numsused[-1]*2)
            numsused.append(numsused[-1]*2)
        while not num_found:
            last_num=0
            for num_u in numsused:
                if numsused[-1]+num_u == num:
                    #print("Woohoo!!!   ",num_u, "+", numsused[-1],"=",num)
                    num_found=True
                    numsused.append(num_u+numsused[-1])
                    break
                if numsused[-1]+num_u>num:
                    break
                last_num=num_u
            if num_found:
                break
            #print(last_num,"+", numsused[-1], '=', last_num+numsused[-1])
            numsused.append(last_num+numsused[-1])
    print(numsused)
    print(len(numsused))
            
        
        
            
            



array = readfile('inputs/input_group56.txt')
figureitout(array)

