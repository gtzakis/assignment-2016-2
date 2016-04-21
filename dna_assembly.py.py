import random
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("onomarxeiou", help="name of file",default='.txt')
parser.add_argument("megethos", help="arithmos",
                    type=int, default=3)
args = parser.parse_args()
megethos = args.megethos
onomarxeiou = args.onomarxeiou

e=[]
dic={}


with open(onomarxeiou) as arxeio:

    for line in arxeio:
        parts=line.split()
        if parts not in e:
            e.append(parts)


    for parts in e:
        key = parts[0][0:2]
        value = parts[0][1:3]


        if key in dic:

            dic[key].append(value)
        else:
            dic[key] = [key]
            dic[key].append(value)

    for i in dic:
        key=i
        for j in dic[key]:
            value=j
            if key==value:
                dic[key].remove(value)




print (dic)

key_list=list(dic.keys())


rkey=(random.choice(key_list))


fkey=rkey

rvalue=dic[rkey][0]
#print (rvalue)


used_values=[]
used_values.append(fkey)

k=0
while (rvalue!=fkey) & (k<len(dic)):

   for i in dic:
       kleidi=i
       if rkey==kleidi:
           if len(dic[rkey])>1:
               flag=False
               for y in dic[rkey]:
                   if flag==False:
                       timirkey=y
                       if timirkey not in used_values:
                           used_values.append(timirkey)
                           dic[rkey].remove(timirkey)
                           rkey=timirkey
                           flag=True
               if flag==False:
                   timirkey=dic[rkey][1]
                   used_values.append(timirkey)
                   rkey=timirkey



           if len(dic[rkey])==1:
               timirkey=dic[rkey][0]
               used_values.append(timirkey)
               dic[rkey].remove(timirkey)
               rkey=timirkey


           print (used_values)
   k=k+1
#if fkey not in used_values:
# used_values.append(fkey)
n=len(used_values)


k=[]
for i in used_values:
    value=i
    k.append(value[1])

print(k)
k1=''.join(k)
print(k1)
