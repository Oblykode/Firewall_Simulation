import random 

def random_ipgenerator():
    random_num = random.randint(0,20)
    return [f"192.168.1.{random_num}", random_num] # 192.168.1.7

def check_firewall_rules(ip , rules):
    for rule_ip , action in rules:
        if ip[0] == rule_ip:
            return action
    return "ALLOW"


def main():
    firewall_rules = {
        "192.168.1.1" : "block",
        "192.168.1.4":  "block",
        "192.168.1.9" : "block",
        "192.168.1.20": "block",
        "192.168.1.16" : "block",
        "192.168.1.5" : "block"
    }


    for i in range(10):
        ip = random_ipgenerator()
        action = check_firewall_rules(ip , firewall_rules.items())
        print(f"IP Address : {ip[0]} - Action : {action} , Random - {ip[1]}")


if __name__ == "__main__":
    main()



