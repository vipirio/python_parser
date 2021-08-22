from datetime import datetime

# Internal Import
import config
from python_parser.pyparser import PyParser
from python_parser.build_object import BuildJsonObject


class LogParser(PyParser):
    """ LogParser class to parse log file's data, 
        And it accpet four params
        file_path = String
        delimeter = String (Based on delimeter to differentiate what kind of data to parse from file)
        Date = String this is optional parameter (Parse the data for perticular date)
        obj_type = This is type of output object (convert output object  based on obj_type)
    """
    def __init__(self, file_path, delimeter_list, date = None, obj_type = 'json', write = True):
        self.delimeters = delimeter_list
        self.date = date
        self.obj_type = obj_type
        self.parsed_data = None
        self.write = write
        super().__init__(file_path)
    
    def __set_file_name__(self,delimeter):
        self.file_name = '_'.join(delimeter.split(' '))

    def filter_string_line(self, delimeter):
        """ get only those line which have given delimeter """
        self.data = [line for line in self.file_data if delimeter in line]
        
    def change_date_format(self,format):
        """ To change the format of log's timestamp """
        if not self.data:
            raise ValueError("Expected delimeter not found in log file")
        self.data = [line.replace(line[:6],datetime.strptime(line[:6],'%b %d').strftime(format)) for line in self.data]

    def reverse_mapping_delimeter(self):
        """ store only Date, address and IP there is no year in log's timestamp so that i'm putting current year(2021) """
        __parse_d__ = list()
        for str_list in self.data:
            line_d = ['2021-'+str_list[0]]
            for strng in str_list:
                if '.' in strng:
                    line_d.append(strng)
            __parse_d__.append(line_d)
        return __parse_d__

    def failed_password_delimeter(self):
        """ store only date, user and IP and there is no year in log's timestamp so that i'm putting current year(2021) """
        __parse_d__ = list()
        for str_list in self.data:
            __parse_d__.append(['2021-'+str_list[0],str_list[-6],str_list[-4]])
        return __parse_d__

    def get_fine_tuned_data(self, delimeter):
        """ Get only required string based on delimeter """
        self.data = [line_str.split(' ') for line_str in self.data]
        if delimeter == "Failed password":
            self.data = self.failed_password_delimeter()
        else:
            self.data = self.reverse_mapping_delimeter()

    def get_resultant_object(self):
        """ Convert parser object based on given oject_type """
        if self.obj_type == 'json':
            build_obj = BuildJsonObject(self.data, write=self.write, outptut_file_name = self.file_name)
            parsed_data = build_obj.build_object()
        else:
            raise ValueError("Not supported this type of object")
        return  parsed_data

    def parse_log(self):
        """ Based on given input to generate parser object"""

        self.parsed_data = dict()
        for delimeter in self.delimeters:
            self.filter_string_line(delimeter)
            self.change_date_format(config.format)
            self.get_fine_tuned_data(delimeter)
            self.__set_file_name__(delimeter)

            if not self.data:
                raise ValueError("expecting address, ip, user and date")

            # if date then get only those data which have same date
            if self.date:
                self.data = [log_d for log_d in self.data if self.date == log_d[0]]
            
            self.parsed_data[delimeter] = self.get_resultant_object()
        return self.parsed_data



        