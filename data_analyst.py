import re
def extract_data(file_path,email_file,phone_file):
    email_pattern = r"[a-zA-Z0-9_.+-]@[a-zA-Z0-9-.]+"
    phone_pattern = r"\+\d{1,2} \d{3} \d{3} \d{4}"

    with open(file_path,'r') as reviews_file, open(email_file,'w') as emails_file, open(phone_file,'w') as phones_file:
        for line in reviews_file:
            emails = re.findall(email_pattern, line)
            phones = re.findall(phone_pattern, line)

            for email in emails:
                emails_file.write(email + '\n')
            for phone in phones:
                phones_file.write(phone + '\n')

if __name__ == '__main__':
    file_path = 'reviews.txt'
    email_file = 'emails.txt'
    phone_file = 'phone_numbers.txt'

    extract_data(file_path,email_file,phone_file)


    print(f"Extracted email address written to: {email_file}")
    print(f"Extracted phone numbers written to {phone_file}")
