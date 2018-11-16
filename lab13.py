class Foo:
    def __str__(self):
        return "foo object in string 的格式"

    def __repr__(self):
        return "foo object in repr 的格式"


f1 = Foo()
print(f1)
print((f1,))
print([f1])
print({f1})
print('%s, %r, %a' % (f1, f1, f1))
print('{0!r}, {0!s},{0!a}'.format(f1))