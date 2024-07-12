def passkey():
    import random as r
    import time as t
    
    passkey1234 = input("Enter preferred numbers you can remember. It cannot be changed later: ")
    name = input("Enter name: ")
    password = input("Enter password: ")
    
    random_integer = r.randint(1, 1230)
    generated_product = int(passkey1234) * random_integer
    
    with open("passkeys.txt", 'a') as f:
        f.write(f"key: {passkey1234}, name: {name}, password: {password}, code: {generated_product}\n")
    
    with open("random_integers.txt", 'a') as f:
        f.write(f"name: {name}, random_integer: {random_integer}\n")
    
    t.sleep(2)
    print("Details updated")

def signin():
    name1 = input("Enter user name: ")
    password1 = input("Enter user password: ")
    
    with open("passkeys.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            details = line.strip().split(", ")
            if len(details) < 4:
                continue
            
            stored_name = details[1].split(": ")[1]
            stored_password = details[2].split(": ")[1]
            stored_passkey = details[0].split(": ")[1]
            stored_code = int(details[3].split(": ")[1])
            
            if name1 == stored_name and password1 == stored_password:
                with open("random_integers.txt", 'r') as f2:
                    random_lines = f2.readlines()
                    for random_line in random_lines:
                        random_details = random_line.strip().split(", ")
                        if len(random_details) < 2:
                            continue
                        if random_details[0].split(": ")[1] == stored_name:
                            stored_random_integer = int(random_details[1].split(": ")[1])
                            if int(stored_passkey) * stored_random_integer == stored_code:
                                print("Logged in")
                                return
                            else:
                                print("Error in passkeys")
                                return
        print("Try again")

# Uncomment these to test the functions
#passkey()
signin()
