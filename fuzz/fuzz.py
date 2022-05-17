#!/usr/local/bin/python3
import atheris
import emot
import sys

emot_obj = emot.core.emot() 

@atheris.instrument_func
def TestOneInput(data):
    barray = bytearray(data)
    # emot_obj.emoji(str(data))
    if len(barray) > 0:
        if barray[0] % 4 == 0:
            del barray[0]
            emot_obj.emoji(str(barray))
        elif barray[0] % 4 == 1:
            del barray[0]
            emot_obj.emoticons(str(barray))
        elif barray[0] % 4 == 2:
            del barray[0]
            emot_obj.bulk_emoji(str(barray).split(" "))
        elif barray[0] % 4 == 3:
            del barray[0]
            emot_obj.bulk_emoticons(str(barray).split(" "))
    else:
        emot_obj.emoji(str(barray))
    

atheris.instrument_all()
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()