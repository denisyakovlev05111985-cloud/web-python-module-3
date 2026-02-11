clients= {
   (1, '111','a@x.com'),
   (2, '111','b@x.com'),
   (3, '222','c@x.com'),
   (4, '333','c@x.com'),
   (5, '444','d@x.com'),
}
phones= {}
emails= {}

duble= []
duble_ids= set()
not_duble= []

for id, phone, email in clients:
    phones.setdefault(phone, set()).add(id)
    emails.setdefault(email, set()).add(id)
print(phones, emails)

for o in (phones, emails):
    for ids in o.values():
        if len(ids) > 1:
            duble.append(ids)
print(duble)
print(not_duble)

for n in duble:
    duble_ids |= n
print(duble_ids)

for id, phone, email  in clients:
    if id not in duble_ids:
        not_duble.append(id)
print(not_duble, len(not_duble))