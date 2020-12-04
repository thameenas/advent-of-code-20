import re

valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def read_input(input_path="input_data.txt"):
    f = open(input_path)
    input_data = f.read().split('\n\n')
    f.close()
    return input_data


def contains_valid_fields(passport_dict):
    return len(set(valid_fields) - set(passport_dict.keys())) == 0


def validate_rules(passport_dict):
    return valid_byr(passport_dict['byr']) and valid_iyr(passport_dict['iyr']) and valid_eyr(
        passport_dict['eyr']) and valid_hgt(passport_dict['hgt']) and valid_ecl(passport_dict['ecl']) and valid_pid(
        passport_dict['pid']) and valid_hcl(passport_dict['hcl'])


def valid_hcl(hcl):
    return bool(re.search(r"^\#[0-9a-f]{6}$", hcl))


def valid_pid(pid):
    return len(pid) == 9 and pid.isdigit()


def valid_ecl(ecl):
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def valid_hgt(hgt):
    if len(hgt) > 2:
        if hgt[-2:] == 'cm':
            return 150 <= int(hgt[:-2]) <= 193
        if hgt[-2:] == 'in':
            return 59 <= int(hgt[:-2]) <= 76


def valid_eyr(eyr):
    return 2020 <= int(eyr) <= 2030


def valid_iyr(iyr):
    return 2010 <= int(iyr) <= 2020


def valid_byr(byr):
    return 1920 <= int(byr) <= 2002


def add_to_dict(s, passport_dict):
    field, value = s.split(":")
    passport_dict[field] = value


def check_validity(passport):
    passport_dict = {}
    passport_fields = re.split('[\n| ]', passport)
    for field in passport_fields:
        add_to_dict(field, passport_dict)
    if contains_valid_fields(passport_dict) and validate_rules(passport_dict):
        return True


def count_valid_passports(passport_list):
    count = 0
    for passport in passport_list:
        if check_validity(passport):
            count += 1
    return count


if __name__ == '__main__':
    passports = read_input()
    print(count_valid_passports(passports))
