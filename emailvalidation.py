import re


def fun(s):
    pattern = re.compile('^([a-zA-Z0-9-_])+@([a-zA-Z0-9])+\.([a-zA-Z]){,3}$')
    return re.match(pattern, s)


def filter_email(emails):
    return list(filter(fun, emails))


n = int(input())
emails = []
for _ in range(n):
    emails.append(input())
filtered_emails = filter_email(emails)
filtered_emails.sort()
print(filtered_emails)