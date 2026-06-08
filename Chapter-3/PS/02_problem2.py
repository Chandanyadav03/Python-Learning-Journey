letter = '''
          Dear <|Name|>,
          You are selected!
         <|Date|> '''

print(letter.replace("<|Name|>", "Chandan").replace("<|Date|>","10-07-2027"))

