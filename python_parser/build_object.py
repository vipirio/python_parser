import json
from abc import ABC, abstractmethod


class BuildObject(ABC):
    """ This is Abstract class of generate object and accept only input_obj as input """
    def __init__(self,input_obj):
        self.input_obj = input_obj
        self.output_obj = None

    @abstractmethod
    def build_object(self):
        pass


class BuildJsonObject(BuildObject):
    """ convert given input_oj into json object, and save into file if write is True """
    def __init__(self, input_obj, write = False, outptut_file_name = None):
        self.write = write
        self.outptut_file_name = outptut_file_name
        super().__init__(input_obj)

    def file_writer(self):
        """ Json data write into json file """
        with open(self.outptut_file_name+'.json', 'w', encoding='utf-8') as f:
            json.dump(self.output_obj, f, ensure_ascii=False, indent=4)
    
    def build_object(self):
        """ Building json object in given format
            {
                "Date":{
                    address/user:{
                        total:no of request,"IPLIST":{
                            IP1:no of request of IP1,"IP2":no of request of IP2
                        }
                    }
                }
            }
        """
        self.output_obj = dict()
        for strng in self.input_obj:
            if strng[2][0] == "[" and strng[2][-1] == "]":
                ip = json.loads(strng[2].replace('.',','))
                ip = '.'.join([str(i) for i in ip])
            else:
                ip = strng[-1]
            if strng[0] in self.output_obj.keys():
                if strng[1] in self.output_obj[strng[0]].keys():
                    self.output_obj[strng[0]][strng[1]]['Total']+=1
                    if ip not in self.output_obj[strng[0]][strng[1]]['IPLIST'].keys():
                        self.output_obj[strng[0]][strng[1]]['IPLIST'][ip]=1
                    else:
                        self.output_obj[strng[0]][strng[1]]['IPLIST'][ip]+=1
                else:
                    self.output_obj[strng[0]][strng[1]] ={"Total":1,"IPLIST":{ip:1}}
            else:
                self.output_obj[strng[0]] = {strng[1]:{"Total":1,"IPLIST":{ip:1}}}

        if self.write:
            self.file_writer()

        return self.output_obj

