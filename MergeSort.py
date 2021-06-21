def merge(a,b):
    merged_list=[]
    len_a,len_b=len(a),len(b)
    index_a,index_b=0,0
    while index_a < len_a and index_b <len_b:
        if a[index_a] < b[index_b]:
            merged_list.append(a[index_a])
            index_a+=1
        else:
            merged_list.append(b[index_b])
            index_b+=1

    if index_a<len_a:
        merged_list.extend(a[index_a:])
    elif index_b<len_b:
        merged_list.extend(b[index_b:])
    return merged_list

def merge_sort(lst):
    if len(lst)<=1:
        return lst
    mid=len(lst)//2
    left=merge_sort(lst[:mid])
    right=merge_sort(lst[mid:])
    return merge(left,right)
  
  
  print(merge_sort([1,28,4,65,14,16,47,64]))
