def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        subseq = string[i:i+k]
        sub_set = set(subseq)
        dis_seq = []
        for c in subseq:
            if c in sub_set:
                dis_seq.append(c)
                sub_set.remove(c)
        print(''.join(dis_seq))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)