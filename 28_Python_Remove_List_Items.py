# নির্দিষ্ট আইটেমটি সরান
""" এই remove()পদ্ধতিটি নির্দিষ্ট আইটেমটি মুছে ফেলে। """

# উদাহরণ
# 'banana' বাদ দিন:

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

""" নির্দিষ্ট মান সহ একাধিক আইটেম থাকলে, remove()পদ্ধতিটি প্রথমটি সরিয়ে দেয়: """

# উদাহরণ
# 'banana'-এর প্রথম উপস্থিতিটি মুছে ফেলুন:

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# নির্দিষ্ট সূচক অপসারণ করুন
""" এই pop()পদ্ধতিটি নির্দিষ্ট ইনডেক্সটি মুছে দেয়। """

# উদাহরণ
# দ্বিতীয় আইটেমটি সরান:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

""" আপনি ইন্ডেক্স নির্দিষ্ট না করলে, pop()মেথডটি শেষ আইটেমটি মুছে দেয়। """

# উদাহরণ
# শেষ আইটেমটি সরান:

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

""" কীওয়ার্ডটি del নির্দিষ্ট ইনডেক্সটিও মুছে দেয়: """

# উদাহরণ
# প্রথম আইটেমটি সরান:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# তালিকাটি পরিষ্কার করুন
""" এই clear()পদ্ধতিটি তালিকাটি খালি করে দেয়। """

""" তালিকাটি এখনও আছে, কিন্তু এর কোনো বিষয়বস্তু নেই। """

# উদাহরণ
# তালিকার বিষয়বস্তু মুছে ফেলুন:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


