# পলায়ন চরিত্র
# কোনো স্ট্রিং-এ অবৈধ অক্ষর প্রবেশ করাতে এস্কেপ ক্যারেক্টার ব্যবহার করুন।

# এস্কেপ ক্যারেক্টার হলো একটি ব্যাকস্ল্যাশের \পর আপনি যে অক্ষরটি ঢোকাতে চান সেটি।

# একটি অবৈধ অক্ষরের উদাহরণ হলো এমন একটি স্ট্রিংয়ের ভিতরে থাকা ডাবল কোট, যা আবার ডাবল কোট দ্বারা ঘেরা থাকে:

# উদাহরণ:
# যদি কোনো স্ট্রিং-এর ভেতরে ডাবল কোট ব্যবহার করা হয় এবং সেই স্ট্রিংটি ডাবল কোট দিয়ে ঘেরা থাকে, তাহলে আপনি একটি এরর পাবেন।

txt = "We are the so-called "Vikings" from the north."
# এই সমস্যাটি সমাধান করতে এস্কেপ ক্যারেক্টার : ব্যবহার করুন \"

# উদাহরণ:
# এস্কেপ ক্যারেক্টার আপনাকে এমন ক্ষেত্রেও ডাবল কোট ব্যবহার করার সুযোগ দেয়, যেখানে সাধারণত এর অনুমতি থাকে না:

txt = "We are the so-called \"Vikings\" from the north."

# পলায়ন চরিত্র
# পাইথনে ব্যবহৃত অন্যান্য এস্কেপ ক্যারেক্টার:

# \'	Single Quote:
txt = 'It\'s alright.'
print(txt) 

# \\	Backslash:
txt = "This will insert one \\ (backslash)."
print(txt) 

# \n	New Line:
txt = "Hello\nWorld!"
print(txt) 

# \r	 Carriage Return:
txt = "Hello\rWorld!"
print(txt) 

# \t Tab:
txt = "Hello\tWorld!"
print(txt) 

# \b	Backspace:
txt = "Hello \bWorld!"
print(txt) 

# \f	 Form Feed:
txt = "Hello \fWorld!"
print(txt) 

# \ooo	Octal value:
txt = "\110\145\154\154\157"
print(txt) 

# \xhh	Hex value
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

# ------------------------------------------------------

#  Text → Oct / Hex
# 1. টেক্সট → Number → octal/Hex

# "A" নম্বর এ রূপান্তর |
''' আগে অক্ষর এর ASCII বের করতে হবে ord () দিয়ে |
তারপর octal/Hex এ রূপান্তর। '''

print (ord ("A"))
# =65

# 2. Number → Octal/Hex

print (oct (65))
print (hex (65))
# = 0o101
# = 0x41

# মানে,
octal = 101
Hex = 41

# 3. Escape firmat বানানো। ( এটা একটা সহজ উপায় সরাসরি Hex Oct Number থেকে text এ তৈরি )
print ("\\101")
print("\\x41")
# =A
# =A

# Oct / Hex → Text 
# 1. Oct → Number → Text :

print(int("101" 8)
# =65

# Number → Text
A = Chr(65)
print(A)
# =A

# একসাথে
print(chr(int("101", 8)))
# =A

# 2. Hex → Numbere → Text:

print (int ("41", 16))
# = 65

# Number → Text
print (chr(65))
# =A

# একসাথে
print(chr(int("41",16)))
# =A

"""
ord() = text → number 
chr() = number → text
Oct() = number → octal
hex() = number → hex
"""

