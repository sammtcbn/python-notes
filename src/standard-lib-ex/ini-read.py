import configparser

def main():

    config = configparser.ConfigParser()
    config.read('ini-read.ini')

    nginx_ip   = config['nginx']['ip']
    nginx_port = config['nginx'].getint('port')

    mysql_ip   = config['mysql']['ip']
    mysql_port = config['mysql'].getint('port')
    mysql_user = config['mysql']['user']
    mysql_pw   = config['mysql']['password']
    mysql_db   = config['mysql']['database']

    print("nginx ip  : " + nginx_ip)
    print("nginx port:", nginx_port)

    print("mysql ip      : " + mysql_ip)
    print("mysql port    :", mysql_port)
    print("mysql user    : " + mysql_user)
    print("mysql password: " + mysql_pw)
    print("mysql database: " + mysql_db)

main()

