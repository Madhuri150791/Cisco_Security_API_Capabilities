
import json
import sys
import csv
import requests
import time

import getpass

server = input("Enter FMC IP: ")
username = input("Enter Username: ")
password = getpass.getpass("Enter Password",stream=sys.stdout)
domain_uuid =""
accesspolicy_uuid =input("Enter Access Policy UUID:")

r = None
headers = {'Content-Type': 'application/json'}
api_auth_path = "/api/fmc_platform/v1/auth/generatetoken"
auth_url = "http://"+server + api_auth_path
try:
    print("Generating Authentication Token...................")
    r = requests.post(auth_url, headers=headers, auth=requests.auth.HTTPBasicAuth(username, password),
                      verify=False)
    auth_headers = r.headers
    auth_token = auth_headers.get('X-auth-access-token', default=None)
    domain_uuid = auth_headers.get('DOMAIN_UUID', default=None)
    if auth_token == None:
        print("auth_token not found. Exiting...")
        sys.exit()
except Exception as err:
    print("Error in generating auth token --> " + str(err))
    sys.exit()

headers['X-auth-access-token'] = auth_token




# POST OPERATION

readfile=open("backup-filterrule.txt","r")#Place the file here which is obtained from the GET operation
rulesnotput=open("Rulesnotput.txt","a")
i=0
length=sum(1 for line in open("accessrule-sf-policy.txt"))
readfile.seek(0)
print("Reading the GET file.............................")
for line in readfile:
        
                    data_json = json.loads(line)
                    if data_json["action"]=="ALLOW":
                        
                        put_data = {"ipsPolicy": {
    "type": "IntrusionPolicy",
    "id": "b4826546-3cfb-11e8-8ca1-da7922d60f71",
    "name": "Inspection_Policy"
  }}
                        data_json.update(put_data)
                    else:
                        pass
                    
                    try:
                        api_path = "/api/fmc_config/v1/domain/" + domain_uuid + "/policy/accesspolicies/" + accesspolicy_uuid + "/accessrules/"  # param
                        print(api_path)
                        url = server + api_path
                        if (url[-1] == '/'):
                            url = url[:-1]
                        #print(json.dumps(data_json,sort_keys=True,indent=4, separators=(',', ': ')))
                        r = requests.post(url, data=json.dumps(data_json), headers=headers, verify=False)
                        status_code = r.status_code
                        resp = r.text
                        if (status_code == 200) or (status_code==201):
                            #print(json.dumps(data_json,sort_keys=True,indent=4, separators=(',', ': ')))
                            json_resp = json.loads(resp)
                            print("POST was successful.........for %s"%(json_resp["name"]))
                            #print(json.dumps(json_resp, sort_keys=True, indent=4, separators=(',', ': ')))
                        else:
                            r.raise_for_status()
                            print("Status code:-->" + status_code+" for name "+str(data_json["name"]))
                            print("Error occurred in PUT --> " + resp)
                            rulesnotput.write(data_json["name"])
                    except requests.exceptions.HTTPError as err:
                        print("Error in connection --> " + str(err))
                        rulesnotput.write(data_json["name"])
                        if status_code==401:# This mean the access token is expired
                                        headers = {'Content-Type': 'application/json'}
                                        api_auth_path = "/api/fmc_platform/v1/auth/generatetoken"
                                        auth_url = server + api_auth_path
                                        try:
                                            r = requests.post(auth_url, headers=headers, auth=requests.auth.HTTPBasicAuth(username, password),
                                                              verify=False)
                                            auth_headers = r.headers
                                            auth_token = auth_headers.get('X-auth-access-token', default=None)
                                            if auth_token == None:
                                                print("auth_token not found. Exiting...")
                                                sys.exit()
                                        except Exception as err:
                                            print("Error in generating auth token --> " + str(err))
                                        headers['X-auth-access-token'] = auth_token
                                        ###########POST the respective access rule
                                        api_path = "/api/fmc_config/v1/domain/" + domain_uuid + "/policy/accesspolicies/" + accesspolicy_uuid + "/accessrules/"  # param
                                        print(api_path)
                                        url = server + api_path
                                        if (url[-1] == '/'):
                                            url = url[:-1]
                                        print(json.dumps(data_json,sort_keys=True,indent=4, separators=(',', ': ')))
                                        r = requests.post(url, data=json.dumps(data_json), headers=headers, verify=False)
                                        status_code = r.status_code
                                        resp = r.text
                                        if (status_code == 200) or (status_code==201):
                                            #print(json.dumps(data_json,sort_keys=True,indent=4, separators=(',', ': ')))
                                            json_resp = json.loads(resp)
                                            print("POST was successful.........for %s"%(json_resp["name"]))
                                            #print(json.dumps(json_resp, sort_keys=True, indent=4, separators=(',', ': ')))
                                        else:
                                            r.raise_for_status()
                                            print("Status code:-->" + status_code+" for name "+data_json["name"])
                                            print("Error occurred in PUT --> " + resp)
                                            rulesnotput.write(data_json["name"])
                        if status_code==429:
                            time.sleep(5)
                        if status_code==400:
                            rulesnotput.write(data_json["name"])
                            print("Changing the name of the rule")
                            print("Status code:-->" + str(status_code)+" for name "+str(data_json["name"]))
                            name=data_json["name"]+"_FTDmig"
                            if len(name)>30:
                                name=name.split("CSM_FW_ACL_")[1].strip()
                            del data_json["name"]
                            data_json.update({"name":name})
                            api_path = "/api/fmc_config/v1/domain/" + domain_uuid + "/policy/accesspolicies/" + accesspolicy_uuid + "/accessrules/"  # param
                            print(api_path)
                            url = server + api_path
                            if (url[-1] == '/'):
                                url = url[:-1]
                            print(json.dumps(data_json,sort_keys=True,indent=4, separators=(',', ': ')))
                            r = requests.post(url, data=json.dumps(data_json), headers=headers, verify=False)
                            status_code = r.status_code
                            resp = r.text
                            if (status_code == 200) or (status_code==201):
                                #print(json.dumps(data_json,sort_keys=True,indent=4, separators=(',', ': ')))
                                json_resp = json.loads(resp)
                                print("POST was successful.........for %s"%(json_resp["name"]))
                                #print(json.dumps(json_resp, sort_keys=True, indent=4, separators=(',', ': ')))
                            else:
                                r.raise_for_status()
                                print("Status code:-->" + status_code+" for name "+data_json["name"])
                                print("Error occurred in PUT --> " + resp)
                                rulesnotput.write(data_json["name"])
                            
                    finally:
                        if r: r.close()

                
               
