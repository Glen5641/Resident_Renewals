class Resident:
    def __init__(self, name, apt, letter, phone, email):
        self.name = name
        self.apt = int(apt)
        self.letter = [letter]
        self.phone = phone
        self.email = email
        self.rent = []
        self.plan = ''
        self.month = 0
        self.day = 0
        self.year = 0

    def setData(self, rent, plan, month, day, year):
        self.rent.append(rent)
        self.plan = plan
        self.month = month
        self.day = day
        self.year = year

    def exists(self, name):
        if self.name == name:
            return True
        return False

    def exist(self, apt, letter):
        if self.apt == int(apt):
            for i in self.letter:
                if i == letter:
                    return True
        return False

    def addLetter(self, letter):
        self.letter.append(letter)

    def printResident(self):
        print('Name:       ' + self.name)
        print('Apt:        ' + str(self.apt) + str(self.letter))
        print('Phone:      ' + self.phone)
        print('Email:      ' + self.email)
        print('Rent:       ' + str(self.rent))
        print('Plan:       ' + str(self.plan))
        print('Expiration: ' + str(self.month) + '/' + str(self.day) + '/' + str(self.year))
        print()



if __name__ == "__main__":
    residents = []
    lines = open(r"C:\{AlphaList_file}.csv", "r").read().splitlines()
    lines = lines[8:len(lines)-12]
    for i in lines:
        parts = i.split(',')
        name = str(parts[0][0:len(parts[0])-1])
        apt = parts[5][5:len(parts[5])]
        letter = ''
        if len(apt) > 1:
            letter = apt[len(apt)-1]
            apt = apt[0:len(apt)-1]
        phone = parts[10]
        email = parts[14]
        if not (phone == '(   )    -') and not (phone == '') and not (email == ''):
            exist = False
            for j in residents:
                if j.exists(name):
                    j.addLetter(letter)
                    exist = True
            if not exist:
                residents.append(Resident(name, apt, letter, phone, email))
    residents = sorted(sorted(residents, key=lambda resident: resident.letter), key=lambda resident: resident.apt)

    lines = open(r"C:\{Renewals_File}.csv", "r").read().splitlines()
    lines = lines[15:len(lines)-12]

    for i in lines:
        parts = i.split(',')
        if not parts[0] == '':
            if parts[0][0] == '0':
                apt = str(parts[0][3:len(parts[0])-1])
                letter = parts[0][len(parts[0])-1]
                plan = str(parts[1])
                name = str(parts[5])
                rent = str(parts[16][0:len(parts[16])-1])
                expiration = str(parts[len(parts)-9])
                month = str(expiration[0:2])
                day = str(expiration[3:5])
                year = str(expiration[6:len(expiration)])
                for j in residents:
                    if j.exist(apt, letter):
                        j.setData(rent, plan, month, day, year)

    f = open(r"C:{master_file}.csv", "w+")
    for j in residents:
        j.printResident()
        f.write("%s,%d,%s,%s/%s/%s" %(j.name,j.apt,j.plan,j.month,j.day,j.year))
        for i in range(4):
            try:
                f.write(",%s" %(j.rent[i]))
            except IndexError:
                f.write(",")
        f.write("\n")

    f.close()
