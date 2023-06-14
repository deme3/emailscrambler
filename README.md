# mailscrambler

A simple Python library to scramble and obfuscate email addresses in HTML pages, also comes with JavaScript deobfuscator.

## Installation

```bash
pip install mailscrambler
```

## Usage

```python
from mailscrambler import scramble, obfuscate, javascriptify, deobfuscator

# Scramble an email address
scrambled = scramble('test@email.com')
print(scrambled) # grfg@rznvy.pbz

# Obfuscate an email address
obfuscated = obfuscate('test@email.com')
print(obfuscated)
"""
&#x74;&#x65;&#x73;&#x74;&#x40;&#x65;&#x6d;&#x61;&#x69;&#x6c;&#x2e;&#x63;&#x6f;&#x6d;
"""

# HTML Embeddable
link = javascriptify('test@email.com')
"""
<script type="text/javascript">document.write('<a href="mailto:&#x74;&#x65;&#x73;&#x74;&#x40;&#x65;&#x6d;&#x61;&#x69;&#x6c;&#x2e;&#x63;&#x6f;&#x6d;">&#x74;&#x65;&#x73;&#x74;&#x40;&#x65;&#x6d;&#x61;&#x69;&#x6c;&#x2e;&#x63;&#x6f;&#x6d;</a>');</script>
"""

# Combine scramble and obfuscate
link = javascriptify('test@email.com', do_scramble=True)
"""
<script type="text/javascript">document.write('<a href="mailto:&#x67;&#x72;&#x66;&#x67;&#x40;&#x72;&#x7a;&#x6e;&#x76;&#x79;&#x2e;&#x70;&#x62;&#x7a;" data-scrambled>&#x67;&#x72;&#x66;&#x67;&#x40;&#x72;&#x7a;&#x6e;&#x76;&#x79;&#x2e;&#x70;&#x62;&#x7a;</a>');</script>
"""

# "Click <here> to report your issue":
support_email = javascriptify('support@test.com', body='Name: \nProduct you encountered the issue with: \nYour issue:\n', custom_caption='here', do_scramble=True)
"""
Click {support_email} to report your issue
<script type="text/javascript">document.write('<a href="mailto:&#x66;&#x68;&#x63;&#x63;&#x62;&#x65;&#x67;&#x40;&#x67;&#x72;&#x66;&#x67;&#x2e;&#x70;&#x62;&#x7a;" data-scrambled data-body="&#x41;&#x6e;&#x7a;&#x72;&#x3a;&#x20;&#x25;&#x35;&#x51;&#x25;&#x35;&#x4e;&#x43;&#x65;&#x62;&#x71;&#x68;&#x70;&#x67;&#x20;&#x6c;&#x62;&#x68;&#x20;&#x72;&#x61;&#x70;&#x62;&#x68;&#x61;&#x67;&#x72;&#x65;&#x72;&#x71;&#x20;&#x67;&#x75;&#x72;&#x20;&#x76;&#x66;&#x66;&#x68;&#x72;&#x20;&#x6a;&#x76;&#x67;&#x75;&#x3a;&#x20;&#x25;&#x35;&#x51;&#x25;&#x35;&#x4e;&#x4c;&#x62;&#x68;&#x65;&#x20;&#x76;&#x66;&#x66;&#x68;&#x72;&#x3a;&#x25;&#x35;&#x51;&#x25;&#x35;&#x4e;" data-custom-caption="&#x75;&#x72;&#x65;&#x72;">&#x66;&#x68;&#x63;&#x63;&#x62;&#x65;&#x67;&#x40;&#x67;&#x72;&#x66;&#x67;&#x2e;&#x70;&#x62;&#x7a;</a>');</script>
```

To embed a deobfuscator in your HTML page, you can call the `deobfuscator` function:

```python
from mailscrambler import deobfuscator

# [...]

# Embed the deobfuscator
page_body += javascriptify('test@email.com', do_scramble=True)
page_body += deobfuscator()

# [...]
```

Note that unless scrambling is used, deobfuscator is not necessary.

## License

MIT License

```
MIT License

Copyright (c) 2023 Demetrio Battaglia

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
