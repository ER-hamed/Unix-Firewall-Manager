#! /usr/bin/python3

# from os import system
from sys import argv
system = print

class IptablesManager:
    def __init__(self):
        self.never_close = [22, 80, 443]
        self.close_other = False

    def handle(self):
        while True:
            self.clear()
            self.show()
            self.command(input('Command: '))

    def command(self, command):
        command = command.split(' ')
        if command[0] == '' or command[0] == 'exit':
            self.clear()
            exit()

        elif command[0] == 'open':
            self.open(int(command[1]))

        elif command[0] == 'close':
            self.close(int(command[1]))

        elif command[0] == 'remove':
            self.remove(int(command[1]))

        elif command[0] == 'flush':
            self.flush()

        elif command[0] == 'set':
            self.set()

        elif command[0] == 'unset':
            self.unset()

        else:
            pass

    def open(self, port: int):
        if port in self.never_close:
            print('Warning: ' + str(port) + ' in not_close list')
        else:
            # filtering input
            port = str(port)
            # remove DROP all
            system('sudo iptables -D INPUT -j DROP')
            # remove port if already exist in rules
            self.remove(int(port))
            # open port
            system('sudo iptables -A INPUT -p tcp --dport ' + port + ' -j ACCEPT')
            if self.close_other:
                # add DROP all
                system('sudo iptables -A INPUT -j DROP')

    def close(self, port: int):
        if port in self.never_close:
            print('Warning: ' + str(port) + ' in not_close list')
        else:
            # filtering input
            port = str(port)
            # remove DROP all
            system('sudo iptables -D INPUT -j DROP')
            # remove port if already exist in rules
            self.remove(int(port))
            # close port
            system('sudo iptables -A INPUT -p tcp --dport ' + port + ' -j DROP')
            if self.close_other:
                # add DROP all
                system('sudo iptables -A INPUT -j DROP')

    def remove(self, port: int):
        if port in self.never_close:
            print('Warning: ' + str(port) + ' in not_close list')
        else:
            # filtering input
            port = str(port)
            # remove port if in ACCEPT
            system('sudo iptables -D INPUT -p tcp --dport ' + port + ' -j ACCEPT')
            # remove port if in DROP
            system('sudo iptables -D INPUT -p tcp --dport ' + port + ' -j DROP')

    @staticmethod
    def flush():
        system('sudo iptables -F')

    @staticmethod
    def clear():
        system('clear')

    @staticmethod
    def show():
        system('sudo iptables -L --line-numbers')

    def set(self):
        for port in self.never_close:
            self.open(port)
        self.close_other = True

    def unset(self):
        for port in self.never_close:
            self.open(port)
        self.close_other = False


if len(argv) == 3:
    iptables_manager = IptablesManager()
    iptables_manager.command(argv[1] + ' ' + argv[2])
    iptables_manager.show()
else:
    iptables_manager = IptablesManager()
    iptables_manager.handle()
