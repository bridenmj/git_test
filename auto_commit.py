import subprocess

print(subprocess)
def git_pull():
    #Simply opening command prompt in Windows
    subprocess.call("git status",shell=True )
    subprocess.call("git pull",shell=True )

def git_push():

    #Simply opening command prompt in Windows
    subprocess.call("git status",shell=True )
    subprocess.call("git add .",shell=True )
    subprocess.call("git commit -am \"autocommit\"",shell=True )
    subprocess.call("git push",shell=True )

def main():
     git_pull()
     git_push()

if __name__ == "__main__":
    main()
