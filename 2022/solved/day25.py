import sys

def read_fuel_requirements(filename):
    with open(filename,'r') as fh:
        fuel_requirements = [line.rstrip('\n') for line in fh]

    return fuel_requirements

def SNAFUtoDecimal(snafuStr):
    snafuDecStr = [char for char in snafuStr]
    resolve_minus = [char if char!='-' else '-1' for char in snafuDecStr]
    resolve_doubleminus = [char if char!='=' else '-2' for char in resolve_minus]
    snafuDec = [int(char) for char in resolve_doubleminus[::-1]]
    decimal = sum([dec*(5**pow) for pow,dec in enumerate(snafuDec)])
    # print(f"{snafuStr}  {decimal}")

    return decimal

def DecimalToSNAFU(dec):
    """
>>> t=28927640190471
>>> tmf19=28927640190471-5**19
>>> tmf19
9854153862346
>>> tmf19//5**10
1009065
>>> tmf19//5**15
322
>>> tmf19//5**16
64
>>> tmf19//5**17
12
>>> tmf19//5**18
2
>>> tmf19-5**18
6039456596721
>>> f19mf18=tmf19-5**18 
>>> f19mf18//5**17     
7
>>> t-(2*5**19)
-9219332465779
>>> f18=t-(2*5**19)     
>>> f18
-9219332465779
>>> f18//5**18
-3
>>> 2*(5**18)
7629394531250
>>> f17=f18+2*(5**18) 
>>> f17
-1589937934529
>>> f17//5**17
-3
>>> f16=f17+2*(5**17)
>>> f16
-64059028279
>>> f16//5**16 
-1
>>> f15=f16+(5**16)
>>> f15
88528862346
>>> f15//5**15
2
>>> f14=f15-2*(5**15)
>>> f14
27493706096
>>> f14//5**14
4
>>> f15=f16
>>> f15
-64059028279
>>> f15//5**15
-3
>>> f14=f15+2*(5**15)
>>> f14
-3023872029
>>> f14//5**14
-1
>>> f13=f14+5**14
>>> f13
3079643596
>>> f13//5**13
2
>>> f12=f13-2*(5**13)
>>> f12
638237346
>>> f12//5**12
2
>>> f11=f12-2*(5**12)
>>> f11
149956096
>>> f11//5**11
3
>>> f13=f14
>>> f13//5**13        
-3
>>> f13        
-3023872029
>>> f12=f13+2*(5**13) 
>>> f12
-582465779
>>> f12//5**12
-3
>>> f11=f12+2*(5**12) 
>>> f11
-94184529
>>> f11//5**11
-2
>>> f10=f11+2*5**11 
>>> f10
3471721
>>> f10//5**10
0
>>> f9=10     
>>> f9//5**9
0
>>> f8=f9
>>> f8//5**8
0
>>> f8
10
>>> f9=f10   
>>> f9
3471721
>>> f9//5**9 
1
>>> f8=f9-5**9
>>> f8
1518596
>>> f8//5**8
3
>>> f8=f9-2*5**9 
>>> f8
-434529
>>> f8//5**8
-2
>>> f7=f8+2*5**8
>>> f7
346721
>>> f7//5**7
4
>>> f8=f9-5**9   
>>> f8//5**8
3
>>> f8
1518596
>>> f8=f9-2*5**9 
>>> f7=f8+5**8   
>>> f7//5**7
-1
>>> f6=f7+5**7
>>> f6//5**6
2
>>> f5=f6-2*5**6
>>> f5
2971
>>> f5//5**5
0
>>> f4=f5
>>> f4//5**4
4
>>> f4=f5-5**5
>>> f4
-154
>>> f4//5**4
-1
>>> f3=f4+5**4
>>> f3
471
>>> f3//5**3
3
>>> f3=f4   
>>> f3//5**3
-2
>>> f2=f3+2*5**3
>>> f2
96
>>> f2//5**2
3
>>> f2=f3+5**3   
>>> f2
-29
>>> f2//5**2
-2
>>> f1=f2+2*5**2
>>> f1
21
>>> f1//5**1
4
>>> f1=f2+5**2   
>>> f1
-4
>>> f1//5**1
-1
>>> f0=f1+5**1
>>> f0
1
>>>
    """
    pass

if __name__ == "__main__":
    file = sys.argv[1]

    fuel_reqs = read_fuel_requirements(file)

    fuel_reqs_decimal = []
    for req in fuel_reqs:
        dec = SNAFUtoDecimal(req)
        fuel_reqs_decimal.append(dec)
    
    total_fuel_req_dec = sum(fuel_reqs_decimal)

    print(f"The total fuel requirments is {total_fuel_req_dec}")
    part1_ans = total_fuel_req_dec

    if len(sys.argv) >= 3:
        if int(sys.argv[2]) == part1_ans:
            print(f"Answer for part 1 is correct!")
    if len(sys.argv) == 4:
        if int(sys.argv[3]) == part2_ans:
            print(f"Answer for part 2 is correct!")

