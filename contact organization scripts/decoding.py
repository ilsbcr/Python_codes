import quopri



#CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:


vcard ="""

BEGIN:VCARD
VERSION:2.1
N;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:AAAAA;;;
FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:=AAAAA
TEL;CELL:050000000
END:VCARD


"""


# Extract FN line
fn_line = [line for line in vcard.splitlines() if line.startswith("FN")][0]
encoded_name = fn_line.split(":",1)[1]

# Decode quoted-printable into UTF-8
decoded_name = quopri.decodestring(encoded_name).decode("utf-8")

print("Full Name:", decoded_name)
