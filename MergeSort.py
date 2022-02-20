def sort(list_of_numbers, start, end):
    print(f"List of numbers given: {list_of_numbers}")
    #length = len(list_of_numbers)
    half_index = int(start + (end - start) / 2)
    print(f"start index: {start}")
    print(f"end index: {end}")
    print(f"Half index of the given list: {half_index}")

    if end>start:
        print(f"sort({list_of_numbers},{start},{half_index})")
        sort(list_of_numbers, start, half_index)
        print(f"sort({list_of_numbers},{half_index + 1}, {end})")
        sort(list_of_numbers, half_index+1, end)
        print(f"merge({list_of_numbers},{start},{half_index},{end})")
        merge(list_of_numbers, start, half_index, end)
    else:
        print("end")


def merge(list_of_numbers, first, half_index, end):
    left_list = list_of_numbers[first: half_index+1]
    right_list = list_of_numbers[half_index+1:end+1]

    print(f"MERGE LEFT: {left_list}")
    print(f"MEREG RIGHT: {right_list}")
    i=0
    j=0
    while(i<len(left_list) and j<len(right_list)):
        if left_list[i] < right_list[j]:
            list_of_numbers[first] = left_list[i]
            i=i+1
            first = first+1
            print(f"list_of_numbers after taking left list elements: {list_of_numbers}")
        else:
            list_of_numbers[first] = right_list[j]
            j=j+1
            first=first+1
            print(f"list_of_numbers after taking right list elements: {list_of_numbers}")


    while(i<len(left_list)):
            print(f"attaching remaining left list: {left_list}")
            list_of_numbers[first]=left_list[i]
            i=i+1
            first=first+1

    while(j<len(right_list)):
            print(f"attaching remaining right list: {right_list}")
            list_of_numbers[first]=right_list[j]
            first=first+1
            j=j+1


def mergeSort(list_of_numbers):
    print(f"mergeSort has recevied parameter list: {list_of_numbers}")
    if len(list_of_numbers)>1:
        mid = len(list_of_numbers)//2
        print(f"mid point is {mid}")
        L = list_of_numbers[:mid]
        R = list_of_numbers[mid:]
        mergeSort(L)
        mergeSort(R)
        i=j=k=0
        while (i < len(L) and j < len(R)):
            print(f"comparing between {L} and {R}")
            if L[i] < R[j]:
                list_of_numbers[k] = L[i]
                i+=1
                k+=1
                #print(f"list_of_numbers after taking left list elements: {list_of_numbers}")
            else:
                list_of_numbers[k] = R[j]
                j+=1
                k+= 1
                #print(f"list_of_numbers after taking right list elements: {list_of_numbers}")

        while (i < len(L)):
            #print(f"attaching remaining left list: {L}")
            list_of_numbers[k] = L[i]
            i+=1
            k+=1

        while (j < len(R)):
           # print(f"attaching remaining right list: {R}")
            list_of_numbers[k] = R[j]
            k+=1
            j = j + 1

list_of_numbers = [5,4]
sort(list_of_numbers, 0, len(list_of_numbers)-1)

print(list_of_numbers)

list_of_numbers = [9,8,7,6,2,3,4]
mergeSort(list_of_numbers)
print(list_of_numbers)


