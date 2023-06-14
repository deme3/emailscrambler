import re

def rot(charRot: int, numRot: int, string: str) -> str:
  """
    Code ported from https://github.com/ThibWeb/email-scramble
    Licensed under ISC License, Copyright (c) 2016, Thibaud Colas
  """
  NUMBERS = '0123456789'
  LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
  UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  REG_NUMBERS = re.compile(r'[0-9]')
  REG_LOWERCASE = re.compile(r'[a-z]')
  REG_UPPERCASE = re.compile(r'[A-Z]')
  
  if charRot < 0:
    charRot = charRot + 26
  
  if numRot < 0:
    numRot = numRot + 10
  
  length = len(string)
  index = -1
  result = ''
  character = ''
  currentPos = ''
  shiftedPos = ''

  while index < length - 1:
    index = index + 1
    character = string[index]
    
    if REG_NUMBERS.match(character):
      currentPos = NUMBERS.find(character)
      shiftedPos = (currentPos + numRot) % 10
      character = NUMBERS[shiftedPos]
    elif REG_LOWERCASE.match(character):
      currentPos = LOWERCASE.find(character)
      shiftedPos = (currentPos + charRot) % 26
      character = LOWERCASE[shiftedPos]
    elif REG_UPPERCASE.match(character):
      currentPos = UPPERCASE.find(character)
      shiftedPos = (currentPos + charRot) % 26
      character = UPPERCASE[shiftedPos]
    
    result = result + character
  
  return result

def scramble(email: str) -> str:
  return rot(13, 5, email)

def unscramble(email: str) -> str:
  return rot(13, 5, email)

def obfuscate(string: str) -> str:
  """Takes in a string and returns it encoded in HTML hex codes"""
  result = ''
  for char in string:
    result = result + '&#x' + hex(ord(char))[2:] + ';'
  return result

def javascriptify(emailto: str, custom_caption: str = None, body: str = None, do_scramble: bool = False) -> str:
  """Takes in an e-mail address and returns a JavaScript-enabled obfuscated mailto link"""
  if body:
    body = body.replace('\n', '%0D%0A')

  caption = (obfuscate(scramble(custom_caption)) if custom_caption else obfuscate(emailto)) if custom_caption else None
  mail_output = obfuscate(scramble(emailto)) if do_scramble else obfuscate(emailto)
  mail_body = (obfuscate(scramble(body)) if do_scramble else obfuscate(body)) if body else None
  return '<script type="text/javascript">document.write(\'<a href="mailto:' + mail_output + '"' + (" data-scrambled" if do_scramble else "") + (f" data-body=\"{mail_body}\"" if body else "") + (f" data-custom-caption=\"{caption}\"" if custom_caption else '') + '>' + mail_output + '</a>\');</script>'

def deobfuscator() -> str:
  """
    Code adapted from https://github.com/ThibWeb/email-scramble
    Licensed under ISC License, Copyright (c) 2016, Thibaud Colas
  """
  return """
<script type="text/javascript">
  (function() {
    function rot(charRot, numRot, string) {
      var NUMBERS = '0123456789';
      var LOWERCASE = 'abcdefghijklmnopqrstuvwxyz';
      var UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
      var REG_NUMBERS = /[0-9]/;
      var REG_LOWERCASE = /[a-z]/;
      var REG_UPPERCASE = /[A-Z]/;

      if (charRot < 0) {
        charRot = charRot + 26;
      }

      if (numRot < 0) {
        numRot = numRot + 10;
      }

      var length = string.length;
      var index = -1;
      var result = '';
      var character = '';
      var currentPos = '';
      var shiftedPos = '';

      while (index < length - 1) {
        index = index + 1;
        character = string[index];

        if (REG_NUMBERS.test(character)) {
          currentPos = NUMBERS.indexOf(character);
          shiftedPos = (currentPos + numRot) % 10;
          character = NUMBERS[shiftedPos];
        } else if (REG_LOWERCASE.test(character)) {
          currentPos = LOWERCASE.indexOf(character);
          shiftedPos = (currentPos + charRot) % 26;
          character = LOWERCASE[shiftedPos];
        } else if (REG_UPPERCASE.test(character)) {
          currentPos = UPPERCASE.indexOf(character);
          shiftedPos = (currentPos + charRot) % 26;
          character = UPPERCASE[shiftedPos];
        }

        result = result + character;
      }

      return result;
    }

    function deobfuscate() {
      let elements = document.querySelectorAll('a[data-scrambled]');

      for(let element of elements) {
        element.href = 'mailto:' + rot(13, 5, element.innerHTML) + (element.dataset.body ? '?body=' + rot(13, 5, element.dataset.body) : '');

        if (element.dataset.customCaption) {
          element.innerHTML = rot(13, 5, element.dataset.customCaption);
        } else {
          element.innerHTML = rot(13, 5, element.innerHTML);
        }
        element.removeAttribute('data-scrambled');
        element.removeAttribute('data-body');
      }
    }

    document.addEventListener('DOMContentLoaded', deobfuscate);
  })();
</script>
  """
