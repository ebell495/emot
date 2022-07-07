#!/usr/local/bin/python3
import atheris
import emot
import sys

emot_obj = emot.core.emot() 

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    if len(data) < 1:
        return

    option = fdp.ConsumeBytes(1)[0]
    in_string = fdp.ConsumeUnicodeNoSurrogates(len(data))

    if option % 4 == 0:
        emot_obj.emoji(in_string)
    elif option % 4 == 1:
        emot_obj.emoticons(in_string)
    elif option % 4 == 2:
        emot_obj.bulk_emoji(in_string.split(" "))
    else:
        emot_obj.bulk_emoticons(in_string.split(" "))
    

atheris.instrument_all()
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()