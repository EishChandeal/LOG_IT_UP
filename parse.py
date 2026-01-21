import re 
from collections import defaultdict

pattern  = "404"

def find_404(file_name):
    try:
        with open(file_name) as file:
            error_count = 0
            for line in file:
                if (re.search(pattern, line)):
                    error_count += 1
                if not line:
                    break
            return error_count
    except FileNotFoundError:
        print(f"{file_name} : does not exist")
    except Exception as e:
        print(f"error : {e} just occured!")


# result  = find_404("server.log")
# print(result)

IP_Pattern = re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}\b")

with open("server.log") as f:
    new_line = f.readline()
    new = IP_Pattern.search(new_line)
    if new:
        print(new.group())

def count_ips(file_name):
    try:
        with open(file_name, "r") as file:
            ip_address_no = defaultdict(int)
            for line in file:
                match = IP_Pattern.search(line)
                if match:
                    val = match.group()
                    ip_address_no[val] += 1
            return dict(ip_address_no)
    except FileNotFoundError:
        print(f"{file_name} : does not exist")
    except Exception as e:
        print(f"error : {e} just occured!")

# 192.168.1.1 -> format to look for using regex expression
# counting the frequencies for each of these IP's 
# noting them down by maintaining a count (using dictionaries)
# initially dictionary will be empty -> then 
# for the first term that is encountered , if not in dict then create a key out of it and 
# initialize it with value of 1

new_dict = count_ips("server.log")
print(new_dict)

# don't blindly trust any tool , refer to docs for the syntax or method they tell you about.
# treating it as an interactive documentation read through.