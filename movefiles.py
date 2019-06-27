import os #for system 
import pandas as pd #for data from massouad
def funcwrite(name,type,path):
    # write 2 file 1 for path of all file of extention type
    name1=name+".Hossam" #txt file with path of all files
    #.hossam file for not enter with search because no extantion called Hossam
    name2=name+"1.Hossam"#txt file with name of all files
    files = [] #list of all files
    names=[] #list of all names
    re='txt' #to don't get eror with r
    pathfile=open(name1,'w')#open path1  to write it
    namefile=open(name2,'w')#open path2 to write it
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:#search for all files
            for i in type:#search for type
                if i in file:#search in file type
                    if '.Hossam' in file :continue
                    else:
                        files.append(os.path.join(r, file))
                        names.append(os.path.join(r,name, file))
            print(d)
        re=str(r);
    for f in files:#write on file
        f=str(f)
        pathfile.write(f)
        pathfile.write('\n')
    pathfile.close()
    for f in names:#write on file
        f=str(f)
        namefile.write(f)
        namefile.write('\n')
    namefile.close()
    return re

def makefolderfun(name,type,path):
    name1=name+".Hossam" #txt file with path of all files
    name2=name+"1.Hossam"#txt file with name of all files
    pf=open(name1,'r')#open path1  to read it
    nf=open(name2,'r')#open path2 to read it
    os.chdir(path)
    p=[]#path
    n=[]#newname
    h=[1,2,3]#namefile
    for x in pf:
        x=x.rstrip('\n')
        p.append(x)
    for x in nf:
        x=x.rstrip('\n')
        n.append(x)
    if (os.path.isdir(os.path.join(os.getcwd(),name))):
        pass
    else:
        os.makedirs(name)
    pf.close()
    nf.close()
    for i in range(len(n)):
        os.rename(p[i],n[i])

        
search_path =input("Enter path : ")
#video=[".mp4",".flv",".mkv"]
# r=root, d=directories, f = files
fileExtansions = pd.read_csv('FileExtansionsDataSet.csv')
fileFormats = {fileExtansions[column].name: [y for y in fileExtansions[column] if not pd.isna(y)] for column in fileExtansions}
#dict comprehension (dict of lists) for dataframe with drop for each nan value.
#fileFormatsReversed = {file_format: folder for folder, fileFormat in fileFormats.items()  for file_format in fileFormat}
#reversing key and value in list for future uses
key=list(fileFormats.keys())
value=list(fileFormats.values())
for i in range(len(key)):
    r=str(funcwrite(key[i],value[i],search_path))
    makefolderfun(key[i],value[i],r)
