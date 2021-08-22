Python Log Parser
===============================

## There are only 2 delimeter so that log file parse based on two delimeter.

* Failed password
* reverse mapping

## There is no dependencies that's why requirements.txt is blank

## How to run the script

* python main.py --file path/to/log_file --date 2021-05-01
* Date is optional

### Output of `Reverse mapping` Delimeter
```json
    {
        "2021-05-01": {
            "vps.treatmentdemo.com": {
                "Total": 1,
                "IPLIST": {
                    "69.90.223.232": 1
                }
            },
            "hn.kd.ny.adsl": {
                "Total": 1,
                "IPLIST": {
                    "42.236.73.19": 1
                }
            },
            "dynamicip-176-214-76-92.pppoe.yar.ertelecom.ru": {
                "Total": 1,
                "IPLIST": {
                    "176.214.76.92": 1
                }
            }
        }
    }
```

### Output of `Failed Password` Delimeter
```json
    {
        "2021-05-01": {
            "root": {
                "Total": 6,
                "IPLIST": {
                    "123.183.209.132": 3,
                    "115.238.245.8": 3
                }
            },
            "ubuntu": {
                "Total": 1,
                "IPLIST": {
                    "90.160.145.30": 1
                }
            },
            "production": {
                "Total": 1,
                "IPLIST": {
                    "69.90.223.232": 1
                }
            }
        }
    }
```
