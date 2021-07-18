from absl.testing import absltest
from absl.testing import parameterized
from rotate import rotate_return


class UnitTests(parameterized.TestCase):
	@parameterized.named_parameters(
		{
			'testcase_name': 'plus1',
          		'input1': 3,
          		'input2': 5,
          		'want': 8,
      		},
      		{
          		'testcase_name': 'plus2',
          		'input1': 6,
          		'input2': -2,
          		'want': 4,
      		})

	def testSum(self, input1, input2, want):
    		self.assertEqual(plus.FindSum(input1, input2), want)	

if __name__ == '__main__':
    absltest.main()
