def calculate_frequency(a):
    b=list(a)
    var_dict={}
    count=0
    for i in b:
        for j in b:
            if j==i:
                count=count+1
        var_dict[i]=count
        count=0
    print(var_dict)
sent=input("enter a sentence")
calculate_frequency(sent)
