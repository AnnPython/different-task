
f = open('access-log', 'r', encoding='utf-8')
count_vub=sum(int(i.split()[-1]) for i in f if i.split()[-2]=='404' and i.split()[-1]!='-')

f = open('access-log', 'r', encoding='utf-8')
count_str=sum(1 for i in f if i.split()[-2]=='404')

f = open('access-log', 'r', encoding='utf-8')
count_vub1=sum(int(i.split()[-1]) for i in f if i.split()[-2]=='200' and i.split()[-1]!='-' )

f = open('access-log', 'r', encoding='utf-8')
count_str1=sum(1 for i in f if i.split()[-2]=='200')

f = open('access-log', 'r', encoding='utf-8')
average_404=count_vub/count_str
print(round(average_404,2))
average_200=count_vub1/count_str1
print(round(average_200,2))
