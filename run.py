import os

if __name__=="__main__":
 while True:

  text = input("Enter what you want to speak : ")

  if text =="quit":
     break
  else:
   os.system(
    f'powershell -Command "Add-Type –AssemblyName System.Speech; '
    f'$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; '
    f'$speak.Speak(\'{text}\');"'
    )

