studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
   antw = []
   for studentcijfers in studentencijfers:
       antw.append(sum(studentcijfers) / len(studentcijfers))
   return antw

def gemiddelde_van_alle_studenten(studentencijfers):
   antw = 0
   aant_cijfers = 0
   for studentcijfers in studentencijfers:
       for cijfer in studentcijfers:
           antw += cijfer
           aant_cijfers += 1
   return antw / aant_cijfers

print(gemiddelde_per_student(studentencijfers))

print(gemiddelde_van_alle_studenten(studentencijfers))