import json
import sys
import csv
import requests

readfile=open("accessrule-sf-policy.txt","r")#Place the file here which is obtained from the GET operation
writefile=open("filterrule-test.txt","w")
for line in readfile:
    data=json.loads(line)
    if "users" in data:
        pass
    else:
        
        if "metadata" in data:
            del data["metadata"]
            #print (data)
            if "links" in data:
                    del data["links"]
                    #print(data)
                    #print("\n")
                    del data["id"]
                    if "commentHistoryList" in data:
                        comment=data["commentHistoryList"][0]["comment"]
                        if "The migrated rule is disabled because:" in comment:
                            pass
                        else:
                            putdata={"newComments":[comment]}
                            del data["commentHistoryList"]
                            data.update(putdata)
                        #print(comment)
                    if "~" in data["name"]:
                        name=data["name"].replace("~","")
                        del data["name"]
                        putdata=""
                        putdata={"name":name}
                        data.update(putdata)
                    writefile.write(str(data))
                    writefile.write("\n")
        
    
    #print(data)
                    
writefile.close()
