import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"[A-Z][a-z_']*(?:'[A-Z])?[a-z_']*(?:[\s-][A-Z][a-z_']*(?:'[A-Z])?[a-z_']*)*"
name_regex = re.compile(name)
name_regex.fullmatch(name)

phone_number = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
phone_regex = re.compile(phone_number)
phone_regex.fullmatch(phone_number)

email_address = r"[A-Za-z][A-za-z.0-9]*@[A-z]*.[A-z]*"
email_regex = re.compile(email_address)
