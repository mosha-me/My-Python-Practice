# প্রোগ্রামিংয়ে ডেটা টাইপ একটি গুরুত্বপূর্ণ ধারণা।

# ভেরিয়েবল বিভিন্ন ধরনের ডেটা সংরক্ষণ করতে পারে এবং বিভিন্ন ধরনের ভেরিয়েবল বিভিন্ন কাজ করতে পারে।

# পাইথনে ডিফল্টরূপে নিম্নলিখিত ডেটা টাইপগুলো বিল্ট-ইন থাকে, যা এই বিভাগগুলোর অন্তর্ভুক্ত:

""" টেক্সট টাইপ:	str
সংখ্যাসূচক প্রকার:	int, float, complex
ক্রমের প্রকারভেদ:	list, tuple, range
ম্যাপিং প্রকার:	dict
সেটের প্রকারভেদ:	set,frozenset
বুলিয়ান প্রকার:	bool
বাইনারি প্রকার:	bytes, bytearray, memoryview
কোনো প্রকার নয়:	NoneType """

# এই ফাংশনটি ব্যবহার করে আপনি যেকোনো অবজেক্টের ডেটা টাইপ জানতে পারবেন type():

# উদাহরণ:
# x ভেরিয়েবলটির ডেটা টাইপ প্রিন্ট করুন:

x = 5
print(type(x))

# ডেটা টাইপ নির্ধারণ করা:
# পাইথনে, কোনো ভেরিয়েবলে মান অ্যাসাইন করার সময় ডেটা টাইপ সেট করা হয়:

""" x = "Hello World"	➜	str	
x = 20 ➜ int	
x = 20.5 ➜	float	
x = 1j ➜	complex	
x = ["apple", "banana", "cherry"]	➜ list	
x = ("apple", "banana", "cherry")	➜ tuple	
x = range(6) ➜ range	
x = {"name" : "John", "age" : 36} ➜ dict	
x = {"apple", "banana", "cherry"}	➜ set	
x = frozenset({"apple", "banana", "cherry"}) ➜ frozenset	
x = True	 ➜ bool	
x = b"Hello" ➜	 bytes	
x = bytearray(5) ➜ bytearray	
x = memoryview(bytes(5)) ➜	memoryview	
x = None ➜ NoneType """

# নির্দিষ্ট ডেটা টাইপ সেট করা

""" x = str("Hello World")	
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name="John", age=36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5)) """
