class Test(object):
	def enter(self):
		print("This is a test object")

class SubTest(Test):
	def test_enter(self):
		print("This is a subclassed test object")


thing = Test()

sub_thing = SubTest()

thing.enter()
sub_thing.enter()

sub_thing.test_enter()