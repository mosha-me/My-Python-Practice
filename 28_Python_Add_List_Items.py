# আইটেম যুক্ত করুন
""" তালিকার শেষে কোনো আইটেম যোগ করতে, এই append() পদ্ধতিটি ব্যবহার করুন: """

# উদাহরণ
#আপনার append()একটি আইটেম যুক্ত করার পদ্ধতি ব্যবহার করা :

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# আইটেম ঢোকান
""" একটি নির্দিষ্ট ইন্ডেক্সে তালিকার কোনো আইটেম যোগ করতে, এই insert()মেথডটি ব্যবহার করুন। """
# এই insert()পদ্ধতিটি নির্দিষ্ট ইন্ডেক্সে একটি আইটেম সন্নিবেশ করে:

# উদাহরণ
# দ্বিতীয় অবস্থানে একটি আইটেম যোগ করুন:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# তালিকা প্রসারিত করুন
""" অন্য তালিকা থেকে বর্তমান তালিকায় উপাদান যুক্ত করতে , extend()পদ্ধতিটি ব্যবহার করুন। """

# উদাহরণ
# tropical এর উপাদানগুলো যোগ করুন thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# যেকোনো পুনরাবৃত্তি যোগ করুন
""" এই পদ্ধতিতে লিস্টextend() যুক্ত করার প্রয়োজন নেই , আপনি যেকোনো ইটারেবল অবজেক্ট (যেমন টাপল, সেট, ডিকশনারি ইত্যাদি) যোগ করতে পারেন। """

# উদাহরণ
# একটি টাপলের উপাদানগুলোকে একটি লিস্টে যোগ করুন:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)



