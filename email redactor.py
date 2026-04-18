email = input("Give me your email: ")
final = ("")
for i in range(len(email)):
    email.find(email[i])
    if email.find(email[i]) == "@":
        email[email.find(email[i:])]
    if i == 0:
        final = final + email[i]
    else:
        if(email[i] == ("@")):
            final = final + email[i]
            break
        else:
            final = final + ("*")
final = final + ("gmail.com")
print(final)

