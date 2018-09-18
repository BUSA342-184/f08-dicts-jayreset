#! opt/bin/python
"""
Read text file 'mbox-short.txt', separate emails that are 'From' and 'To',
and print the usernames and hosts and their counts categorized by From Users, From Hosts,
To Users, and To Hosts
"""

emailList = []
fromUser = {}
fromHost = {}
toUser = {}
toHost = {}

# open text file as variable emails
with open('mbox-short.txt') as emails:
    # Read each line in the text file
    for i in emails:
        # split each line to read each word
        lines = i.split()
        # lines starting with the words 'From:' or 'To:' are appended to emailList
        if 'From:' in lines or 'To:' in lines:
            emailList.append(i)

for item in emailList:
    # separate and remove 'From:' and 'To:'
    email = item.split(':')[1].strip()
    # separate username and hostname
    user, host = email.split('@')
    # put usernames into user key of fromUser dictionary and hosts into host key of fromHost dictionary
    if item.startswith('From'):
        fromUser.setdefault(user, 0)
        fromHost.setdefault(host, 0)
        fromUser[user] += 1
        fromHost[host] += 1
    # put usernames into user key of toUser dictionary and hosts into host key of toHost dictionary
    elif item.startswith('To'):
        toUser.setdefault(user, 0)
        toHost.setdefault(host, 0)
        toUser[user] += 1
        toHost[host] += 1

print('--- FROM USER ---')
# print each username and their counts
for item, count in sorted(fromUser.items()):
    print(item, ",", count, '\n', sep='')


print('--- FROM HOST ---')
# print each hostname and their counts
for item, count in sorted(fromHost.items()):
    print(item, ",", count, '\n', sep='')

print('--- TO USER ---')
# print each username and their counts
for item, count in sorted(toUser.items()):
    print(item, ",", count, '\n', sep='')

print('--- TO HOST ---')
# print each hostname and their counts
for item, count in sorted(toHost.items()):
    print(item, ",", count, '\n', sep='')
