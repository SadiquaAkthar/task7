import time
# function creating a text file and write-timestamp.
def file_stamp():
    f=open("demo.txt","w")
    #writing the timestamp and converting it to str type
    f.write(str(time.time()))
    #open and read the file after the appending:
    f = open("demo.txt", "r")
    print(f.read())
    f.close()


file_stamp()
