def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
       return False
    else:
      return True
  else:
    return False

def days_in_month(year,month):
  """"Will take a year and a month as inputsand it will use this information to work out the number of days in the month
     then return that as the output. """
# ΜΟΛΙΣ ΠΡΑΓΜΑΤΟΠΟΙΗΘΗΚΕ ΧΡΗΣΗ Dockstring, ΤΟ ΟΠΟΙΟ ΕΔΩ ΔΙΝΕΙ ΤΗ ΔΙΚΙΑ ΜΑΣ ΠΕΡΙΓΡΑΦΕΙ ΑΠΕΝΑΝΤΙ ΣΤΗΝ ΕΝΤΟΛΗ ΠΟΥ ΔΗΜΙΟΥΡΓΗΣΑΜΕ ΣΤΗΝ ΠΡΟΗΓΟΥΜΕΝΗ ΓΡΑΜΜΗ.
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if month < 1 or month > 12:
    return 'Invalid month'
# ΠΟΤΕ ΜΗΝ ΞΕΧΝΑΣ ΤΟ ΒΑΣΙΚΟ ΒΗΜΑ ΠΟΥ ΕΛΕΓΧΕΙ ΑΜΑ Ο ΧΡΗΣΤΗΣ ΠΛΗΚΤΡΟΛΟΓΕΙ ΕΓΚΥΡΟ ΠΕΡΙΕΧΟΜΕΝΟ!!!!!!
  if is_leap(year) and month == 2:
   return 29
  return month_days[month - 1]
# return > print , ΑΜΑ ΒΑΛΕΙΣ ΤΟ ΔΕΥΤΕΡΟ ΤΟΤΕ ΔΕΝ ΘΑ ΓΙΝΕΙ Η ΑΝΤΙΚΑΤΑΣΤΑΣΗ ΣΤΗ ΜΕΤΑΒΛΗΤΗ days ΓΙΑ ΑΥΤΟ ΤΟ ΑΠΟΤΕΛΕΣΜΑ ΘΑ ΕΙΝΑΙ: Νοne (ΕΚΤΟΣ ΑΜΑ ΑΦΑΙΡΕΣΕΙΣ ΕΠΙΠΛΕΟΝ ΤΗ ΣΕΙΡΑ 27)!

#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)