import re

password_list = ['fjd3IR9', 'ghdfj32', 'DSJKHD23', 'dsF43', '4fdg5Fj3', 'DHSJdhjsU', 'fjd3IR9.;', 'fjd3  IR9', 'djI38D55', 'a2.d412', 'JHD5FJ53', '!fdjn345', 'jfkdfj3j', '123', 'abc', '123abcABC', 'ABC123abc', 'Password123']

def regex_password(password):
    regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$'
    # Au moins une lettre minuscule
    # Au moins une lettre majuscule
    # Au moins un chiffre
    # Au moins 6 charactères au total.
    is_match = True
    match = re.search(regex, password)
    if match:
        is_match = True
        return f"Mot de passe : '{password}' avec RegEx => is_match {is_match}"
    elif match is None:
        is_match = False
        return f"Mot de passe : '{password}' avec RegEx => is_match {is_match}"

for password in password_list:
    print(regex_password(password))