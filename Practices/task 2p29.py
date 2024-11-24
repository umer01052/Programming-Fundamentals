x="life, living matter and, as such, matter that shows certain attributes that \
include responsiveness, growth, metabolism, energy transformation, and reproduction. \
Although a noun, as with other defined entities, the word life might be better cast as \
a verb to reflect its essential status as a process. Life comprises individuals, living \
beings, assignable to groups (taxa). Each individual is composed of one or more minimal \
living units, called cells, and is capable of transformation of carbon-based and other \
compounds (metabolism), growth, and participation in reproductive acts. Life forms \
present on Earth today have evolved from ancient common ancestors through the generation \
of hereditary variation and natural selection. The several branches of science \
that reveal the common historical, functional, and chemical basis of the evolution of all \
life include electron microscopy, genetics, paleo biology (including paleontology), and \
molecular biology."

cout_word=0
arr=[]
for i in range (len(x)):
    
    if x[i]==' ' or x[i]=='.' or x[i]=='(' or x[i]==')'or x[i]==',':
        arr.append(cout_word)

        cout_word=0
    else:
        cout_word+=1

     
for i in range (len(arr)):
    for j in range (len(arr)-1):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]


print('Maximum length of word :',arr[0])
