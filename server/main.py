
import glob
import shutil
import os
import zipfile
import time
 
source_path='..\source\*'
destination='..\destination'
postfix=[1,2,3]
 
cnt=0
while True:
    source_object=glob.glob(source_path)
   
    if len(source_object)>0 and cnt<len(source_object):
        for i in range(len(source_object)):
            object_path=source_object[i]
            object_name=object_path.split('\\')[-1]
            file_name=object_name.split('.')[0]
            try:
                extention=object_name.split('.')[1]
            except IndexError:
                print(os.error)
                print("end operation")
                os.remove(object_path)
                cnt+=1
                continue
 
   
            if extention=='txt':
                time.sleep(2)
                print("Copying file",end='')
                for i in range(3):
                    time.sleep(1)
                    print('.',end='')
                print()
           
 
                with open(object_path,'r')as file_s:
                    all_read_lines=[]
                    lines=file_s.readlines()
                    for line in lines:
                        all_read_lines.append(line)
                file_s.close()
                file_for_zip=[]
                for item in postfix:
                    i=0
                    len_file=item*10
                    new_file_name=file_name+'_'+str(item)+'.'+extention
                    with open(new_file_name,'a') as file_d:
                        for line in all_read_lines:
                            if i==len_file: break
                            if i==len_file-1:
                                file_d.write(line.strip('\n'))
                                i+=1
                                continue
                            file_d.write(line)
                            i+=1
                    file_d.close()
                    path=glob.glob(new_file_name)
                    if len(path)>0:
                        obj=path[0]
                        file_for_zip.append(new_file_name)
                        # os.remove(obj)
                time.sleep(2)
                print("File ziping",end='')
                for i in range(3):
                    time.sleep(1)
                    print('-',end="")
                print()
                #create zip file
                zip_file_name=f'{file_name}.zip'
                zip_path='./'+zip_file_name
                # print(zip_file_name,zip_path)
 
                #write zip file
                with zipfile.ZipFile(zip_file_name,'w') as zip_file:
                    for file in file_for_zip:
                        zip_file.write(file)
                        os.remove(file)
                    zip_file.close()
                print("Copying zip file to the destination file",end='')
                # time.sleep(1)
                for i in range(3):
                    # time.sleep(1)
                    print('-',end="")    
                print()
                # copy to destination
 
                # time.sleep(2)
                shutil.copy(zip_path,f'{destination}/{zip_file_name}')
   
                #unzip file
                print("Extract zip file",end='')
                for i in range(3):
                    print('.',end="")
                print()
                with zipfile.ZipFile(f'{destination}/{zip_file_name}')as z:
                    z.extractall(destination)
                # time.sleep(2)
                os.remove(f'{destination}/{zip_file_name}')
   
                #remove the server zip file
                # time.sleep(2)
                os.remove(zip_path)
   
            elif extention=='py':
                print("Python file exicuting",end='')
                for i in range(3):
                    print('.',end="")  
                print('\n')
                try:
                    time.sleep(1)
                    os.system(f'python {object_path}')
                except os.error:
                    print(os.error)
            #remove the source file
            time.sleep(2)
            # os.remove(object_path)
            print("\nEnd operation\n")
            cnt+=1
            time.sleep(1)


