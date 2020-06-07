import os

def changeDir(folder_name):
    os.chdir("/content/{}".format(folder_name))

def changePer(folder_name):
    os.system("chmod 777 runcolab.sh")
    os.system("chmod 777 train.sh")

def makerunFile(folder_name):
    runcolabfile = "/content/{}/runcolab.sh".format(folder_name)
    with open(runcolabfile, 'w') as runfile:
        runfile.write("pip install -r requirements.txt\n".format(folder_name))
        runfile.write("sh ./train.sh")

def setupColab(githubLink):
    # os.system("git clone {}".format(githubLink))

    folder_name = githubLink.split("/")[-1].split('.')[0]
    makerunFile(folder_name)
    changeDir(folder_name)
    changePer(folder_name)
