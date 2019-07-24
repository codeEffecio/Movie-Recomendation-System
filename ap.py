a=[]
i=0
while(i<2):
    lst=str(input("enter 2 films-"))
    a.append(lst)
    i+=1
    
    
import requests
import json
movie1=a[0]
movie2=a[1]

base_url = f"https://tastedive.com/api/similar?q="

url1=base_url+movie1
url2=base_url+movie2

response = requests.get(url1)
response2=requests.get(url2)
result = response.json()
result2=response2.json()
#print(result)
#print(result2)
y=[]
x=[]
i=0
while i<10:
    
    output=result['Similar']['Results'][i]['Name']
    output2=result2['Similar']['Results'][i]['Name']
    i+=1
    x.append(output)
    y.append(output2)
#print(x)
#print(y)
z=x+y
s1=set(z)
zU=list(s1)
dict={}
y={}
for i in range(0,len(zU)):
            
    
    base_url2="http://www.omdbapi.com/?t="+zU[i]+"&apikey=12f27bc4"
    response3=requests.get(base_url2)
    result3= response3.json()
    
    rating=result3['Ratings'][0]['Value']
    title=result3['Title']
    rt=rating.partition("/")
    a=float(rt[0])
    b=float(rt[2])
    rating=(a/b)*b
    rating=round(rating,3)
    
    dict={title:rating}
    y.update(dict)

z=[]
tup=sorted(y.items(),key=lambda x:x[1],reverse=1)
for e in tup:
    z.append([e[0],":",e[1]])
print("Top 3 movies based on ratings-")
for i in range(0,3):
    print(z[i])
    i+=1
