


# def cal(ops):
    
#     if 1< len(ops)<=1000:
#         new_list=[]
#         x=0
#         for i, value in enumerate(ops):
#             # new_list.append(i)
#             if type(value) is int:
#                 new_list.append(value)
#             elif value=='D':
#                 new_list.append(new_list[i-x-2]*2)
#             elif value == 'C':
#                 del new_list[i-1]
#                 x+=1
#             elif value=='+':
#                  new_list.append(new_list[i-x-2]+new_list[i-x-3])
#             else:
#                 print('wrong value')
#     summ = sum(new_list)
#     return summ

# test=[5,2,'C','D','+']
# print(cal(test))

def cal(ops):
    if 1< len(ops)<=1000:
        new_list=[]
        x=0
        pointer = 0
        for value in ops:
            if type(value) is int:
                new_list.append(value)
            elif value=='D':
                new_list.append(new_list[pointer-1]*2)
            elif value == 'C':
                del new_list[pointer-1]
                pointer -= 2
            elif value=='+':
                 new_list.append(new_list[pointer-1]+new_list[pointer-2])
            else:
                print('wrong value')
            pointer += 1
        # for i, value in enumerate(ops):
        #     # new_list.append(i)
        #     if type(value) is int:
        #         new_list.append(value)
        #     elif value=='D':
        #         new_list.append(new_list[i-x-2]*2)
        #     elif value == 'C':
        #         del new_list[i-1]
        #         x+=1
        #     elif value=='+':
        #          new_list.append(new_list[i-x-2]+new_list[i-x-3])
        #     else:
        #         print('wrong value')
    summ = sum(new_list)
    return summ

test=[5,2,'C','D','+']
print(cal(test))
# def reversing(s):
#     lst=[]
#     final_list=[]
#     for l in s:
#         if l.isalpha():
#             lst.append(l)
#     reverselst=lst[::-1]
#     v=0
#     for i in s:
        
#         if i.isalpha():
#             final_list.append(reverselst[v])
#             v+=1
#         else:
#             final_list.append(i)
            
#     return ''.join(final_list)

# yo= ['a','b','-','z']
# print(reversing(yo))