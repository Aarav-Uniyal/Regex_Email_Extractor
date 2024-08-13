import re

string = '''
This is a test string for email detection.
Are bhai pareshaan mat karo ye lo mera e-mail:
aarav@gmail.com
ye to fake tha ab asli waala deta hun:
heryetueuj@yahoo.com
are main to yahoo par hoon hi nhi chalo ek aur lelo:
atlan@email.com
email? ye kaisi site hai
chalo yaar bye main to mazaak kar rha tha.
goodbye@dost.com
reyteue@bdbfg.com.com.com
tfye6@@@@ghg.com
kaisa lagaa joke.
mujhe patta hai main dimaag kha rha hun.
Isliye byeeeeeeeeeeeee...........

'''


def email_extractor():
    response = re.compile(r'\w+@\S\w+.com')
    find = response.findall(string)
    for results in find:
        with open("Ex11(Test).txt", "a") as file:
            file.write(results + "\n")


if __name__ == '__main__':
    email_extractor()
    print("The emails have been recorded.")
