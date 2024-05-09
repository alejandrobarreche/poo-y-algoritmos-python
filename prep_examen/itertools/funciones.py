from itertools import *


class ChainingExamples:
    @staticmethod
    def chain_example():
        print("Chaining Example:")
        for i in chain([1, 2, 3], ['a', 'b', 'c']):
            print(i, end=' ')
        print()

    @staticmethod
    def chain_from_iterable_example():
        print("Chaining from Iterable Example:")
        def make_iterables_to_chain():
            yield [1, 2, 3]
            yield ['a', 'b', 'c']
        
        for i in chain.from_iterable(make_iterables_to_chain()):
            print(i, end=' ')
        print()


class ZippingExamples:
    @staticmethod
    def zip_example():
        print("Zipping Example:")
        for i in zip([1, 2, 3], ['a', 'b', 'c']):
            print(i)

    @staticmethod
    def zip_longest_example():
        print("Zip Longest Example:")
        r1 = range(3)
        r2 = range(2)
        print('zip stops early:')
        print(list(zip(r1, r2)))

        r1 = range(3)
        r2 = range(2)
        print('\nzip_longest processes all of the values:')
        print(list(zip_longest(r1, r2)))


class SlicingExamples:
    @staticmethod
    def islice_example():
        print("islice Example:")
        print('Stop at 5:')
        for i in islice(range(100), 5):
            print(i, end=' ')
        print('\n')

        print('Start at 5, Stop at 10:')
        for i in islice(range(100), 5, 10):
            print(i, end=' ')
        print('\n')

        print('By tens to 100:')
        for i in islice(range(100), 0, 100, 10):
            print(i, end=' ')
        print('\n')


class MappingExamples:
    @staticmethod
    def map_example():
        print("Map Example:")
        def times_two(x):
            return 2 * x

        def multiply(x, y):
            return (x, y, x * y)

        print('Doubles:')
        for i in map(times_two, range(5)):
            print(i)

        print('\nMultiples:')
        r1 = range(5)
        r2 = range(5, 10)
        for i in map(multiply, r1, r2):
            print('{:d} * {:d} = {:d}'.format(*i))

        print('\nStopping:')
        r1 = range(5)
        r2 = range(2)
        for i in map(multiply, r1, r2):
            print(i)


class CountingExamples:
    @staticmethod
    def count_example():
        print("Count Example:")
        for i in zip(count(1), ['a', 'b', 'c']):
            print(i)


class CyclingExamples:
    @staticmethod
    def cycle_example():
        print("Cycle Example:")
        for i in zip(range(7), cycle(['a', 'b', 'c'])):
            print(i)


class RepeatingExamples:
    @staticmethod
    def repeat_example():
        print("Repeat Example:")
        for i in repeat('over-and-over', 5):
            print(i)


class FilteringExamples:
    @staticmethod
    def dropwhile_example():
        print("Dropwhile Example:")
        def should_drop(x):
            print('Testing:', x)
            return x < 1

        for i in dropwhile(should_drop, [-1, 0, 1, 2, -2]):
            print('Yielding:', i)

    @staticmethod
    def takewhile_example():
        print("Takewhile Example:")
        def should_take(x):
            print('Testing:', x)
            return x < 2

        for i in takewhile(should_take, [-1, 0, 1, 2, -2]):
            print('Yielding:', i)

    @staticmethod
    def filter_example():
        print("Filter Example:")
        def check_item(x):
            print('Testing:', x)
            return x < 1

        for i in filter(check_item, [-1, 0, 1, 2, -2]):
            print('Yielding:', i)

    @staticmethod
    def compress_example():
        print("Compress Example:")
        every_third = cycle([False, False, True])
        data = range(1, 10)

        for i in compress(data, every_third):
            print(i, end=' ')
        print()


class GroupingExamples:
    @staticmethod
    def groupby_example():
        print("Groupby Example:")
        data = [(0, 0), (1, 1), (2, 2), (0, 3), (1, 4), (2, 5), (0, 6)]
        for k, g in groupby(data, lambda x: x[0]):
            print(k, list(g))


class AccumulatingExamples:
    @staticmethod
    def accumulate_example():
        print("Accumulate Example:")
        print(list(accumulate(range(5))))


if __name__ == "__main__":
    ChainingExamples.chain_example()
    ChainingExamples.chain_from_iterable_example()
    ZippingExamples.zip_example()
    ZippingExamples.zip_longest_example()
    SlicingExamples.islice_example()
    MappingExamples.map_example()
    CountingExamples.count_example()
    CyclingExamples.cycle_example()
    RepeatingExamples.repeat_example()
    FilteringExamples.dropwhile_example()
    FilteringExamples.takewhile_example()
    FilteringExamples.filter_example()
    FilteringExamples.compress_example()
    GroupingExamples.groupby_example()
    AccumulatingExamples.accumulate_example()
