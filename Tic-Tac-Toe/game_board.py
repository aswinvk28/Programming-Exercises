def draw_game_board(user_input=[2,1], player='o', previous=None):
  dashed_lines = """ --- --- --- """
  entries = """|   |   |   |"""
  result = [dashed_lines, entries, dashed_lines, entries, dashed_lines, entries, dashed_lines]
  array = result[user_input[0]*2 + 1]
  array = array[:(user_input[1]*4 + 2)] + player + array[(user_input[1]*4 + 2):]
  result[user_input[0]*2 + 1] = array
  return "\n".join(result)

if __name__ == "__main__":
  print(draw_game_board())
  