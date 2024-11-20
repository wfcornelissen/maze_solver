import unittest
from maze import *

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 10
        num_rows = 5
        cell_size_x = 30
        cell_size_y = 30
        win = Window(cell_size_x* num_cols, cell_size_y* num_rows)
        m1 = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y, win)
        self.assertEqual(len(m1._cells),num_cols,)
        self.assertEqual(len(m1._cells[0]),num_rows,)
        win.wait_for_close()


    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        cell_size_x = 30
        cell_size_y = 30
        win = Window(cell_size_x* num_cols, cell_size_y* num_rows)
        m1 = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y, win)
        self.assertEqual(m1._cells[0][0].has_top_wall,False,)
        self.assertEqual(m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,False,)
        win.wait_for_close()
    

if __name__ == "__main__":
    unittest.main()