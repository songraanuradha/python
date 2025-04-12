import example2


words = int(input("Enter your words"))
one,two,three = example2.toAmount_into_rupee(words)
# two = example2.toAmount_into_rupee(words)
# three = example2.toAmount_into_rupee(words)

print(f"One = {one}  Two = {two} Three = {three}")