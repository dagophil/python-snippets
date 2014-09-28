import sys
import os
import string
import numpy


class Sudoku(object):
    """Basically a 9x9 numpy array with some additional functions."""

    def __init__(self, data):
        if len(data) != 81:
            raise Exception("Sudoku must have 81 numbers.")
        self._data = numpy.array(data).reshape((9, 9))
        orig_data = [a != 0 for a in data]
        self._orig_data = numpy.array(orig_data).reshape((9, 9))

    def __str__(self):
        return self._data.__str__()

    def increment(self, flat_index):
        self._data.flat[flat_index] += 1

    def is_orig(self, flat_index):
        return self._orig_data.flat[flat_index]

    def get_value(self, flat_index):
        return self._data.flat[flat_index]

    def set_value(self, flat_index, val):
        self._data.flat[flat_index] = val

    @staticmethod
    def _is_valid_data(data):
        """Returns whether the given data is valid."""
        assert len(data) == 9
        bins = numpy.bincount(data)[1:]
        for b in bins:
            if b > 1:
                return False
        return True

    def _is_valid_row(self, row_index):
        """Returns whether the given row is valid."""
        row = self._data[row_index, :]
        return Sudoku._is_valid_data(row)

    def _is_valid_column(self, col_index):
        """Returns whether the given column is valid."""
        col = self._data[:, col_index]
        return Sudoku._is_valid_data(col)

    def _is_valid_block(self, block_index):
        """Returns whether the given block is valid."""
        top_left = numpy.unravel_index(block_index, (3, 3))
        top_left = tuple(a*3 for a in top_left)
        data = self._data[top_left[0]:top_left[0]+3, top_left[1]:top_left[1]+3]
        return Sudoku._is_valid_data(data.ravel())

    def is_valid_after_change(self, flat_index):
        """Returns whether the Sudoku currently has a valid state,
        but only the fields influenced by the given index are checked."""
        index = numpy.unravel_index(flat_index, (9, 9))
        if not self._is_valid_row(index[0]):
            return False
        if not self._is_valid_column(index[1]):
            return False
        block_index = tuple(i/3 for i in index)
        block_index = numpy.ravel_multi_index(block_index, (3, 3))
        if not self._is_valid_block(block_index):
            return False
        return True

    def is_valid(self):
        """Returns whether the Sudoku currently has a valid state."""
        for i in range(9):
            if not self._is_valid_row(i):
                return False
            if not self._is_valid_column(i):
                return False
            if not self._is_valid_block(i):
                return False
        return True


def remove_digits(s):
    """Remove all digits from s and return the result."""
    all = string.maketrans('', '')
    nodigits = all.translate(all, string.digits)
    return s.translate(all, nodigits)


def solve(sud):
    """Solves the Sudoku in place."""
    assert isinstance(sud, Sudoku)
    current = 0
    direction = 1
    while current != 81:
        if not sud.is_orig(current):
            while sud.get_value(current) != 9:
                sud.increment(current)
                if sud.is_valid_after_change(current):
                    direction = 1
                    break
            else:
                direction = -1
                sud.set_value(current, 0)
                if current == 0:
                    raise Exception("The Sudoku does not have a valid solution.")
        current += direction


if __name__ == "__main__":
    # Get some input.
    input_data = []
    if len(sys.argv) > 1:
        # Get input from the given file.
        if not os.path.isfile(sys.argv[1]):
            raise Exception("Given argument must be a file.")
        with open(sys.argv[1], "r") as f:
            for line in f:
                line = remove_digits(line)
                input_data += [int(a) for a in line]
    else:
        # Read the input from the command line
        raise Exception("Reading from command line is not implemented yet.")

    # Create the sudoku object and solve it.
    s = Sudoku(input_data)
    print "Input:"
    print s
    solve(s)
    print "Solved:"
    print s
