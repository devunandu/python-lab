def find_all_occurrence(main_string,sub_string):
    indices=[]
    index=main_string.find(sub_string)
    while index!=-1:
        indices.append(index)
        index=main_string.find(sub_string,index+1)
    return indices if indices else -1
main_str=input("enter the main string: ")
sub_str=input("enter the sub string: ")
result=find_all_occurrence(main_str,sub_str)
print("indices: ",result)
