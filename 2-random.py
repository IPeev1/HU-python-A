import random

def monopolyworp():
    dob1_1 = random.randrange(1, 7)
    dob1_2 = random.randrange(1, 7)
    dob2_1 = random.randrange(1, 7)
    dob2_2 = random.randrange(1, 7)
    dob3_1 = random.randrange(1, 7)
    dob3_2 = random.randrange(1, 7)

    if dob1_1 == dob1_2:
        if dob2_1 == dob2_2:
            if dob3_1 == dob3_2:
                print('%d + %d = %d (dubbel)' % (dob1_1, dob1_2, (dob1_1 + dob1_2)))
                print('%d + %d = %d (dubbel)' % (dob2_1, dob2_2, (dob2_1 + dob2_2)))
                print('%d + %d = (direct naar gevangenis)\n' % (dob3_1, dob3_2))
            else:
                print('%d + %d = %d (dubbel)' % (dob1_1, dob1_2, (dob1_1 + dob1_2)))
                print('%d + %d = %d (dubbel)' % (dob2_1, dob2_2, (dob2_1 + dob2_2)))
                print('%d + %d = %d\n' % (dob3_1, dob3_2, (dob3_1 + dob3_2)))
        else:
            print('%d + %d = %d (dubbel)' % (dob1_1, dob1_2, (dob1_1 + dob1_2)))
            print('%d + %d = %d\n' % (dob2_1, dob2_2, (dob2_1 + dob2_2)))
    else:
        print('%d + %d = %d\n' % (dob1_1, dob1_2, (dob1_1 + dob1_2)))

monopolyworp()
