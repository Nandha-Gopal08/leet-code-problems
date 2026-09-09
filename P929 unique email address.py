def unique_email_address(emails):
    addreses = set()

    for email in emails:
        local,domain = email.split("@")
        print(local)
        if "+" in local:
            local = local[:local.index("+")]
        print(local)
        if "." in local:
            local = local.replace(".","")
        print(local)
        actual = local + "@" + domain
        print(actual)
        addreses.add(actual)
    return len(addreses)
emails = ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]
print(unique_email_address(emails))
