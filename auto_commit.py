import subprocess

print(subprocess)
def calling():

    #Simply opening command prompt in Windows
    subprocess.call("git status",shell=True )
    subprocess.call("git add .",shell=True )
    subprocess.call("git commit -am \"autocommit\"",shell=True )
    subprocess.call("git push",shell=True )

def main():
     calling()

if __name__ == "__main__":
    main()
