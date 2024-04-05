# I declare that my work contains no examples od misconduct, such as plagiarism or collusion
# Any code taken from otehr sources id referenced within my code solution.
# Student iD: 20221445
# Date: 07-12-2022

count=0                           #number of outcomes
count_1=0                         #number of progresses
count_2=0                         #number of module trailers
count_3=0                         #number of mudule retrievers
count_4=0                         #number of excludes
list1=[[],[],[],[]]               
dict1={}                          #dictionary for progresses
dict2={}                          #dictionary for module trailers
dict3={}                          #dictionary for module retrievers
dict4={}                          #dictionary for excludes
user_inp='y'


def dictionary(dict_name):
    for k in dict_name.keys():
        print(f'{k} : {dict_name[k]}')                #displaying from dictionary 
    
def file_read(file_name):
    try:
        file1=open(file_name,'r')
        read1=file1.read()
        print(read1,end="")                           #displaying from files
        file1.close()
        file1=open(file_name,'w')                     #erasing file content
        file1.write()
        file1.close()
    except:
        return

def file_write(file_name,outcome):
        file1=open(file_name,'a')
        file1.write(f'{outcome} : {p},{d},{f}\n')     #file writing
        file1.close()
            

def listing2(num_count,outcome,listindex):
    for d in range(num_count):
        print(f'{outcome} : ',end="")                 #displaying from lists
        for s in range(3):
            if s==2:
                print(list1[listindex][0])
            else:
                print(list1[listindex][0],end=",")
            list1[listindex].pop(0)


while user_inp=='y':
    total=0
    st_id=input('Enter the student id : ')
    while total!=120:
        for x in ('Pass','defer','fail'):
            try:
                marks=int(input(f'Please enter your credits at {x}: '))
                if marks not in range(0,121,20):
                    print('Out of range.\n')
                    break
                if x=='Pass':
                    p=marks
                elif x=='defer':
                    d=marks
                else:
                    f=marks
        
            except:
                print('Integer Required\n')
                break
            if x=='fail':
                total=p+d+f
                if  total!=120:
                    print('Total incorrect.\n')
                
            
    if p==120:
        print('Progress\n')
        list1[0].extend((p,d,f))
        file_write('progress_file.txt','Progress')
        dict1[st_id]=f'Progress - {p},{d},{f}'
        count_1=count_1+1


        
    elif p==100:
        print('Progress (module trailer)\n')
        list1[1].extend((p,d,f))
        file_write('trailer_file.txt','Progress (module trailer)')
        dict2[st_id]=f'Progress (module trailer) - {p},{d},{f}'
        count_2=count_2+1


        
    elif p+d<=40:
        print('Exclude\n')
        list1[3].extend((p,d,f))
        file_write('exclude_file.txt','Exclude')
        dict4[st_id]=f'Exclude - {p},{d},{f}'
        count_4=count_4+1


    else:
        print('Do not progress (module retriever)\n')
        list1[2].extend((p,d,f))
        file_write('retriever_file.txt','Do not progress (module retriever)')
        dict3[st_id]=f'Do not progress (module retriever) - {p},{d},{f}'
        count_3=count_3+1


    count=count+1

    user_inp=input('Would you like to enter another set of data?\nEnter \'y\' for yes or \'q\' to quit and view results: ')
    print()

if user_inp=='q':
    print(' - '*40,'\n')
    print('Histogram')
    print('Prgress  ',count_1,':','*'*count_1)
    print('Trailer  ',count_2,':','*'*count_2)
    print('Retriever',count_3,':','*'*count_3)
    print('Exclude  ',count_4,':','*'*count_4,end="\n\n")
    print(f'{count} outcomes total.')
    print('\n',' - '*40)
    
    listing2(count_1,'Progress',0)
    listing2(count_2,'Progress (module trailer)',1)
    listing2(count_3,'Do not progress (module retriever)',2)
    listing2(count_4,'Exclude',3)
    print()

    file_read('progress_file.txt')
    file_read('trailer_file.txt')
    file_read('retriever_file.txt')
    file_read('exclude_file.txt')
    print()

    dictionary(dict1)
    dictionary(dict2)
    dictionary(dict3)
    dictionary(dict4)

    



